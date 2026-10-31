// Standalone, asset-free side-on 3D fighting spike for OpenOMF.
#define SDL_MAIN_HANDLED
#include "live_input.h" // pulls in windows.h; must precede epoxy/gl.h (APIENTRY)
#include <SDL.h>
#include <epoxy/gl.h>
#include <xmp.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/stat.h>
#ifdef _WIN32
#include <direct.h>
#endif

#include "source_replay.h"
#include "pose_catalog.h"
#include "story.h"
#include "projection_poses.h"
#include "model_meshes.h"
#include "meshy_meshes.h"

#ifdef _WIN32
// Ask Optimus to start this executable on the discrete GPU. Windows graphics
// preferences can still override the request on newer Windows releases.
__declspec(dllexport) unsigned long NvOptimusEnablement = 1;
#endif

#define WIDTH 960
#define HEIGHT 600
#define DT (1.0f / 60.0f)
#define VERT_CAP 400000

typedef struct { float x, y, vy, facing, hp, max_hp, cooldown, attack, stun; int kind; bool hit, guard;
                 int source_state, source_animation, source_sprite, source_animation_tick;
                 float pose_height, pose_stride, pose_reach, pose_lean, pose_depth, presentation_x; } Fighter;
typedef struct { float x, y, z, r, g, b; } Vertex;
typedef struct { char ch; unsigned char rows[7]; } Glyph;

static Vertex vertices[VERT_CAP];
static int vertex_count;
static float camera_x;
static float camera_y;
static int phase; // 0 briefing, 1 fight, 2 victory, 3 defeat
static int try_again_choice; // 0 yes, 1 no
static int source_live_winner = -1;
// --result-file: when the live match is decided, write the winner here, hold the final pose briefly, and
// exit, so a story can read the result. Replaces the retry prompt.
static const char *live_result_path;
static bool live_result_written;
static double live_result_timer;
static bool restart_live_match;
static Fighter player, rival;
static float elapsed;
static float source_visual_time;
static float live_round_intro_time;
static float live_impact_time;
static float live_impact_x;
static int live_impact_kind; // 1 hit, 2 block
static float rival_attack_delay;
static bool jump_was_down;
static int win_width = WIDTH, win_height = HEIGHT;
static SourceReplay source_replay;
static SourceFollow source_follow;
static size_t source_replay_index;
static bool source_replay_mode;
static bool source_follow_mode;
static const char *source_input_path;
static bool source_input_enabled;
static Uint64 source_follow_arrival;
#ifdef _WIN32
static HANDLE source_input_mapping;
static Omf3kLiveInput *source_shared_input;
static const char *source_state_map_name;
static HANDLE source_state_mapping;
static Omf3kLiveState *source_shared_state;
static size_t source_shared_capacity;
#endif
static bool source_replay_paused;
static float source_tick_seconds = .028f;
static bool model_preview_mode;
static int model_preview_view; // 0 right side, 1 front, 2 back
static int model_preview_pose; // idle, punch, kick, guard, crouch, walk, jump, hit, special
static const char *source_live_pilot_name;
static const char *source_live_rival_name;
static bool selection_mode;
// Story mode: plays a scene script (story.h) with a dialogue box, choices, skip, and a log.
static bool story_mode;
static Story story_data;
static StoryRun story_run;
static const char *story_start_scene;
static int story_sel;
static bool story_log_open;
static int story_match_state;              // real match: 0 idle, 1 running, 2 closed without a result
static char story_match_message[96];
static bool story_debug_fights;   // --debug-fights: matches can be skipped by choosing the result
static bool story_save_enabled;
static char story_save_buf[512];
static const char *story_save_path;
static char story_notice[96];
static Uint64 story_notice_until;
static bool story_notice_pending;
// Selection screen: shown first when the script declares a player and a rival, until a HAR is confirmed.
static bool story_setup;
static int story_setup_har;          // 0 Jaguar, 1 Shadow
typedef struct { int w,h; unsigned char *rgb; } StoryPortrait;
static StoryPortrait story_portraits[2];   // the player's pilot, then the rival's
// Power, agility and endurance of the ten playable pilots, copied from src/resources/pilots.c (OpenOMF).
static const struct { const char *name; int power,agility,endurance; } story_pilot_stats[] = {
    {"Crystal",5,16,9},{"Steffan",13,9,8},{"Milano",7,20,4},{"Christian",9,7,15},{"Shirro",20,1,8},
    {"JeanPaul",9,10,11},{"Ibrahim",10,1,20},{"Angel",7,10,13},{"Cossette",14,8,8},{"Raven",14,4,12}
};
static const char *selection_path;
static int selection_har;
static int selection_pilot;

static const char *selection_pilot_names[] = {
    "CRYSTAL", "STEFFAN", "MILANO", "CHRISTIAN", "SHIRRO",
    "JEANPAUL", "IBRAHIM", "ANGEL", "COSSETTE", "RAVEN"
};
static const char *selection_har_names[] = {"JAGUAR", "SHADOW"};

static bool write_selection(void) {
    if(!selection_path || !*selection_path) return false;
    FILE *file=fopen(selection_path,"w");
    if(!file) return false;
    fprintf(file,"har=%s\npilot=%s\n",selection_har_names[selection_har],
            selection_pilot_names[selection_pilot]);
    fclose(file);
    return true;
}

static void request_live_restart(void) {
    if(live_result_path) return;   // a story match is played once; its result is final
    restart_live_match = true;
#ifdef _WIN32
    if(source_shared_input) InterlockedExchange(&source_shared_input->restart_requested, 1);
#endif
}

static const Glyph font[] = {
    {'A',{14,17,17,31,17,17,17}}, {'B',{30,17,17,30,17,17,30}},
    {'C',{14,17,16,16,16,17,14}}, {'D',{30,17,17,17,17,17,30}},
    {'E',{31,16,16,30,16,16,31}}, {'F',{31,16,16,30,16,16,16}},
    {'G',{14,17,16,23,17,17,14}}, {'H',{17,17,17,31,17,17,17}},
    {'I',{14,4,4,4,4,4,14}}, {'J',{7,2,2,2,18,18,12}},
    {'K',{17,18,20,24,20,18,17}}, {'L',{16,16,16,16,16,16,31}},
    {'M',{17,27,21,21,17,17,17}}, {'N',{17,25,21,19,17,17,17}},
    {'O',{14,17,17,17,17,17,14}}, {'P',{30,17,17,30,16,16,16}},
    {'Q',{14,17,17,17,21,18,13}}, {'R',{30,17,17,30,20,18,17}},
    {'S',{15,16,16,14,1,1,30}}, {'T',{31,4,4,4,4,4,4}},
    {'U',{17,17,17,17,17,17,14}}, {'V',{17,17,17,17,17,10,4}},
    {'W',{17,17,17,21,21,21,10}}, {'X',{17,17,10,4,10,17,17}},
    {'Y',{17,17,10,4,4,4,4}}, {'Z',{31,1,2,4,8,16,31}},
    {'0',{14,17,19,21,25,17,14}}, {'1',{4,12,4,4,4,4,14}},
    {'2',{14,17,1,2,4,8,31}}, {'3',{30,1,1,14,1,1,30}},
    {'4',{2,6,10,18,31,2,2}}, {'5',{31,16,30,1,1,17,14}},
    {'6',{6,8,16,30,17,17,14}}, {'7',{31,1,2,4,8,8,8}},
    {'8',{14,17,17,14,17,17,14}}, {'9',{14,17,17,15,1,2,12}},
    {':',{0,4,4,0,4,4,0}}, {'.',{0,0,0,0,0,12,12}},
    {'-',{0,0,0,31,0,0,0}}, {'/',{1,1,2,4,8,16,16}},
    {'!',{4,4,4,4,4,0,4}}, {'?',{14,17,1,2,4,0,4}},
    {',',{0,0,0,0,12,4,8}}, {'\'',{4,4,8,0,0,0,0}}, {'"',{10,10,0,0,0,0,0}},
    {'(',{2,4,8,8,8,4,2}}, {')',{8,4,2,2,2,4,8}}, {';',{0,12,12,0,12,4,8}},
    {'>',{16,8,4,2,4,8,16}}, {'<',{1,2,4,8,4,2,1}}, {'_',{0,0,0,0,0,0,31}},
    {' ',{0,0,0,0,0,0,0}}
};

static float clampf(float x, float a, float b) { return x < a ? a : (x > b ? b : x); }
static float distance_x(const Fighter *a, const Fighter *b) { return fabsf(a->x - b->x); }
static int facing_dir(const Fighter *f) { return f->facing < 0 ? 1 : -1; }
static bool source_standing_kick(int har, int animation) {
    return (har==0 && animation==41) || (har==1 && animation==42);
}
static bool source_standing_punch(int har, int animation) {
    return (har==0 && animation==42) || (har==1 && animation==43);
}
static bool source_close_contact_attack(int har, int animation) {
    return source_standing_punch(har,animation) || source_standing_kick(har,animation) ||
           (har==0 && animation==30) || (har==1 && animation==23);
}
static void reset_fight(void) {
    player = (Fighter){.x=-3.0f, .facing=-1.5707963f, .hp=100, .max_hp=100};
    rival = (Fighter){.x=3.0f, .facing=1.5707963f, .hp=100, .max_hp=100};
    elapsed = 0;
    rival_attack_delay = 2.5f;
    jump_was_down = false;
    try_again_choice = 0;
    phase = 1;
}
static void apply_source_fighter(Fighter *dest, const SourceFighter *source) {
    // OpenOMF's arena spans x=20..300 with a y=190 floor.
    // Match source screen spacing and apparent speed while allowing the
    // side-view meshes to fill the original sprites' horizontal silhouettes.
    const float x_scale = 7.6f / 280.0f, y_scale = 12.0f / 280.0f;
    dest->x = (source->x - 160.0f) * x_scale;
    dest->y = (190.0f - source->y) * y_scale;
    dest->vy = -source->vy * y_scale;
    dest->facing = source->facing == 1 ? -1.5707963f : 1.5707963f;
    dest->hp = fmaxf(0.0f, (float)source->health);
    dest->max_hp = (float)source->max_health;
    // Values mirror har.h states and animation.h's common animation IDs.
    dest->source_state = source->state;
    dest->source_animation = source->animation;
    dest->source_sprite = source->sprite;
    dest->source_animation_tick = source->animation_tick;
    dest->guard = source->state == 5 || source->state == 10 ||
                  source->animation == 5 || source->animation == 6;
    dest->stun = source->state == 7 || source->state == 9 || source->state == 10 ||
                 source->state == 12 ? 1.0f : 0.0f;
    bool kick=source_standing_kick(source->har,source->animation);
    bool punch=source_standing_punch(source->har,source->animation);
    dest->kind = kick ? 2 : 1;
    int duration = kick ? 15 : punch ? (source->har==0 ? 8 : 13) : 23;
    float progress = clampf((float)source->animation_tick / (float)duration,0,1);
    dest->attack = (kick || punch || source->animation == 20)
                       ? 1.0f : 0.0f;
    dest->pose_reach = dest->attack ? sinf(progress * 3.14159265f) : 0;
    const PoseFrame *pose=pose_catalog_lookup(source->har,source->animation,source->sprite);
    if(pose && (pose->flags&POSE_REACH)) dest->pose_reach=pose->reach;
    dest->pose_height = (source->state == 4 || source->state == 5 ||
                         source->animation == 4 || source->animation == 6) ? .68f : 1.0f;
    dest->pose_stride = (source->state == 2 || source->state == 3) ?
                         sinf((float)source->animation_tick * .75f) * .30f : 0;
}
static void apply_source_frame(size_t index) {
    const SourceFrame *frame = &source_replay.frames[index];
    source_replay_index = index;
    apply_source_fighter(&player, &frame->fighter[0]);
    apply_source_fighter(&rival, &frame->fighter[1]);
    if(frame->has_events && (frame->hit_mask || frame->block_mask)) {
        int hit=frame->hit_mask;
        int recipient=hit ? (hit&1 ? 0 : 1) : (frame->block_mask&1 ? 0 : 1);
        live_impact_x=recipient==0 ? player.x : rival.x;
        live_impact_kind=hit ? 1 : 2;
        live_impact_time=.20f;
    } else if(source_follow_mode && !frame->has_events && index>0) {
        const SourceFrame *previous=&source_replay.frames[index-1];
        if(frame->fighter[0].health<previous->fighter[0].health) {
            live_impact_x=player.x;
            live_impact_kind=1;
            live_impact_time=.20f;
        } else if(frame->fighter[1].health<previous->fighter[1].health) {
            live_impact_x=rival.x;
            live_impact_kind=1;
            live_impact_time=.20f;
        }
    }
    elapsed = frame->tick * source_tick_seconds;
    phase = 1;
    if(source_follow_mode && frame->has_match_result) {
        if(source_live_winner < 0 && frame->match_winner >= 0) {
            source_live_winner = frame->match_winner;
            try_again_choice = 0;
        } else if(restart_live_match && frame->match_winner < 0) {
            source_live_winner = -1;
            restart_live_match = false;
            try_again_choice = 0;
        }
    }
}
static void interpolate_live_fighters(Uint64 now, bool exact) {
    if(!source_follow_mode || source_replay_index == 0 || !source_follow_arrival) return;
    const SourceFrame *previous = &source_replay.frames[source_replay_index-1];
    const SourceFrame *current = &source_replay.frames[source_replay_index];
    float blend = exact ? 1.0f : clampf((float)((double)(now-source_follow_arrival) /
                  (double)SDL_GetPerformanceFrequency() / source_tick_seconds),0,1);
    Fighter before, after;
    apply_source_fighter(&before,&previous->fighter[0]);
    apply_source_fighter(&after,&current->fighter[0]);
    player.x=before.x+(after.x-before.x)*blend;
    player.y=before.y+(after.y-before.y)*blend;
    apply_source_fighter(&before,&previous->fighter[1]);
    apply_source_fighter(&after,&current->fighter[1]);
    rival.x=before.x+(after.x-before.x)*blend;
    rival.y=before.y+(after.y-before.y)*blend;
    elapsed=((float)previous->tick+blend)*source_tick_seconds;
}
// Presentation only: the source turns a fighter in a single tick (for example when a get-up begins), so ease the
// displayed yaw over a few ticks instead of snapping the mesh through 180 degrees. Position, state, and hit logic
// still read the source. Seeking, frame jumps, and captures snap so screenshots stay exact.
static void smooth_source_facing(double dt, bool snap) {
    static float shown[2];
    static bool valid;
    static size_t last_index;
    if(!source_replay.count) return;
    if(!valid || snap || source_replay_index>last_index+3 || source_replay_index+3<last_index) {
        for(int i=0;i<2;i++) {
            const SourceFighter *f=&source_replay.frames[source_replay_index].fighter[i];
            shown[i]=f->facing==1 ? -1.5707963f : 1.5707963f;
        }
        valid=true;
    } else {
        const float max_step=(float)(dt*3.14159265/.15);
        for(int i=0;i<2;i++) {
            const SourceFighter *f=&source_replay.frames[source_replay_index].fighter[i];
            float target=f->facing==1 ? -1.5707963f : 1.5707963f;
            float delta=target-shown[i];
            shown[i]+=clampf(delta,-max_step,max_step);
        }
    }
    last_index=source_replay_index;
    player.facing=shown[0];
    rival.facing=shown[1];
}
static void write_source_input(const unsigned char *keys) {
    if(!source_input_enabled) return;
    static int last_action = -1;
    static Uint64 last_write_ms;
    // Match src/controller/controller.h ACT flags; OpenOMF owns all move logic.
    int action = 0;
    if(keys) {
        if(keys[SDL_SCANCODE_A] && !keys[SDL_SCANCODE_D]) action |= 0x20;
        if(keys[SDL_SCANCODE_D] && !keys[SDL_SCANCODE_A]) action |= 0x40;
        if(keys[SDL_SCANCODE_W] && !keys[SDL_SCANCODE_S]) action |= 0x08;
        if(keys[SDL_SCANCODE_S] && !keys[SDL_SCANCODE_W]) action |= 0x10;
        if(keys[SDL_SCANCODE_J]) action |= 0x04;
        if(keys[SDL_SCANCODE_K]) action |= 0x02;
    }
    action = action ? action : 1;
#ifdef _WIN32
    if(source_shared_input) {
        InterlockedExchange(&source_shared_input->action,action);
        InterlockedExchange(&source_shared_input->heartbeat_ms,(LONG)GetTickCount());
        return;
    }
#endif
    Uint64 now=SDL_GetTicks64();
    if(keys && action==last_action && now-last_write_ms<250) return;
    FILE *file=fopen(source_input_path,"w");
    if(file) {
        fprintf(file,"%lld %d\n",(long long)time(NULL),action);
        fclose(file);
        last_action=action;
        last_write_ms=now;
    }
}
#ifdef _WIN32
static int poll_shared_source_state(char *error, size_t error_size) {
    if(!source_shared_state) {
        source_state_mapping=OpenFileMappingA(FILE_MAP_ALL_ACCESS,FALSE,source_state_map_name);
        if(!source_state_mapping) return 0;
        source_shared_state=MapViewOfFile(source_state_mapping,FILE_MAP_ALL_ACCESS,0,0,sizeof(Omf3kLiveState));
        if(!source_shared_state) {
            CloseHandle(source_state_mapping);
            source_state_mapping=NULL;
            return 0;
        }
    }
    Omf3kLiveState snapshot;
    bool consistent=false;
    for(int attempt=0;attempt<3;attempt++) {
        LONG first=InterlockedCompareExchange(&source_shared_state->sequence,0,0);
        if(first&1) continue;
        MemoryBarrier();
        memcpy(&snapshot,(const void *)source_shared_state,sizeof(snapshot));
        MemoryBarrier();
        LONG second=InterlockedCompareExchange(&source_shared_state->sequence,0,0);
        if(first==second && !(second&1)) { consistent=true; break; }
    }
    if(!consistent || snapshot.fighter[0].max_health<=0 || snapshot.fighter[1].max_health<=0 ||
       snapshot.match_winner < -1 || snapshot.match_winner > 1 ||
       snapshot.hit_mask < 0 || snapshot.hit_mask > 3 ||
       snapshot.block_mask < 0 || snapshot.block_mask > 3 ||
       snapshot.round_winner < -1 || snapshot.round_winner > 1 ||
       snapshot.projectile_count < 0 ||
       snapshot.projectile_count > OMF3K_LIVE_PROJECTILE_MAX) return 0;
    uint32_t tick=(uint32_t)snapshot.tick;
    if(source_replay.count && tick<=source_replay.frames[source_replay.count-1].tick) {
        // After a requested rematch, a fresh arena may restart the source tick count.
        if(!restart_live_match || snapshot.match_winner>=0 ||
           tick==source_replay.frames[source_replay.count-1].tick) return 0;
        source_replay.count=0;
        source_replay_index=0;
        source_follow_arrival=0;
    }
    if(source_replay.count==source_shared_capacity) {
        if(source_shared_capacity>=1000000) {
            snprintf(error,error_size,"Live source state exceeds one million frames");
            return -1;
        }
        size_t next_capacity=source_shared_capacity ? source_shared_capacity*2 : 256;
        SourceFrame *frames=realloc(source_replay.frames,next_capacity*sizeof(*frames));
        if(!frames) {
            snprintf(error,error_size,"Out of memory reading live source state");
            return -1;
        }
        source_replay.frames=frames;
        source_shared_capacity=next_capacity;
    }
    _Static_assert(sizeof(SourceFighter)==sizeof(Omf3kLiveFighter),"Live fighter layout mismatch");
    SourceFrame *frame=&source_replay.frames[source_replay.count++];
    frame->tick=tick;
    memcpy(frame->fighter,snapshot.fighter,sizeof(frame->fighter));
    frame->match_winner=snapshot.match_winner;
    frame->has_match_result=1;
    frame->hit_mask=snapshot.hit_mask;
    frame->block_mask=snapshot.block_mask;
    frame->round_winner=snapshot.round_winner;
    frame->has_events=1;
    _Static_assert(sizeof(SourceProjectile)==sizeof(Omf3kLiveProjectile),"Live projectile layout mismatch");
    frame->projectile_count=snapshot.projectile_count;
    memcpy(frame->projectile,snapshot.projectile,
           (size_t)frame->projectile_count*sizeof(*frame->projectile));
    return 1;
}
#endif
static const char *source_har_name(int id) {
    static const char *names[] = {"JAGUAR", "SHADOW", "THORN", "PYROS", "ELECTRA", "KATANA",
                                  "SHREDDER", "FLAIL", "GARGOYLE", "CHRONOS", "NOVA"};
    return id >= 0 && id < (int)(sizeof(names) / sizeof(names[0])) ? names[id] : "HAR";
}
static void strike(Fighter *a, Fighter *b, int kind) {
    if(a->cooldown > 0 || a->stun > 0 || a->hp <= 0) return;
    a->kind = kind;
    a->attack = kind == 1 ? .27f : .44f;
    a->cooldown = kind == 1 ? .48f : .78f;
    a->hit = false;
    (void)b;
}
static void update_fighter(Fighter *a, Fighter *b, float move, bool jumping) {
    a->cooldown = fmaxf(0, a->cooldown - DT);
    a->stun = fmaxf(0, a->stun - DT);
    if(a->attack > 0) {
        a->attack = fmaxf(0, a->attack - DT);
        float active = a->kind == 1 ? .17f : .27f;
        if(!a->hit && a->attack <= active) {
            a->hit = true;
            float reach = a->kind == 1 ? 2.2f : 2.8f;
            if(distance_x(a, b) <= reach && fabsf(a->y-b->y) < 1.35f &&
               (b->x-a->x)*facing_dir(a) > 0 && b->hp > 0) {
                float damage = a == &player ? (a->kind == 1 ? 11.0f : 19.0f)
                                            : (a->kind == 1 ? 5.0f : 9.0f);
                if(b->guard) damage *= .2f;
                else b->stun = a->kind == 1 ? .22f : .38f;
                b->hp = fmaxf(0, b->hp - damage);
                b->x = clampf(b->x + facing_dir(a)*(b->guard ? .08f : .36f), -7.2f, 7.2f);
            }
        }
    }
    if(a->stun <= 0) {
        if(jumping && a->y <= 0 && a->vy <= 0) a->vy = 8.2f;
        // Jaguar's AF file lists forward/reverse speeds as 5/4. The world-unit
        // scale remains provisional until the source match is measured.
        float speed = a->attack > 0 ? 1.2f : (move * facing_dir(a) < 0 ? 3.52f : 4.4f);
        a->x = clampf(a->x + move * speed * DT, -7.2f, 7.2f);
    }
    a->y = fmaxf(0, a->y + a->vy * DT);
    a->vy = a->y > 0 ? a->vy - 22.0f * DT : 0;
    // Facing is discrete. Screen directions never depend on which side a HAR occupies.
    a->facing = a->x <= b->x ? -1.5707963f : 1.5707963f;
}
static void tick(const unsigned char *keys) {
    if(phase != 1) return;
    // Resolve facing before reading directional actions, including the tick
    // when a jumping fighter crosses to the other side.
    player.facing = player.x <= rival.x ? -1.5707963f : 1.5707963f;
    rival.facing = rival.x <= player.x ? -1.5707963f : 1.5707963f;
    elapsed += DT;
    rival_attack_delay = fmaxf(0, rival_attack_delay - DT);
    // Holding an attack repeats it when ready; a missed key press during
    // recovery no longer leaves the player standing still.
    if(keys[SDL_SCANCODE_K]) strike(&player, &rival, 2);
    else if(keys[SDL_SCANCODE_J]) strike(&player, &rival, 1);
    float move = (float)(keys[SDL_SCANCODE_D] != 0) - (float)(keys[SDL_SCANCODE_A] != 0);
    bool jump_down = keys[SDL_SCANCODE_W] != 0;
    bool jump = jump_down && !jump_was_down;
    jump_was_down = jump_down;
    float dist = distance_x(&player, &rival);
    float ai_move = dist > 1.9f ? (float)(player.x > rival.x ? 1 : -1) : 0;
    if(dist < 2.6f && rival_attack_delay <= 0 && rival.cooldown <= 0 && rival.stun <= 0) {
        strike(&rival, &player, ((int)(elapsed * 1.7f) % 3) == 0 ? 2 : 1);
        rival_attack_delay = 1.4f;
    }
    player.guard = move * facing_dir(&player) < 0 && !jump && player.y <= 0 &&
                   player.stun <= 0 && player.attack <= 0;
    // The placeholder AI can defend without the player input mapping.
    rival.guard = dist < 2.7f && player.attack > .12f &&
                  ((int)(elapsed * 1.5f) % 4 == 0) && rival.y <= 0 &&
                  rival.stun <= 0 && rival.attack <= 0;
    update_fighter(&player, &rival, move, jump);
    update_fighter(&rival, &player, ai_move, false);
    // Grounded bodies push apart; a jump can cross over an opponent.
    float dx = rival.x - player.x;
    if(fabsf(dx) < 1.05f && player.y < 1.0f && rival.y < 1.0f) {
        float side = dx >= 0 ? 1.0f : -1.0f;
        float push = (1.05f - fabsf(dx)) * .5f;
        player.x = clampf(player.x - side*push, -7.2f, 7.2f);
        rival.x = clampf(rival.x + side*push, -7.2f, 7.2f);
    }
    player.facing = player.x <= rival.x ? -1.5707963f : 1.5707963f;
    rival.facing = rival.x <= player.x ? -1.5707963f : 1.5707963f;
    if(rival.hp <= 0) phase = 2;
    if(player.hp <= 0) phase = 3;
}

static void vertex(float x, float y, float z, float r, float g, float b) {
    if(vertex_count < VERT_CAP) vertices[vertex_count++] = (Vertex){x,y,z,r,g,b};
    else {
        static bool warned;
        if(!warned) { warned=true; fprintf(stderr,"vertex buffer full (%d); geometry is being dropped\n",VERT_CAP); }
    }
}
static void projected(float x, float y, float z, float r, float g, float b) {
    // Fixed side-on camera. Depth adds only a small vertical offset for 3D staging.
    float aspect = (float)win_width / (float)win_height;
    if(model_preview_mode) {
        vertex(x*.96f/(3.5f*aspect), (y-1.61f)*.88f/2.15f,
               (.50f*(10.0f-y)+.84f*(17.0f-z))/40.0f, r,g,b);
        return;
    }
    float sx = (x - camera_x) * .96f / ((source_replay_mode ? 3.0f : 4.8f) * aspect);
    float sy = source_replay_mode ? ((y - camera_y) * .84f - z * .16f) / 4.6f - .10f
                                  : ((y - camera_y) * .84f - z * .16f) / 4.2f - .20f;
    float depth = (.12f * (camera_x - x) + .50f * (10.0f - y) + .84f * (17.0f - z)) / 40.0f;
    vertex(sx, sy, depth, r, g, b);
}
static void face(float a[3], float b[3], float c[3], float d[3], float rgb[3], float light) {
    projected(a[0],a[1],a[2],rgb[0]*light,rgb[1]*light,rgb[2]*light);
    projected(b[0],b[1],b[2],rgb[0]*light,rgb[1]*light,rgb[2]*light);
    projected(c[0],c[1],c[2],rgb[0]*light,rgb[1]*light,rgb[2]*light);
    projected(a[0],a[1],a[2],rgb[0]*light,rgb[1]*light,rgb[2]*light);
    projected(c[0],c[1],c[2],rgb[0]*light,rgb[1]*light,rgb[2]*light);
    projected(d[0],d[1],d[2],rgb[0]*light,rgb[1]*light,rgb[2]*light);
}
static void box(float x,float y,float z,float sx,float sy,float sz,float yaw,float r,float g,float b) {
    float p[8][3], rgb[3] = {r,g,b};
    float co = cosf(yaw), si = sinf(yaw);
    for(int i=0;i<8;i++) {
        float lx = (i&1 ? .5f : -.5f)*sx, ly = (i&2 ? .5f : -.5f)*sy;
        float lz = (i&4 ? .5f : -.5f)*sz;
        p[i][0]=x+lx*co+lz*si; p[i][1]=y+ly; p[i][2]=z-lx*si+lz*co;
    }
    face(p[0],p[4],p[6],p[2],rgb,.52f); // left
    face(p[1],p[3],p[7],p[5],rgb,.72f); // right
    face(p[0],p[1],p[5],p[4],rgb,.76f); // bottom
    face(p[2],p[6],p[7],p[3],rgb,1.15f); // top
    face(p[0],p[2],p[3],p[1],rgb,.86f); // front
    face(p[4],p[5],p[7],p[6],rgb,.62f); // rear
}
static void part(const Fighter *f,float x,float y,float z,float sx,float sy,float sz,float r,float g,float b) {
    float co=cosf(f->facing), si=sinf(f->facing);
    float height=f->pose_height > 0 ? f->pose_height : 1.0f;
    z-=f->pose_lean*(y-1.38f);
    box(f->x+x*co+z*si,y*height+f->y,-x*si+z*co,sx,sy*height,sz,f->facing,r,g,b);
}
static void tapered_part(const Fighter *f,float y,float bottom_w,float top_w,float bottom_d,float top_d,
                         float height,float r,float g,float b) {
    float p[8][3], rgb[3]={r,g,b}, co=cosf(f->facing), si=sinf(f->facing);
    for(int i=0;i<8;i++) {
        bool top=(i&2)!=0;
        float lx=(i&1 ? .5f : -.5f)*(top ? top_w : bottom_w);
        float lz=(i&4 ? .5f : -.5f)*(top ? top_d : bottom_d);
        lz-=f->pose_lean*(y+(top ? height*.5f : -height*.5f)-1.38f);
        p[i][0]=f->x+lx*co+lz*si;
        float pose_height=f->pose_height > 0 ? f->pose_height : 1.0f;
        p[i][1]=f->y+(y+(top ? height*.5f : -height*.5f))*pose_height;
        p[i][2]=-lx*si+lz*co;
    }
    face(p[0],p[4],p[6],p[2],rgb,.55f);
    face(p[1],p[3],p[7],p[5],rgb,.80f);
    face(p[0],p[1],p[5],p[4],rgb,.58f);
    face(p[2],p[6],p[7],p[3],rgb,1.22f);
    face(p[0],p[2],p[3],p[1],rgb,.96f);
    face(p[4],p[5],p[7],p[6],rgb,.68f);
}
static void ring(float x,float z,float inner,float outer,float r,float g,float b) {
    for(int i=0;i<24;i++) {
        float a=(float)i*6.2831853f/24.0f, next=(float)(i+1)*6.2831853f/24.0f;
        float x0=x+cosf(a)*inner,z0=z+sinf(a)*inner;
        float x1=x+cosf(a)*outer,z1=z+sinf(a)*outer;
        float x2=x+cosf(next)*outer,z2=z+sinf(next)*outer;
        float x3=x+cosf(next)*inner,z3=z+sinf(next)*inner;
        projected(x0,.026f,z0,r,g,b); projected(x1,.026f,z1,r,g,b); projected(x2,.026f,z2,r,g,b);
        projected(x0,.026f,z0,r,g,b); projected(x2,.026f,z2,r,g,b); projected(x3,.026f,z3,r,g,b);
    }
}
static void robot_placeholder(Fighter *f, float r, float g, float b, float t) {
    float bob = f->stun > 0 ? -.13f : sinf(t * 4.0f) * .025f;
    float punch = f->source_animation ? f->pose_reach :
                  (f->attack > 0 ? (f->kind == 2 ? .78f : .56f) : 0);
    float kick = f->source_animation && f->kind == 2 ? punch : 0;
    float arm_reach = kick ? 0 : punch;
    float recoil = f->source_animation && f->stun > 0 ? .22f : 0;
    float armor = f->stun > 0 ? 1.35f : 1.0f;
    // Broad torso, narrow waist, separated armor plates and bright core.
    part(f,0,1.45f+bob,.02f,.76f,.43f,.52f,r*.40f,g*.48f,b*.53f);
    tapered_part(f,1.96f+bob,.80f,1.20f,.48f,.72f,.82f,r*armor,g*armor,b*armor);
    part(f,0,2.03f+bob,-.36f,.68f,.46f,.08f,r*.82f,g*.88f,b*.95f);
    part(f,0,2.10f+bob,-.43f,.30f,.27f,.06f,.97f,.84f,.45f);
    part(f,0,2.56f+bob,.01f,.28f,.24f,.30f,.15f,.22f,.33f);
    tapered_part(f,2.86f+bob,.65f,.48f,.54f,.41f,.48f,r*.8f,g*.85f,b*.9f);
    part(f,0,2.89f+bob,-.31f,.46f,.13f,.08f,.73f,.96f,1.0f);
    part(f,0,3.17f+bob,.03f,.32f,.15f,.42f,r*.57f,g*.63f,b*.69f);
    for(int side=-1;side<=1;side+=2) {
        float s=(float)side;
        float stride=f->pose_stride*s;
        float leg_kick=side == 1 ? kick : 0;
        part(f,s*.38f,.90f+bob,.04f-stride*.28f-leg_kick*.15f,.38f,.93f,.50f,r*.55f,g*.60f,b*.68f);
        part(f,s*.40f,.40f+bob,-.08f-stride*.55f-leg_kick*.60f,.43f,.61f,.53f,r*.81f,g*.85f,b*.88f);
        part(f,s*.41f,.13f+bob+leg_kick*.36f,-.22f-stride-leg_kick*1.08f,.56f,.22f,.77f,r*.48f,g*.53f,b*.61f);
        part(f,s*.73f,2.30f+bob,.01f,.58f,.32f,.74f,r*1.08f,g*1.08f,b*1.08f);
        float strike_arm=side == 1 ? arm_reach : 0;
        float guard_arm=f->guard ? .40f : 0;
        part(f,s*.73f,1.88f+bob,-.10f-strike_arm*.33f-guard_arm*.25f+recoil,.34f,.71f,.40f,r*.52f,g*.61f,b*.70f);
        part(f,s*.74f,1.44f+bob+guard_arm*.90f+strike_arm*.30f,
             -.22f-strike_arm*.90f-guard_arm*.60f+recoil,.41f,.48f,.53f,r*.88f,g*.94f,b);
        part(f,s*.74f,1.50f+bob+guard_arm*.90f+strike_arm*.30f,
             -.51f-strike_arm*1.12f-guard_arm*.60f+recoil,.30f,.20f,.08f,.88f,.93f,1.0f);
        part(f,s*.87f,2.57f+bob,.20f,.20f,.45f,.37f,r*.64f,g*.70f,b*.76f);
    }
    if(f->guard) {
        part(f,0,1.92f+bob,-.77f,1.26f,.64f,.07f,.19f,.55f,.75f);
        part(f,0,1.92f+bob,-.82f,1.12f,.53f,.035f,.60f,.93f,1.0f);
    }
    if(f->attack > 0) part(f,0,1.52f+bob+kick*.20f,-1.12f-punch*.65f,
                            .52f,.08f,.12f,1.0f,.85f,.48f);
}
typedef struct { float y,z; } RigPoint;
typedef struct { RigPoint shoulder,elbow,wrist,hip,knee,ankle; } RigSide;

// OMF3K_MESHY=1 swaps the blockouts for the decimated Meshy meshes: the Robot Mascot
// for Jaguar and the Rocket Jester for Shadow.
static bool use_meshy_model(void) {
    static int enabled=-1;
    if(enabled<0) {
        const char *v=getenv("OMF3K_MESHY");
        enabled=v && v[0] && v[0]!='0';
    }
    return enabled;
}

// max_stretch>0 limits how far the limb is lengthened or shortened to reach its target (the Meshy
// arms turn long and thin when an authored pose is far longer than the rest arm).
static RigPoint rig_map(RigPoint p,RigPoint from_a,RigPoint from_b,
                        RigPoint to_a,RigPoint to_b,float max_stretch) {
    float sy=from_b.y-from_a.y, sz=from_b.z-from_a.z;
    float ty=to_b.y-to_a.y, tz=to_b.z-to_a.z;
    float source_len=hypotf(sy,sz), target_len=hypotf(ty,tz);
    if(source_len<.0001f || target_len<.0001f) return p;
    float along=((p.y-from_a.y)*sy+(p.z-from_a.z)*sz)/source_len;
    float across=((p.y-from_a.y)*(-sz)+(p.z-from_a.z)*sy)/source_len;
    float stretch=target_len/source_len;
    if(max_stretch>0) stretch=clampf(stretch,1.0f/max_stretch,max_stretch);
    float scaled=along*stretch/target_len;
    return (RigPoint){to_a.y+scaled*ty+across*(-tz)/target_len,
                      to_a.z+scaled*tz+across*ty/target_len};
}

// Tilt a rig point about the torso pivot (height 1.38, depth 0) by atan(lean): positive leans the
// top toward the opponent (negative z). Rotating, not shearing, keeps the torso its length at the
// large tilts of dives and rolls; for small leans it matches the old shear.
static RigPoint lean_rotate(float y,float z,float lean) {
    float theta=atanf(lean), s=sinf(theta), c=cosf(theta), h=y-1.38f;
    return (RigPoint){1.38f+h*c+z*s, z*c-h*s};
}

// The authored arm poses come from flat sprites, so their segment lengths vary by about +-0.3 from pose to pose
// (the shoulder-to-elbow distance averages nearly twice the rig's upper arm). The Meshy arms cannot stretch like that:
// the forearm is placed at the elbow point, so a stretched upper arm leaves it detached. Keep the arm's bones
// near their rest lengths and take only each bone's direction from the pose, so the segments stay chained.
// origin, when not NULL, is where the sprite's own shoulder joint lies (authored in the pose editor): the upper arm's
// direction is then measured from it instead of from the rig's shoulder, which the pose was never drawn against.
static void limit_arm(RigSide *r,int har,const RigPoint *origin) {
    const float upper=har==0 ? .48f : .48f, fore=har==0 ? .63f : .66f;
    const RigPoint from=origin ? *origin : r->shoulder;
    float uy=r->elbow.y-from.y, uz=r->elbow.z-from.z;
    float ul=hypotf(uy,uz);
    if(ul>.0001f) {
        float len=clampf(ul,upper*.90f,upper*1.10f);
        r->elbow=(RigPoint){r->shoulder.y+uy/ul*len,r->shoulder.z+uz/ul*len};
    }
    float fy=r->wrist.y-r->elbow.y, fz=r->wrist.z-r->elbow.z;
    float fl=hypotf(fy,fz);
    if(fl>.0001f) {
        float len=clampf(fl,fore*.85f,fore*1.10f);
        r->wrist=(RigPoint){r->elbow.y+fy/fl*len,r->elbow.z+fz/fl*len};
    }
}

static void model_rig_sides(const Fighter *f,int har,float t,RigSide sides[2],
                            float *body_drop,float *body_lean,float *body_shift) {
    const PoseFrame *pose=pose_catalog_lookup(har,f->source_animation,f->source_sprite);
    // Keep the authored long-range silhouette, but fold the striking limb
    // toward a nearby opponent so it does not pass through their torso.
    float contact_distance=0;
    bool contact_pose=false;
    if(source_replay_mode && (f==&player || f==&rival)) {
        const Fighter *opponent=f==&player ? &rival : &player;
        float source_dx=opponent->x-f->x;
        float presentation_dx=(opponent->x+opponent->presentation_x)-
                              (f->x+f->presentation_x);
        contact_pose=source_dx*facing_dir(f)>=0;
        contact_distance=fabsf(presentation_dx);
    }
    float crouch=clampf((1.0f-(f->pose_height>0 ? f->pose_height : 1.0f))/.32f,0,1);
    float bob=f->stun>0 ? -.12f : sinf(t*4.0f)*.018f;
    float reach=f->source_animation ? f->pose_reach :
                (f->attack>0 ? (f->kind==2 ? .78f : .56f) : 0);
    float kick=f->source_animation ? (f->kind==2 ? reach : 0) :
               (f->attack>0 && f->kind==2 ? reach : 0);
    float arm_reach=kick ? 0 : reach;
    float recoil=f->source_animation && f->stun>0 ? .18f : 0;
    *body_drop=bob-crouch*.52f;
    // An authored body height replaces the state-derived crouch drop. Arm joint heights are
    // relative to it, leg joint heights are absolute.
    if(pose && (pose->flags&POSE_DROP)) *body_drop=bob+pose->body_y;
    *body_shift=pose && (pose->flags&POSE_BODY) ? pose->body_z : 0;
    *body_lean=har==0 && f->source_animation==30 && pose ?
                    .05f+.43f*pose->reach : 0;
    float shadow_punch_lunge=0;
    if(har==1 && f->source_animation==23 && pose) {
        // Shadow Punch starts with an extended arm; animate the body and legs to carry its source-keyed lunge.
        static const float lunge_by_sprite[]={.58f,.92f,.74f,.48f,.24f,0.0f};
        if(f->source_sprite>=0 && f->source_sprite<6)
            shadow_punch_lunge=lunge_by_sprite[f->source_sprite];
        *body_drop-=.16f*shadow_punch_lunge;
        *body_lean=.30f*shadow_punch_lunge;
    }
    // An authored lean (from the pose editor's two-point axis) overrides the hard-coded ones above.
    if(pose && (pose->flags&POSE_LEAN)) *body_lean=pose->lean;
    for(int i=0;i<2;i++) {
        int side=i==0 ? -1 : 1;
        float stride=f->pose_stride*(float)side;
        float leg_kick=side==1 ? kick : 0;
        float arm_forward=side==1 ? arm_reach : 0;
        float guard=f->guard ? .37f : 0;
        RigSide *r=&sides[i];
        r->hip=(RigPoint){1.38f+*body_drop,.02f+crouch*.10f+*body_shift};
        r->knee=(RigPoint){.57f+bob-crouch*.04f+leg_kick*.44f,
                           -.02f-crouch*.38f-stride*.32f-leg_kick*.55f};
        r->ankle=(RigPoint){.18f+bob+leg_kick*.92f,
                            -.03f-stride*.82f-leg_kick*1.28f};
        if(pose && (pose->flags&POSE_LEG) && side==pose->side) {
            r->knee=(RigPoint){pose->knee_y+bob,pose->knee_z};
            r->ankle=(RigPoint){pose->ankle_y+bob,pose->ankle_z};
            if(contact_pose && source_standing_kick(har,f->source_animation) &&
               pose->reach>.5f) {
                float ankle_z=-clampf(contact_distance-.50f,.28f,-pose->ankle_z);
                float fold=ankle_z-pose->ankle_z;
                r->ankle.z=ankle_z;
                r->knee.z+=fold*.35f;
            }
        } else if(pose && (pose->flags&POSE_LEG2) && side!=pose->side) {
            // The other leg, fitted from the same source sprite: planted, trailing, or bracing.
            r->knee=(RigPoint){pose->knee2_y+bob,pose->knee2_z};
            r->ankle=(RigPoint){pose->ankle2_y+bob,pose->ankle2_z};
        } else if(f->source_state==6 || f->y>.25f) {
            // Both robots tuck the near knee and draw the far foot underneath.
            r->knee.y+=side==1 ? .38f : .19f;
            r->knee.z+=side==1 ? -.27f : .24f;
            r->ankle.y+=side==1 ? .48f : .31f;
            r->ankle.z+=side==1 ? -.12f : .20f;
        }
        if(har==0 && f->source_animation==30 && pose) {
            float lunge=pose->reach;
            r->knee=(RigPoint){(side==1 ? .75f+.30f*lunge : .57f)+bob,
                                side==1 ? -.15f-.55f*lunge : .12f+.48f*lunge};
            r->ankle=(RigPoint){.18f+bob,
                                 side==1 ? -.15f-.35f*lunge : .15f+.85f*lunge};
        }
        if(shadow_punch_lunge>0) {
            float spread=.30f+.90f*shadow_punch_lunge;
            float leg_y=.68f-.10f*shadow_punch_lunge;
            r->knee=(RigPoint){leg_y+bob,side==1 ? -.38f-spread*.42f : .24f+spread*.42f};
            r->ankle=(RigPoint){.16f+bob,side==1 ? -.62f-spread : .62f+spread};
        }
        // The shoulder follows the torso lean (pivot 1.38, as in model_transform).
        // The blockout's arms hang from a shoulder 0.13 above the rest joint (the top of its shoulder armor). The Meshy
        // arms are fitted to the joint itself, so a pivot up there would stretch every upper arm; use the joint.
        float shoulder_pivot=use_meshy_model() ? (har==0 ? 2.24f : 2.25f) : 2.38f;
        RigPoint shoulder=lean_rotate(shoulder_pivot,0,*body_lean);
        RigPoint pose_shoulder={0,0};
        bool have_pose_shoulder=false;
        r->shoulder=(RigPoint){shoulder.y+*body_drop,shoulder.z+*body_shift};
        r->elbow=(RigPoint){1.77f+*body_drop+guard*.27f+arm_forward*.20f,
                            -.10f-arm_forward*.37f-guard*.28f+recoil};
        r->wrist=(RigPoint){1.38f+*body_drop+guard*1.55f+arm_forward*.55f,
                            -.24f-arm_forward*1.04f-guard*.60f+recoil};
        if(pose && (pose->flags&POSE_ARM) && side==pose->side) {
            r->elbow=(RigPoint){pose->elbow_y+*body_drop,pose->elbow_z+recoil};
            r->wrist=(RigPoint){pose->wrist_y+*body_drop,pose->wrist_z+recoil};
            if(pose->flags&POSE_SHOULDER) {
                pose_shoulder=(RigPoint){pose->shoulder_y+*body_drop,pose->shoulder_z+recoil};
                have_pose_shoulder=true;
            }
            if(contact_pose && (source_standing_punch(har,f->source_animation) ||
                                (har==0 && f->source_animation==30)) &&
               pose->reach>.5f) {
                float wrist_z=-clampf(contact_distance-.20f,.38f,-pose->wrist_z);
                float fold=wrist_z-pose->wrist_z;
                r->wrist.z=wrist_z+recoil;
                r->elbow.z+=fold*.45f;
            }
        } else if(pose && (pose->flags&POSE_ARM2) && side!=pose->side) {
            // The other arm, fitted from the same source sprite.
            r->elbow=(RigPoint){pose->elbow2_y+*body_drop,pose->elbow2_z+recoil};
            r->wrist=(RigPoint){pose->wrist2_y+*body_drop,pose->wrist2_z+recoil};
            if(pose->flags&POSE_SHOULDER2) {
                pose_shoulder=(RigPoint){pose->shoulder2_y+*body_drop,pose->shoulder2_z+recoil};
                have_pose_shoulder=true;
            }
        } else if(f->stun>0 && !f->guard) {
            r->elbow.y+=side==1 ? .35f : .20f;
            r->elbow.z+=.18f;
            r->wrist.y+=side==1 ? .70f : .28f;
            r->wrist.z+=side==1 ? .31f : .42f;
        }
        if(use_meshy_model()) limit_arm(r,har,have_pose_shoulder ? &pose_shoulder : NULL);
    }
}

static void model_transform(const Fighter *f,int har,const ModelPart *part,
                            const RigSide sides[2],float body_drop,float body_lean,float body_shift,
                            ModelPosition source,float out[3]) {
    RigPoint p={source.y,source.z};
    const RigSide *r=&sides[part->side==1 ? 1 : 0];
    if(part->group==0 || part->group==1 || part->group==2) {
        RigPoint tilted=lean_rotate(source.y,source.z,body_lean);
        p.y=tilted.y+body_drop;
        p.z=tilted.z+body_shift;
    } else {
        float shoulder_y=har==0 ? 2.24f : 2.25f;
        float elbow_y=har==0 ? 1.76f : 1.77f;
        float wrist_y=har==0 ? 1.13f : 1.11f;
        float hip_y=har==0 ? 1.30f : 1.27f;
        float knee_y=har==0 ? .75f : .76f;
        float ankle_y=har==0 ? .23f : .24f;
        float arm_cap=use_meshy_model() ? 1.08f : 0;   // near-constant arm length; poses may not reach their wrist
        switch(part->group) {
        case 3: p=rig_map(p,(RigPoint){shoulder_y,0},(RigPoint){elbow_y,-.02f},
                          r->shoulder,r->elbow,arm_cap); break;
        case 4: case 5:
            p=rig_map(p,(RigPoint){elbow_y,-.02f},(RigPoint){wrist_y,-.08f},
                      r->elbow,r->wrist,arm_cap); break;
        case 6: p=rig_map(p,(RigPoint){hip_y,0},(RigPoint){knee_y,har==0 ? -.01f : 0},
                          r->hip,r->knee,0); break;
        case 7: p=rig_map(p,(RigPoint){knee_y,har==0 ? -.01f : 0},
                          (RigPoint){ankle_y,-.02f},r->knee,r->ankle,0); break;
        case 8: p.y+=r->ankle.y-ankle_y; p.z+=r->ankle.z+.02f; break;
        }
    }
    float co=cosf(f->facing), si=sinf(f->facing);
    out[0]=f->x+f->presentation_x+source.x*co+p.z*si;
    out[1]=f->y+p.y;
    out[2]=-source.x*si+p.z*co+f->pose_depth;
}

static void robot_loaded_model(Fighter *f,int har,float t,bool projection) {
    RigSide sides[2];
    float body_drop,body_lean,body_shift;
    model_rig_sides(f,har,t,sides,&body_drop,&body_lean,&body_shift);
    bool meshy=use_meshy_model();
    const ModelPart *parts=model_parts;
    const ModelPosition *positions=model_positions;
    const uint16_t *indices=model_indices;
    const ModelBlend *blend=NULL;
    size_t part_count=sizeof(model_parts)/sizeof(model_parts[0]);
    if(meshy && har==0) {
        parts=meshy_parts; positions=meshy_positions; indices=meshy_indices; blend=meshy_blend;
        part_count=sizeof(meshy_parts)/sizeof(meshy_parts[0]);
    } else if(meshy && har==1) {
        parts=jester_parts; positions=jester_positions; indices=jester_indices; blend=jester_blend;
        part_count=sizeof(jester_parts)/sizeof(jester_parts[0]);
    }
    for(size_t i=0;i<part_count;i++) {
        const ModelPart *part=&parts[i];
        if(part->har!=har) continue;
        for(unsigned j=part->first;j<part->first+part->count;j+=3) {
            float p[3][3];
            for(int k=0;k<3;k++) {
                unsigned vi=indices[j+k];
                model_transform(f,har,part,sides,body_drop,body_lean,body_shift,positions[vi],p[k]);
                // Vertices near a joint also follow the neighbouring group, which closes the seam.
                if(blend && blend[vi].weight) {
                    ModelPart other=*part;
                    other.group=blend[vi].group;
                    other.side=blend[vi].side;
                    float q[3],w=blend[vi].weight/255.0f;
                    model_transform(f,har,&other,sides,body_drop,body_lean,body_shift,positions[vi],q);
                    for(int a=0;a<3;a++) p[k][a]+=(q[a]-p[k][a])*w;
                }
            }
            float ux=p[1][0]-p[0][0], uy=p[1][1]-p[0][1], uz=p[1][2]-p[0][2];
            float vx=p[2][0]-p[0][0], vy=p[2][1]-p[0][1], vz=p[2][2]-p[0][2];
            float nx=uy*vz-uz*vy, ny=uz*vx-ux*vz, nz=ux*vy-uy*vx;
            float length=sqrtf(nx*nx+ny*ny+nz*nz);
            if(length<.00001f) continue;
            // Broad overhead light, with a cool edge that separates the armor plates.
            float top=fmaxf(0,ny/length);
            float side=fabsf(nz/length);
            float edge=fabsf(nx/length);
            float shade=clampf(.63f+.30f*top+.20f*side+.13f*edge,.60f,1.14f);
            float red=part->r/255.0f, green=part->g/255.0f, blue=part->b/255.0f;
            if(projection) {
                float bright=fmaxf(red,fmaxf(green,blue));
                if(green>red*1.5f) { red=.54f; green=.94f; blue=1.0f; }
                else if(bright<.25f) { red=.15f; green=.10f; blue=.34f; }
                else { red=.48f; green=.36f; blue=.86f; }
                shade=clampf(shade+.12f,.72f,1.25f);
            }
            for(int k=0;k<3;k++)
                projected(p[k][0],p[k][1],p[k][2],
                          red*shade,green*shade,blue*shade);
        }
    }
}

static void robot(Fighter *f, int har, float t) {
    if(har==0 || har==1) {
        robot_loaded_model(f,har,t,false);
    }
    else robot_placeholder(f,.56f,.61f,.68f,t);
}
// Projectile animations that show a full Shadow figure: the shadows of P41 (25, 26), the K41 slide (22, 53), the
// P252 grab (37, 52 rising; once it connects, 39 drops onto the opponent, then 40, 50 and 51 hold and release them)
// and the P632 air move (34, 35), and
// their hit frames (27, 28, 29, 38, 49).
static bool shadow_projection_animation(int animation) {
    return animation==25 || animation==26 || animation==22 || animation==53 || animation==34 || animation==35 ||
           animation==37 || animation==52 || animation==39 || animation==40 || animation==50 || animation==51 ||
           animation==27 || animation==28 || animation==29 || animation==38 || animation==49;
}
static const ProjectionPose *projection_pose_for(int animation,int sprite) {
    for(size_t k=0;k<sizeof(projection_poses)/sizeof(projection_poses[0]);k++)
        if(projection_poses[k].anim==animation && projection_poses[k].sprite==sprite) return &projection_poses[k];
    return NULL;
}
static void source_projectiles(void) {
    if(!source_replay_mode || !source_replay.count) return;
    const SourceFrame *frame=&source_replay.frames[source_replay_index];
    for(int i=0;i<frame->projectile_count;i++) {
        const SourceProjectile *p=&frame->projectile[i];
        if(p->sprite<0) continue;
        float x=(p->x-160.0f)*(7.6f/280.0f);
        float y=(190.0f-p->y)*(12.0f/280.0f);
        if(p->owner<0 || p->owner>1) continue;
        int har=frame->fighter[p->owner].har;
        if(har==0 && (p->animation==38 || p->animation==37)) {
            // Concussion shot (38) in flight and its impact burst (37). The burst grows with the source impact
            // sprite 0-5, so it reads at fight-camera scale; position and timing stay as OpenOMF reports them.
            float direction=p->facing>=0 ? 1.0f : -1.0f;
            float yaw=p->facing>=0 ? -1.5707963f : 1.5707963f;
            if(p->animation==38) {
                float size=.62f;
                for(int trail=5;trail>=1;trail--)
                    box(x-direction*(size*.45f+trail*.22f),y,0,
                        size*(.38f-trail*.05f),size*(.46f-trail*.06f),size*(.90f-trail*.12f),yaw,
                        .08f,.30f+trail*.07f,.44f+trail*.07f);
                box(x,y,0,size*.20f,size*1.00f,size*1.70f,yaw,.05f,.26f,.50f);              // outer glow: a thin sheet the core sticks out of
                // Each brighter layer is shorter and thinner but deeper toward the camera, so the layers stack visibly.
                box(x,y,0,size*.30f,size*.72f,size*1.48f,yaw,.08f,.42f,.68f);
                box(x+direction*size*.06f,y,0,size*.40f,size*.48f,size*1.30f,yaw,.20f,.74f,.96f);
                box(x+direction*size*.12f,y,0,size*.50f,size*.25f,size*1.08f,yaw,.85f,1.0f,1.0f);
            } else {
                int frame_index=p->sprite>5 ? 5 : p->sprite;
                float size=.55f+.14f*(float)frame_index;
                box(x,y,0,size*.20f,size*1.00f,size*1.30f,yaw,.05f,.26f,.50f);
                box(x,y,0,size*.30f,size*.72f,size*1.10f,yaw,.08f,.42f,.68f);
                box(x,y,0,size*.40f,size*.48f,size*.90f,yaw,.20f,.74f,.96f);
                box(x,y,0,size*.50f,size*.25f,size*.70f,yaw,.85f,1.0f,1.0f);
                for(int k=0;k<8;k++) {
                    float a=.785398f*(float)k;
                    box(x+cosf(a)*size*.85f,y+sinf(a)*size*.85f,0,size*.12f,size*.12f,size*.32f,yaw,.55f,.92f,1.0f);
                }
            }
        } else if(har==1 && (p->animation==54 || p->animation==60)) {
            // Shadow Punch's ice blade slides along the floor (54) and bursts on contact (60); larger and
            // trailing so it reads at fight-camera scale. The burst grows with the source sprite.
            float direction=p->facing>=0 ? 1.0f : -1.0f;
            float yaw=p->facing>=0 ? -1.5707963f : 1.5707963f;
            ring(x,0,.48f,.55f,.34f,.24f,.74f);
            if(p->animation==54) {
                // The blade spawns on the floor 60 source units ahead of Shadow and moves 20 per tick, so its
                // distance from Shadow gives a ramp-in over its first two ticks with no per-projectile state.
                float away=fabsf(p->x-frame->fighter[p->owner].x);
                float grow=clampf(.45f+(away-60.0f)/80.0f,.45f,1.0f);
                for(int k=0;k<6;k++)
                    box(x-direction*.26f*grow*(float)k,(.14f+.04f*(float)k)*grow,0,(.48f-.06f*(float)k)*grow,
                        (.26f+.05f*(float)k)*grow,(.72f-.09f*(float)k)*grow,yaw,.40f,.86f-.04f*(float)k,.98f);
            } else {
                int frame_index=p->sprite>5 ? 5 : (p->sprite<0 ? 0 : p->sprite);
                float grow=1.0f+.22f*(float)frame_index;
                for(int k=0;k<7;k++)
                    box(x+direction*(.18f*(float)(k-3))*grow,(.30f+.20f*(float)(k%3))*grow,0,.20f*grow,
                        (.56f+.22f*(float)(k%2))*grow,.32f*grow,yaw,.60f,.94f,1.0f);
            }
        } else if(har==1 && shadow_projection_animation(p->animation)) {
            // Shadow's projections are full Shadow figures, drawn with the rig. A sprite authored in the pose editor
            // uses its own pose and stands on the floor at the height its projectile spawns at (P41 shadow 111,
            // slide 190, grab 168, air move 153), rising or falling with it. Otherwise it borrows the pose of the
            // authored sprite that best matches its silhouette (projection_poses.h, from match_projection_poses.py),
            // placed so the two silhouettes coincide; the hit and return frames match Shadow's damage frames exactly.
            const float xs=7.6f/280.0f, ys=12.0f/280.0f;
            float dir=p->facing>=0 ? 1.0f : -1.0f;
            // The scripts of 39, 40, 50 and 51 carry the "r" tag (flip the sprite horizontally) on every frame: the
            // drawn figure is mirrored against the projectile's own direction.
            if(p->animation==39 || p->animation==40 || p->animation==50 || p->animation==51) dir=-dir;
            int pose_animation=p->animation, pose_sprite=p->sprite;
            float spawn_y=(p->animation==25 || p->animation==26) ? 111.0f :
                          (p->animation==37 || p->animation==52) ? 168.0f :
                          (p->animation==34 || p->animation==35) ? 153.0f : 190.0f;
            float ghost_y=(spawn_y-p->y)*ys;
            if(!pose_catalog_lookup(1,p->animation,p->sprite)) {
                const ProjectionPose *borrow=projection_pose_for(p->animation,p->sprite);
                if(borrow) {
                    pose_animation=borrow->from_anim; pose_sprite=borrow->from_sprite;
                    x+=(float)borrow->dx*dir*xs;
                    ghost_y=(190.0f-(p->y+(float)borrow->dy))*ys;
                }
            }
            Fighter ghost={.x=x,.y=ghost_y,.facing=dir>=0 ? -1.5707963f : 1.5707963f,
                           .pose_height=1,.pose_depth=.55f,
                           .source_animation=pose_animation,.source_sprite=pose_sprite};
            const PoseFrame *pose=pose_catalog_lookup(1,pose_animation,pose_sprite);
            if(pose && (pose->flags&POSE_REACH)) ghost.pose_reach=pose->reach;
            robot_loaded_model(&ghost,1,source_visual_time,true);
        }
    }
}
static void stadium_background(void) {
    static const float crowd_colors[][3] = {
        {.11f,.21f,.31f}, {.20f,.27f,.39f}, {.32f,.18f,.24f},
        {.27f,.34f,.39f}, {.40f,.29f,.18f}, {.13f,.31f,.29f}
    };
    const int crowd_color_count=(int)(sizeof(crowd_colors)/sizeof(crowd_colors[0]));

    // Roof and continuous back wall enclose the arena like a large indoor bowl.
    box(0,2.75f,-8.05f,19.0f,5.5f,.28f,0,.025f,.045f,.075f);
    box(0,4.23f,-7.55f,18.8f,.20f,.62f,0,.12f,.18f,.28f);
    box(0,3.98f,-7.18f,17.8f,.08f,.16f,0,.20f,.54f,.63f);
    box(0,3.80f,-6.98f,16.6f,.045f,.08f,0,.42f,.68f,.72f);
    for(int i=-4;i<=4;i++) {
        float x=(float)i*2.0f;
        box(x,3.33f,-7.45f,.10f,1.22f,.16f,0,.12f,.24f,.34f);
        box(x,3.93f,-7.10f,.45f,.10f,.48f,0,.19f,.28f,.36f);
    }

    // Stepped seating tiers and abstract spectator silhouettes use only new geometry.
    for(int row=0;row<4;row++) {
        float y=1.12f+(float)row*.43f;
        float z=-6.95f-(float)row*.19f;
        box(0,y-.15f,z,17.6f,.24f,.68f,0,.075f,.11f,.18f);
        box(0,y-.005f,z+.63f,17.5f,.055f,.08f,0,.17f,.32f,.39f);
        for(int column=0;column<36;column++) {
            float x=-8.25f+(float)column*.47f+(row%2 ? .23f : 0.0f);
            int color=(column*7+row*11+(column/3))%crowd_color_count;
            const float *c=crowd_colors[color];
            box(x,y+.055f,z+.45f,.25f,.30f,.14f,0,c[0],c[1],c[2]);
            box(x,y+.305f,z+.45f,.16f,.16f,.14f,0,
                clampf(c[0]+.12f,.10f,.52f),clampf(c[1]+.12f,.12f,.55f),clampf(c[2]+.12f,.14f,.60f));
        }
    }

    // A central arena board and high perimeter lights identify the venue.
    box(0,3.38f,-6.48f,3.35f,.76f,.20f,0,.025f,.055f,.095f);
    box(0,3.38f,-6.35f,3.05f,.52f,.035f,0,.055f,.12f,.18f);
    box(-1.10f,3.39f,-6.30f,.54f,.17f,.025f,0,.18f,.72f,.86f);
    box(-.36f,3.39f,-6.30f,.54f,.17f,.025f,0,.18f,.72f,.86f);
    box(.38f,3.39f,-6.30f,.54f,.17f,.025f,0,.92f,.30f,.44f);
    box(1.12f,3.39f,-6.30f,.54f,.17f,.025f,0,.92f,.30f,.44f);
    box(0,2.86f,-6.18f,8.4f,.045f,.08f,0,.26f,.60f,.64f);
}
static void quad(float x,float y,float w,float h,float r,float g,float b) {
    float x2=x+w,y2=y+h;
    vertex(x,y,-.99f,r,g,b); vertex(x2,y,-.99f,r,g,b); vertex(x2,y2,-.99f,r,g,b);
    vertex(x,y,-.99f,r,g,b); vertex(x2,y2,-.99f,r,g,b); vertex(x,y2,-.99f,r,g,b);
}
static const unsigned char *glyph(char ch) {
    if(ch>='a' && ch<='z') ch=(char)(ch-'a'+'A');
    for(size_t i=0;i<sizeof(font)/sizeof(font[0]);i++) if(font[i].ch==ch) return font[i].rows;
    return font[sizeof(font)/sizeof(font[0])-1].rows;
}
static void label(float x,float y,float size,const char *s,float r,float g,float b) {
    for(;*s;s++,x+=size*6.0f) {
        const unsigned char *rows=glyph(*s);
        for(int row=0;row<7;row++) for(int col=0;col<5;col++)
            if(rows[row] & (1 << (4-col))) quad(x+col*size,y-row*size,size*.85f,size*.85f,r,g,b);
    }
}

static void selection_hud(void) {
    quad(-1,-1,2,2,.015f,.025f,.065f);
    quad(-.78f,.62f,1.56f,.20f,.04f,.10f,.18f);
    label(-.70f,.71f,.018f,"OMF2115 / CHOOSE YOUR FIGHTER",.65f,.92f,1);
    label(-.72f,.43f,.012f,"UP DOWN ROBOT",.55f,.70f,.84f);
    label(-.72f,.34f,.012f,"LEFT RIGHT PILOT",.55f,.70f,.84f);
    label(-.72f,.18f,.011f,"ROBOT",.48f,.60f,.72f);
    label(-.72f,.05f,.020f,selection_har_names[selection_har],.30f,.90f,1);
    label(.12f,.18f,.011f,"PILOT",.48f,.60f,.72f);
    label(.12f,.05f,.020f,selection_pilot_names[selection_pilot],1,.72f,.79f);
    quad(-.78f,-.20f,1.56f,.035f,.12f,.18f,.25f);
    quad(-.78f,-.20f,.78f,.035f,.16f,.83f,.94f);
    label(-.72f,-.42f,.013f,"ENTER START MATCH",.70f,.90f,.96f);
    label(-.72f,-.54f,.011f,"ESC CANCEL",.55f,.70f,.84f);
}
// Word-wraps text into lines of at most width characters; returns the line count.
static int story_wrap(const char *text,int width,char lines[][80],int max_lines) {
    int n=0;
    const char *p=text;
    while(*p && n<max_lines) {
        while(*p==' ') p++;
        int len=0,last_space=-1;
        while(p[len] && len<width) { if(p[len]==' ') last_space=len; len++; }
        if(p[len] && p[len]!=' ' && last_space>0) len=last_space;
        memcpy(lines[n],p,(size_t)len);
        lines[n][len]=0;
        while(len>0 && lines[n][len-1]==' ') lines[n][--len]=0;
        n++;
        p+=len;
    }
    return n;
}
static void story_speaker_color(const char *speaker,float *r,float *g,float *b) {
    float c[3]={.95f,.95f,.95f};
    if(!*speaker) { c[0]=.70f; c[1]=.78f; c[2]=.85f; }
    else if(!strcmp(speaker,"Crystal")) { c[0]=.55f; c[1]=.90f; c[2]=1; }
    else if(!strcmp(speaker,"Christian")) { c[0]=1; c[1]=.70f; c[2]=.62f; }
    else if(!strcmp(speaker,"YOU")) { c[0]=.85f; c[1]=1; c[2]=.70f; }
    *r=c[0]; *g=c[1]; *b=c[2];
}
// Loads project/build/portraits/<Pilot>.bmp, exported from the original game's data by
// project/tools/export_pilot_portraits.py. Local only: the art is never committed. Missing files fall back to a card.
static void story_load_bmp(StoryPortrait *portrait,const char *path) {
    free(portrait->rgb);
    portrait->rgb=NULL; portrait->w=portrait->h=0;
    SDL_Surface *loaded=SDL_LoadBMP(path);
    if(!loaded) return;
    SDL_Surface *rgb=SDL_ConvertSurfaceFormat(loaded,SDL_PIXELFORMAT_RGB24,0);
    SDL_FreeSurface(loaded);
    if(!rgb) return;
    portrait->rgb=malloc((size_t)rgb->w*(size_t)rgb->h*3);
    if(portrait->rgb) {
        for(int y=0;y<rgb->h;y++)
            memcpy(portrait->rgb+(size_t)y*(size_t)rgb->w*3,(unsigned char*)rgb->pixels+(size_t)y*(size_t)rgb->pitch,(size_t)rgb->w*3);
        portrait->w=rgb->w; portrait->h=rgb->h;
    }
    SDL_FreeSurface(rgb);
}
static void story_load_portrait(StoryPortrait *portrait,const char *pilot) {
    char path[256];
    snprintf(path,sizeof(path),"project/build/portraits/%s.bmp",pilot);
    story_load_bmp(portrait,path);
}

// ---- sounds: original effects exported by export_story_assets.py into project/build/sounds ----
enum { SND_MOVE, SND_SELECT, SND_COUNT };
typedef struct { Uint8 *data; Uint32 len; } StorySound;
static StorySound story_sounds[SND_COUNT];
static SDL_AudioDeviceID story_audio;
static bool story_muted;
static void story_notify(const char *text);
// ---- music: the original tracker modules, played from OMF2097/ with libxmp on a second audio device ----
static SDL_AudioDeviceID story_music_dev;
static xmp_context story_music_ctx;
static char story_music_name[STORY_NAME];
static void story_music_callback(void *userdata,Uint8 *stream,int len) {
    (void)userdata;
    // Silent while muted, and while a match runs (OpenOMF plays the arena's music there).
    if(!story_music_ctx || story_muted || story_match_state==1 || xmp_play_buffer(story_music_ctx,stream,len,0)<0)
        memset(stream,0,(size_t)len);
}
static void story_music_set(const char *name) {
    snprintf(story_music_name,sizeof(story_music_name),"%s",name);
    SDL_LockAudioDevice(story_music_dev);
    if(story_music_ctx) {
        xmp_end_player(story_music_ctx);
        xmp_release_module(story_music_ctx);
        xmp_free_context(story_music_ctx);
        story_music_ctx=NULL;
    }
    if(name[0]) {
        char path[96];
        size_t n=(size_t)snprintf(path,sizeof(path),"OMF2097/");
        for(const char *c=name;*c && n+5<sizeof(path);c++) path[n++]=(char)((*c>='a' && *c<='z') ? *c-32 : *c);
        snprintf(path+n,sizeof(path)-n,".PSM");
        xmp_context ctx=xmp_create_context();
        bool loaded=false;
        if(ctx && xmp_load_module(ctx,path)==0) {
            loaded=true;
            if(xmp_start_player(ctx,44100,0)==0) {
                xmp_set_player(ctx,XMP_PLAYER_VOLUME,70);
                xmp_set_player(ctx,XMP_PLAYER_INTERP,XMP_INTERP_LINEAR);
                story_music_ctx=ctx;
            }
        }
        if(!story_music_ctx) {
            fprintf(stderr,"Could not play the music %s\n",path);
            if(ctx) { if(loaded) xmp_release_module(ctx); xmp_free_context(ctx); }
        }
    }
    SDL_UnlockAudioDevice(story_music_dev);
}
// Follows the story: plays the track the script asked for, and nothing when the script has none.
static void story_music_sync(const char *want) {
    if(!story_music_dev || !strcmp(want,story_music_name)) return;
    story_music_set(want);
}
static void story_audio_init(void) {
    static const char *files[SND_COUNT]={"move","select"};
    if(SDL_InitSubSystem(SDL_INIT_AUDIO)!=0) return;
    SDL_AudioSpec want,have;
    SDL_zero(want);
    want.freq=22050; want.format=AUDIO_S16SYS; want.channels=1; want.samples=1024;
    story_audio=SDL_OpenAudioDevice(NULL,0,&want,&have,0);
    if(!story_audio) return;
    int loaded=0;
    for(int i=0;i<SND_COUNT;i++) {
        char path[128];
        snprintf(path,sizeof(path),"project/build/sounds/%s.wav",files[i]);
        SDL_AudioSpec spec;
        Uint8 *buf;
        Uint32 len;
        if(!SDL_LoadWAV(path,&spec,&buf,&len)) continue;
        SDL_AudioCVT cvt;
        if(SDL_BuildAudioCVT(&cvt,spec.format,spec.channels,spec.freq,have.format,have.channels,have.freq)>=0) {
            cvt.len=(int)len;
            cvt.buf=SDL_malloc((size_t)len*(size_t)cvt.len_mult);
            if(cvt.buf) {
                memcpy(cvt.buf,buf,len);
                SDL_ConvertAudio(&cvt);
                story_sounds[i].data=cvt.buf;
                story_sounds[i].len=(Uint32)cvt.len_cvt;
                loaded++;
            }
        }
        SDL_FreeWAV(buf);
    }
    SDL_AudioSpec music_want,music_have;
    SDL_zero(music_want);
    music_want.freq=44100; music_want.format=AUDIO_S16SYS; music_want.channels=2; music_want.samples=2048;
    music_want.callback=story_music_callback;
    story_music_dev=SDL_OpenAudioDevice(NULL,0,&music_want,&music_have,0);
    if(story_music_dev) SDL_PauseAudioDevice(story_music_dev,0);
    printf("Story sounds: %d of %d loaded; music %s\n",loaded,SND_COUNT,story_music_dev ? "ready" : "unavailable");
    fflush(stdout);
    SDL_PauseAudioDevice(story_audio,0);
}
static void story_sound(int which) {
    if(!story_audio || story_muted || !story_sounds[which].data) return;
    SDL_ClearQueuedAudio(story_audio);
    SDL_QueueAudio(story_audio,story_sounds[which].data,story_sounds[which].len);
}

// ---- backdrops: the original arena image when one is exported for the scene's bg, else a generated scene ----
static StoryPortrait story_backdrop;
static char story_backdrop_name[STORY_NAME];
// Illustrated sequence: a 320x124 frame from project/build/art, animated by the script's art effect.
static StoryPortrait story_art_image;
static char story_art_name[STORY_NAME];
static char story_art_effect[STORY_NAME];
static Uint64 story_art_started;
static bool story_capturing;      // a --shot run: show every effect as it looks a few seconds in
static int story_shot_typed=-1;   // --typed N with --shot: freeze the typewriter after N characters
static float story_draw_bright=1.0f;            // portraits are drawn at this brightness (1 is normal)
static float story_typed;                       // characters of the current say line revealed so far
static unsigned story_typed_line=0xFFFFFFFFu;   // log_total of the line being typed
static Uint64 story_type_last;                  // time of the previous typing update
static bool story_script_running;               // inside --script: nothing waits for the typewriter
static unsigned story_effect_seen;              // last flash or banner beat played
static Uint64 story_effect_start;
static char story_effect_kind[16];
static char story_effect_text[STORY_NAME];
static StoryPortrait story_speakers[10];        // portraits of the ten pilots, loaded when first needed
static bool story_speaker_tried[10];
// The backdrop fills x -1..1 and y -.24..1, under the header band and above the dialogue box.
static float story_u(float u) { return -1.0f+2.0f*u; }
static float story_v(float v) { return -.24f+1.24f*v; }
static void story_box(float u0,float v0,float u1,float v1,float r,float g,float b) {
    quad(story_u(u0),story_v(v0),story_u(u1)-story_u(u0),story_v(v1)-story_v(v0),r,g,b);
}
static void story_gradient(float v0,float v1,int bands,const float *c0,const float *c1) {
    for(int i=0;i<bands;i++) {
        float t=((float)i+.5f)/(float)bands;
        story_box(0,v0+(v1-v0)*(float)i/(float)bands,1,v0+(v1-v0)*(float)(i+1)/(float)bands+.002f,
                  c0[0]+(c1[0]-c0[0])*t,c0[1]+(c1[1]-c0[1])*t,c0[2]+(c1[2]-c0[2])*t);
    }
}
static void story_draw_green_room(void) {
    static const float wall_top[3]={.03f,.09f,.08f}, wall_low[3]={.07f,.21f,.17f};
    story_gradient(.20f,1.0f,12,wall_top,wall_low);
    story_box(0,0,1,.20f,.05f,.05f,.07f);                               // floor
    story_box(0,.20f,1,.215f,.02f,.05f,.04f);                           // baseboard
    story_box(.14f,.36f,.86f,.80f,.45f,.35f,.18f);                      // mirror frame
    story_box(.155f,.38f,.845f,.78f,.13f,.20f,.24f);                    // glass
    story_box(.17f,.62f,.52f,.65f,.22f,.32f,.37f);                      // glass glint
    for(int i=0;i<14;i++) { float u=.16f+.05f*(float)i; story_box(u,.805f,u+.025f,.840f,1.0f,.86f,.50f); }  // bulbs
    story_box(.10f,.20f,.50f,.33f,.30f,.09f,.12f);                      // couch seat
    story_box(.10f,.33f,.50f,.46f,.36f,.11f,.15f);                      // couch back
    story_box(.08f,.20f,.12f,.38f,.24f,.07f,.10f);                      // arms
    story_box(.48f,.20f,.52f,.38f,.24f,.07f,.10f);
    story_box(.60f,.20f,.90f,.30f,.35f,.30f,.22f);                      // make-up table
    story_box(.64f,.30f,.68f,.36f,.70f,.60f,.50f);
    story_box(.74f,.30f,.77f,.40f,.50f,.70f,.60f);
    story_box(.82f,.30f,.86f,.34f,.85f,.80f,.70f);
}
static void story_draw_medical_bay(void) {
    static const float wall_top[3]={.56f,.67f,.76f}, wall_low[3]={.76f,.86f,.91f};
    story_gradient(.20f,1.0f,12,wall_top,wall_low);
    story_box(0,0,1,.20f,.38f,.45f,.51f);                               // floor
    story_box(0,.20f,1,.225f,.30f,.38f,.44f);                           // baseboard
    for(int i=0;i<4;i++) story_box(.07f+.24f*(float)i,.90f,.25f+.24f*(float)i,.97f,.96f,.98f,1.0f);  // ceiling lights
    story_box(.05f,.28f,.16f,.84f,.42f,.58f,.74f);                      // curtain
    for(int i=0;i<5;i++) story_box(.05f+.022f*(float)i,.28f,.056f+.022f*(float)i,.84f,.36f,.50f,.66f);
    story_box(.24f,.24f,.64f,.30f,.62f,.67f,.72f);                      // bed frame
    story_box(.24f,.30f,.64f,.40f,.92f,.96f,1.0f);                      // mattress
    story_box(.24f,.40f,.33f,.45f,.86f,.92f,.98f);                      // pillow
    story_box(.26f,.20f,.29f,.24f,.45f,.50f,.55f);
    story_box(.59f,.20f,.62f,.24f,.45f,.50f,.55f);
    story_box(.68f,.20f,.70f,.70f,.60f,.64f,.68f);                      // drip stand
    story_box(.64f,.70f,.74f,.74f,.60f,.64f,.68f);
    story_box(.72f,.30f,.94f,.34f,.30f,.36f,.42f);                      // monitor stand and screen
    story_box(.74f,.34f,.92f,.72f,.20f,.24f,.28f);
    story_box(.755f,.355f,.905f,.705f,.04f,.07f,.09f);
    static const float beat[16]={0,0,0,0,.02f,-.02f,.12f,-.09f,.02f,0,0,0,.04f,0,0,0};
    for(int k=0;k<16;k++) story_box(.765f+.0085f*(float)k,.52f+beat[k],.772f+.0085f*(float)k,.535f+beat[k],.30f,.95f,.50f);
}
static void story_draw_generic_backdrop(const char *name) {
    unsigned hash=2166136261u;
    for(const char *c=name;*c;c++) { hash^=(unsigned char)*c; hash*=16777619u; }
    float c0[3]={.03f+.05f*(float)(hash&7)/7.0f,.05f+.06f*(float)((hash>>3)&7)/7.0f,.09f+.08f*(float)((hash>>6)&7)/7.0f};
    float c1[3]={c0[0]+.10f,c0[1]+.10f,c0[2]+.10f};
    story_gradient(.20f,1.0f,12,c0,c1);
    story_box(0,0,1,.20f,.05f,.05f,.06f);
    story_box(0,.20f,1,.215f,c1[0],c1[1],c1[2]);
}
static void story_draw_stadium_fallback(void) {
    static const float top[3]={.02f,.03f,.08f}, low[3]={.10f,.14f,.24f};
    story_gradient(.30f,1.0f,12,top,low);
    story_box(0,0,1,.30f,.10f,.13f,.17f);
    for(int i=0;i<9;i++) story_box(.06f+.11f*(float)i,.86f,.10f+.11f*(float)i,.92f,1.0f,.95f,.80f);   // arena lights
    for(int row=0;row<3;row++) for(int i=0;i<30;i++) {
        float u=.02f+.032f*(float)i, v=.34f+.07f*(float)row;
        unsigned h=(unsigned)(i*7919+row*104729)%5;
        story_box(u,v,u+.022f,v+.05f,.18f+.05f*(float)h,.20f+.04f*(float)h,.30f);
    }
}
// ---- smooth pictures: the upscaled *_hd.bmp files are drawn as textures, between two runs of the quad batch ----
typedef struct { GLuint id; int w,h; } StoryTexture;
static StoryTexture story_backdrop_tex, story_art_tex;
static struct { bool active; GLuint id; float x0,y0,x1,y1,u0,v0,u1,v1,bright; int split; } story_tex_draw;
static GLuint story_gl_program, story_gl_vao;     // the quad batch's, restored after a textured draw
static GLuint story_tex_program, story_tex_vao, story_tex_vbo;
static GLint story_tex_bright_loc;
static GLuint make_shader(GLenum type,const char *source);
static void story_tex_init(GLuint main_program,GLuint main_vao) {
    story_gl_program=main_program; story_gl_vao=main_vao;
    const char *vs="#version 330 core\nlayout(location=0) in vec2 p;layout(location=1) in vec2 t;out vec2 uv;"
                   "void main(){gl_Position=vec4(p,-.99,1);uv=t;}";
    const char *fs="#version 330 core\nin vec2 uv;uniform sampler2D img;uniform float bright;out vec4 o;"
                   "void main(){o=vec4(texture(img,uv).rgb*bright,1);}";
    GLuint v=make_shader(GL_VERTEX_SHADER,vs), f=make_shader(GL_FRAGMENT_SHADER,fs);
    story_tex_program=glCreateProgram();
    glAttachShader(story_tex_program,v); glAttachShader(story_tex_program,f); glLinkProgram(story_tex_program);
    GLint linked=0; glGetProgramiv(story_tex_program,GL_LINK_STATUS,&linked);
    glDeleteShader(v); glDeleteShader(f);
    if(!linked) { fprintf(stderr,"Texture program link failed; smooth pictures are off\n"); story_tex_program=0; return; }
    story_tex_bright_loc=glGetUniformLocation(story_tex_program,"bright");
    glUseProgram(story_tex_program);
    glUniform1i(glGetUniformLocation(story_tex_program,"img"),0);
    glGenVertexArrays(1,&story_tex_vao); glGenBuffers(1,&story_tex_vbo);
    glBindVertexArray(story_tex_vao); glBindBuffer(GL_ARRAY_BUFFER,story_tex_vbo);
    glBufferData(GL_ARRAY_BUFFER,6*4*sizeof(float),NULL,GL_STREAM_DRAW);
    glVertexAttribPointer(0,2,GL_FLOAT,GL_FALSE,4*sizeof(float),(void*)0); glEnableVertexAttribArray(0);
    glVertexAttribPointer(1,2,GL_FLOAT,GL_FALSE,4*sizeof(float),(void*)(2*sizeof(float))); glEnableVertexAttribArray(1);
    glUseProgram(main_program); glBindVertexArray(main_vao);
    glBindBuffer(GL_ARRAY_BUFFER,0);
}
static void story_texture_load(StoryTexture *texture,const char *path) {
    if(texture->id) { glDeleteTextures(1,&texture->id); texture->id=0; }
    texture->w=texture->h=0;
    if(!story_tex_program) return;
    StoryPortrait image={0};
    story_load_bmp(&image,path);
    if(!image.rgb) return;
    glGenTextures(1,&texture->id);
    glBindTexture(GL_TEXTURE_2D,texture->id);
    glPixelStorei(GL_UNPACK_ALIGNMENT,1);
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGB8,image.w,image.h,0,GL_RGB,GL_UNSIGNED_BYTE,image.rgb);
    glGenerateMipmap(GL_TEXTURE_2D);
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR);
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE);
    texture->w=image.w; texture->h=image.h;
    free(image.rgb);
}
// Asks for a texture to be drawn over the rectangle x0..x1, y0..y1 (NDC) after the quads emitted so far.
static void story_tex_request(const StoryTexture *texture,float x0,float y0,float x1,float y1,
                              float u0,float v0,float u1,float v1,float bright) {
    story_tex_draw.active=true; story_tex_draw.id=texture->id;
    story_tex_draw.x0=x0; story_tex_draw.y0=y0; story_tex_draw.x1=x1; story_tex_draw.y1=y1;
    story_tex_draw.u0=u0; story_tex_draw.v0=v0; story_tex_draw.u1=u1; story_tex_draw.v1=v1;
    story_tex_draw.bright=bright;
    story_tex_draw.split=vertex_count;
}
static void story_tex_flush(void) {
    if(!story_tex_draw.active || !story_tex_program) return;
    const float x0=story_tex_draw.x0,y0=story_tex_draw.y0,x1=story_tex_draw.x1,y1=story_tex_draw.y1;
    const float u0=story_tex_draw.u0,v0=story_tex_draw.v0,u1=story_tex_draw.u1,v1=story_tex_draw.v1;
    // The picture's first row is the top of the screen rectangle, so v grows downwards.
    const float quad_data[24]={x0,y1,u0,v0, x1,y1,u1,v0, x1,y0,u1,v1,  x0,y1,u0,v0, x1,y0,u1,v1, x0,y0,u0,v1};
    glUseProgram(story_tex_program);
    glUniform1f(story_tex_bright_loc,story_tex_draw.bright);
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D,story_tex_draw.id);
    glBindVertexArray(story_tex_vao);
    glBindBuffer(GL_ARRAY_BUFFER,story_tex_vbo);
    glBufferData(GL_ARRAY_BUFFER,sizeof(quad_data),quad_data,GL_STREAM_DRAW);
    glDrawArrays(GL_TRIANGLES,0,6);
    glUseProgram(story_gl_program); glBindVertexArray(story_gl_vao);
    glBindBuffer(GL_ARRAY_BUFFER,0);
}
// The backdrop fills the width; a picture taller than the area is cropped around its middle, as the pixel path does.
static void story_draw_backdrop_texture(const StoryTexture *texture) {
    float region=story_v(1.0f)-story_v(0.0f);
    float aspect=(float)win_width/(float)win_height;
    float visible=region/(2.0f*((float)texture->h/(float)texture->w)*aspect);
    if(visible>1.0f) visible=1.0f;
    float v0=(1.0f-visible)*.5f;
    story_tex_request(texture,-1.0f,story_v(0.0f),1.0f,story_v(1.0f),0,v0,1,v0+visible,1.0f);
}
static void story_draw_backdrop_image(const StoryPortrait *image) {
    // Every second pixel, filling the width, centred vertically; runs of one colour become one quad.
    int cols=image->w/2, rows=image->h/2;
    float dx=2.0f/(float)cols;
    float natural=dx*(float)win_width/(float)win_height;
    float region=story_v(1.0f)-story_v(0.0f);
    int visible=(int)(region/natural+.5f);
    if(visible>rows) visible=rows;
    float dy=region/(float)visible;
    int first=(rows-visible)/2;
    for(int row=0;row<visible;row++) {
        const unsigned char *line=image->rgb+(size_t)((first+row)*2)*(size_t)image->w*3;
        float y=story_v(1.0f)-(float)(row+1)*dy;
        for(int col=0;col<cols;) {
            int end=col+1;
            while(end<cols && !memcmp(line+col*2*3,line+end*2*3,3)) end++;
            quad(-1.0f+(float)col*dx,y,(float)(end-col)*dx+.0008f,dy+.0008f,
                 line[col*2*3]/255.0f,line[col*2*3+1]/255.0f,line[col*2*3+2]/255.0f);
            col=end;
        }
    }
}
static void story_update_art(void) {
    if(!strcmp(story_art_name,story_run.art) && !strcmp(story_art_effect,story_run.art_effect)) return;
    bool new_picture=strcmp(story_art_name,story_run.art)!=0;
    snprintf(story_art_name,sizeof(story_art_name),"%s",story_run.art);
    snprintf(story_art_effect,sizeof(story_art_effect),"%s",story_run.art_effect);
    story_art_started=SDL_GetTicks64();
    if(!new_picture) return;
    free(story_art_image.rgb);
    story_art_image.rgb=NULL; story_art_image.w=story_art_image.h=0;
    if(!story_art_name[0]) return;
    char file[STORY_NAME];
    size_t n=0;
    for(const char *c=story_art_name;*c && n+1<sizeof(file);c++) file[n++]=(char)((*c>='A' && *c<='Z') ? *c+32 : *c);
    file[n]=0;
    char path[160];
    snprintf(path,sizeof(path),"project/build/art/%s.bmp",file);
    story_load_bmp(&story_art_image,path);
    snprintf(path,sizeof(path),"project/build/art/%s_hd.bmp",file);
    story_texture_load(&story_art_tex,path);
}
// One frame of the illustration. fade brightens it from black, zoom slowly pushes in, pan slides across a slightly
// zoomed frame; every destination pixel is a nearest-neighbour sample of the source, merged into runs.
static void story_draw_art(void) {
    const StoryPortrait *image=&story_art_image;
    float seconds=story_capturing ? 3.0f : (float)(SDL_GetTicks64()-story_art_started)/1000.0f;
    float window=1.0f, shift=0, bright=1.0f;
    if(!strcmp(story_art_effect,"fade")) {
        bright=clampf(seconds/.8f,0,1);
    } else if(!strcmp(story_art_effect,"zoom")) {
        window=1.0f/(1.0f+.14f*clampf(seconds/8.0f,0,1));
    } else if(!strcmp(story_art_effect,"pan")) {
        window=1.0f/1.14f;
        shift=clampf(seconds/8.0f,0,1)*(1.0f-window);
    }
    float region=story_v(1.0f)-story_v(0.0f);
    int cols=image->w, rows=image->h;
    float dx=2.0f/(float)cols, dy=region/(float)rows;
    float step_x=window*(float)image->w/(float)cols, step_y=window*(float)image->h/(float)rows;
    float x0=!strcmp(story_art_effect,"pan") ? shift*(float)image->w : (1.0f-window)*(float)image->w*.5f;
    float y0=(1.0f-window)*(float)image->h*.5f;
    for(int row=0;row<rows;row++) {
        int sy=(int)(y0+((float)row+.5f)*step_y);
        if(sy>=image->h) sy=image->h-1;
        const unsigned char *line=image->rgb+(size_t)sy*(size_t)image->w*3;
        float y=story_v(1.0f)-(float)(row+1)*dy;
        for(int col=0;col<cols;) {
            int start_x=(int)(x0+((float)col+.5f)*step_x);
            if(start_x>=image->w) start_x=image->w-1;
            int end=col+1;
            while(end<cols) {
                int sx=(int)(x0+((float)end+.5f)*step_x);
                if(sx>=image->w) sx=image->w-1;
                if(memcmp(line+start_x*3,line+sx*3,3)) break;
                end++;
            }
            quad(-1.0f+(float)col*dx,y,(float)(end-col)*dx+.0008f,dy+.0008f,
                 line[start_x*3]/255.0f*bright,line[start_x*3+1]/255.0f*bright,line[start_x*3+2]/255.0f*bright);
            col=end;
        }
    }
}
static void story_draw_art_texture(const StoryTexture *texture) {
    float seconds=story_capturing ? 3.0f : (float)(SDL_GetTicks64()-story_art_started)/1000.0f;
    float window=1.0f, shift=0, bright=1.0f;
    if(!strcmp(story_art_effect,"fade")) bright=clampf(seconds/.8f,0,1);
    else if(!strcmp(story_art_effect,"zoom")) window=1.0f/(1.0f+.14f*clampf(seconds/8.0f,0,1));
    else if(!strcmp(story_art_effect,"pan")) { window=1.0f/1.14f; shift=clampf(seconds/8.0f,0,1)*(1.0f-window); }
    float u0=!strcmp(story_art_effect,"pan") ? shift : (1.0f-window)*.5f;
    float v0=(1.0f-window)*.5f;
    story_tex_request(texture,-1.0f,story_v(0.0f),1.0f,story_v(1.0f),u0,v0,u0+window,v0+window,bright);
    (void)texture;
}
static void story_update_backdrop(void) {
    if(!strcmp(story_backdrop_name,story_run.bg)) return;
    snprintf(story_backdrop_name,sizeof(story_backdrop_name),"%s",story_run.bg);
    char file[STORY_NAME];
    size_t n=0;
    for(const char *c=story_run.bg;*c && n+1<sizeof(file);c++) file[n++]=*c==' ' ? '_' : (char)((*c>='A' && *c<='Z') ? *c+32 : *c);
    file[n]=0;
    char path[160];
    snprintf(path,sizeof(path),"project/build/backdrops/%s.bmp",file);
    story_load_bmp(&story_backdrop,path);
    snprintf(path,sizeof(path),"project/build/backdrops/%s_hd.bmp",file);
    story_texture_load(&story_backdrop_tex,path);
}
static void story_draw_backdrop(void) {
    if(story_art_image.rgb) {
        if(story_art_tex.id) story_draw_art_texture(&story_art_tex); else story_draw_art();
        return;
    }
    if(story_backdrop_tex.id) { story_draw_backdrop_texture(&story_backdrop_tex); return; }
    if(story_backdrop.rgb) { story_draw_backdrop_image(&story_backdrop); return; }
    if(!strcmp(story_run.bg,"green room")) story_draw_green_room();
    else if(!strcmp(story_run.bg,"medical bay")) story_draw_medical_bay();
    else if(!strcmp(story_run.bg,"stadium")) story_draw_stadium_fallback();
    else story_draw_generic_backdrop(story_run.bg);
}
// Draws a portrait from its top-left corner, one source pixel per px screen pixels, merging runs of one colour.
static void story_draw_portrait(const StoryPortrait *portrait,const char *pilot,float x,float y,float px) {
    float dx=2.0f*px/(float)win_width, dy=2.0f*px/(float)win_height;
    if(!portrait->rgb) {   // no original art exported: a plain card with the pilot's initial
        quad(x,y-57*dy,57*dx,57*dy,.10f*story_draw_bright,.16f*story_draw_bright,.26f*story_draw_bright);
        char initial[2]={pilot[0],0};
        label(x+17*dx,y-14*dy,.030f,initial,.55f,.70f,.84f);
        return;
    }
    for(int row=0;row<portrait->h;row++) {
        const unsigned char *line=portrait->rgb+(size_t)row*(size_t)portrait->w*3;
        for(int col=0;col<portrait->w;) {
            int end=col+1;
            while(end<portrait->w && !memcmp(line+col*3,line+end*3,3)) end++;
            quad(x+(float)col*dx,y-(float)(row+1)*dy,(float)(end-col)*dx+.0008f,dy+.0008f,
                 line[col*3]/255.0f*story_draw_bright,line[col*3+1]/255.0f*story_draw_bright,
                 line[col*3+2]/255.0f*story_draw_bright);
            col=end;
        }
    }
}
static void story_stat_row(float x,float y,const char *name,int value) {
    label(x,y,.008f,name,.55f,.70f,.84f);
    quad(x+.46f,y-.040f,.40f,.040f,.08f,.12f,.20f);
    quad(x+.46f,y-.040f,.40f*(float)value/20.0f,.040f,.30f,.80f,.95f);
}
static void story_setup_card(int side,float x,const char *pilot,const char *har,const char *role) {
    char lines[8][80];
    story_draw_portrait(&story_portraits[side],pilot,x,.50f,3.0f);
    char upper[STORY_NAME];
    snprintf(upper,sizeof(upper),"%s",pilot);
    label(x+.40f,.46f,.009f,upper,side==0 ? .55f : 1,side==0 ? .90f : .70f,side==0 ? 1 : .62f);
    label(x+.40f,.36f,.0065f,role,.48f,.60f,.72f);
    char in_har[48];
    snprintf(in_har,sizeof(in_har),"IN %s",har);
    label(x+.40f,.29f,.008f,in_har,.92f,.95f,.98f);
    const int count=(int)(sizeof(story_pilot_stats)/sizeof(story_pilot_stats[0]));
    for(int i=0;i<count;i++) {
        if(strcmp(story_pilot_stats[i].name,pilot)) continue;
        story_stat_row(x,-.14f,"POWER",story_pilot_stats[i].power);
        story_stat_row(x,-.23f,"AGILITY",story_pilot_stats[i].agility);
        story_stat_row(x,-.32f,"ENDURANCE",story_pilot_stats[i].endurance);
    }
    int n=story_wrap(story_card_text(&story_data,pilot),20,lines,7);
    for(int i=0;i<n;i++) label(x,-.48f-.065f*(float)i,.0075f,lines[i],.85f,.90f,.95f);
}
// ---- routes: the selection screen can switch to the script written from the rival's side ----
static char story_script_path[512];
static bool story_save_named;   // --save-file was given: the save path stays as named
static void story_save_path_for(const char *script,char *out,size_t size) {
    const char *base=script;
    for(const char *c=script;*c;c++) if(*c=='/' || *c=='\\') base=c+1;
    snprintf(out,size,"project/build/story/%s.save",base);
}
static void story_set_script_path(const char *path) {
    snprintf(story_script_path,sizeof(story_script_path),"%s",path);
    if(!story_save_named) story_save_path_for(path,story_save_buf,sizeof(story_save_buf));
}
// The route script's path: the route line is relative to the folder of the script being played.
static void story_route_path(const char *script,const Story *story,char *out,size_t size) {
    size_t dir=0;
    for(size_t i=0;script[i];i++) if(script[i]=='/' || script[i]=='\\') dir=i+1;
    snprintf(out,size,"%.*s%s",(int)dir,script,story->route.path);
}
static void story_load_cast_portraits(void) {
    story_load_portrait(&story_portraits[0],story_data.player_pilot);
    story_load_portrait(&story_portraits[1],story_data.rival_pilot);
    story_setup_har=story_data.player_har[0]=='S' || story_data.player_har[0]=='s';
}
// Replaces the loaded script with its route; false (and the old script kept) when the route cannot be loaded.
static bool story_switch_route(void) {
    if(!story_data.has_route) return false;
    char path[512],error[256];
    story_route_path(story_script_path,&story_data,path,sizeof(path));
    Story next;
    if(!story_load(&next,path,error,sizeof(error))) {
        fprintf(stderr,"%s\n",error);
        story_notify("CANNOT LOAD THE OTHER PILOT'S STORY");
        return false;
    }
    story_free(&story_data);
    story_data=next;
    story_set_script_path(path);
    story_load_cast_portraits();
    memset(&story_run,0,sizeof(story_run));
    return true;
}
static void story_setup_hud(void) {
    static const char *har_names[2]={"JAGUAR","SHADOW"};
    quad(-1,-1,2,2,.015f,.025f,.065f);
    label(-.94f,.985f,.008f,"OMF2115 / STORY",.65f,.92f,1);
    label(-.94f,.89f,.016f,story_data.has_route ? "PILOT AND HAR" : "CHOOSE YOUR HAR",.80f,.88f,.96f);
    char choice[32];
    snprintf(choice,sizeof(choice),"< %s >",har_names[story_setup_har]);
    label(-.94f,.73f,.020f,choice,.30f,.90f,1);
    bool recommended=story_data.player_har[0] && (story_data.player_har[0]|32)==(har_names[story_setup_har][0]|32);
    if(recommended) label(.34f,.69f,.0075f,"RECOMMENDED",1,.85f,.40f);
    story_setup_card(0,-.94f,story_data.player_pilot,har_names[story_setup_har],"YOU");
    story_setup_card(1,.06f,story_data.rival_pilot,har_names[story_setup_har^1],"RIVAL");
    label(-.94f,-.945f,.007f,story_data.has_route ? "UP DOWN PILOT  LEFT RIGHT HAR  ENTER START"
                                                   : "LEFT RIGHT HAR  ENTER START  ESC QUIT",.48f,.60f,.72f);
}
// Starts the story with the chosen HAR for the player; the rival takes the other.
static void story_begin(int har_index) {
    static const char *names[2]={"Jaguar","Shadow"};
    StoryFlag flags[4];
    snprintf(flags[0].name,STORY_NAME,"player_har");
    snprintf(flags[0].value,STORY_NAME,"%s",names[har_index]);
    snprintf(flags[1].name,STORY_NAME,"rival_har");
    snprintf(flags[1].value,STORY_NAME,"%s",names[har_index^1]);
    snprintf(flags[2].name,STORY_NAME,"player_pilot");
    snprintf(flags[2].value,STORY_NAME,"%s",story_data.player_pilot);
    snprintf(flags[3].name,STORY_NAME,"rival_pilot");
    snprintf(flags[3].value,STORY_NAME,"%s",story_data.rival_pilot);
    story_start_with_flags(&story_run,&story_data,story_start_scene,flags,4);
    story_setup=false;
    story_sel=0;
    story_log_open=false;
    story_sound(SND_SELECT);
}
static int story_pilot_index(const char *name) {   // 0-9 in the pilot table, or -1
    for(int i=0;i<10;i++) {
        const char *a=story_pilot_stats[i].name,*b=name;
        while(*a && *b && (*a|32)==(*b|32)) { a++; b++; }
        if(!*a && !*b) return i;
    }
    return -1;
}
// The portraits of the two fighters stand over the backdrop, the speaker lit and the other dimmed.
static void story_draw_speakers(const char *speaker,bool all_lit) {
    if(story_art_image.rgb) return;   // an illustration replaces the cast
    int stand[2]={-1,-1};
    int speaking=story_pilot_index(speaker);
    if(story_data.has_cast) {
        stand[0]=story_pilot_index(story_data.player_pilot);
        stand[1]=story_pilot_index(story_data.rival_pilot);
    } else if(speaking>=0) {
        stand[0]=speaking;
    }
    if(speaking>=0 && speaking!=stand[0] && speaking!=stand[1]) stand[1]=speaking;   // a guest takes the right side
    const float px=3.6f;
    float dx=2.0f*px/(float)win_width, dy=2.0f*px/(float)win_height;
    float width=57*dx, height=57*dy;
    for(int side=0;side<2;side++) {
        int index=stand[side];
        if(index<0) continue;
        if(!story_speaker_tried[index]) {
            story_speaker_tried[index]=true;
            story_load_portrait(&story_speakers[index],story_pilot_stats[index].name);
        }
        bool lit=all_lit || (*speaker && index==speaking);
        float bright=lit ? 1.0f : .45f;
        float x=side==0 ? -.93f : .93f-width;
        float top=-.20f+height;
        const float *accent=side==0 ? (const float[]){.24f,.78f,1.0f} : (const float[]){1.0f,.55f,.27f};
        quad(x-.012f,top-height-.016f,width+.024f,height+.032f,accent[0]*bright,accent[1]*bright,accent[2]*bright);
        story_draw_bright=bright;
        story_draw_portrait(&story_speakers[index],story_pilot_stats[index].name,x,top,px);
        story_draw_bright=1.0f;
    }
}
// Advances the typewriter for the current say line; true once the whole line is showing.
static bool story_update_typing(void) {
    if(story_run.event!=STORY_EVENT_SAY) return true;
    Uint64 now=SDL_GetTicks64();
    size_t total=strlen(story_say_text(&story_run));
    if(story_typed_line!=(unsigned)story_run.log_total) {
        story_typed_line=(unsigned)story_run.log_total;
        story_typed=0;
        story_type_last=now;
    }
    if(story_capturing) story_typed=story_shot_typed>=0 && (size_t)story_shot_typed<total ? (float)story_shot_typed : (float)total;
    else story_typed+=(float)(now-story_type_last)*.055f;   // about 55 characters a second
    story_type_last=now;
    if(story_typed>(float)total) story_typed=(float)total;
    return (size_t)story_typed>=total;
}
// Flash and banner beats from the script. A flash is two quick white strobes; a banner slides in, holds, and leaves.
static void story_update_effect(void) {
    if(story_run.effect_serial==story_effect_seen) return;
    story_effect_seen=story_run.effect_serial;
    snprintf(story_effect_kind,sizeof(story_effect_kind),"%s",story_run.effect_kind);
    snprintf(story_effect_text,sizeof(story_effect_text),"%s",story_run.effect_text);
    story_effect_start=SDL_GetTicks64();
}
static float story_effect_age(void) { return (float)(SDL_GetTicks64()-story_effect_start)/1000.0f; }
static float story_banner_left(void) {   // seconds the banner is still up; Enter waits for it
    if(strcmp(story_effect_kind,"banner")) return 0;
    float left=1.4f-story_effect_age();
    return left>0 ? left : 0;
}
static void story_draw_effect(void) {
    float age=story_effect_age();
    if(!strcmp(story_effect_kind,"flash")) {
        if(!story_capturing && (age<.07f || (age>=.12f && age<.19f))) quad(-1,-1,2,2,1,1,1);
    } else if(!strcmp(story_effect_kind,"banner") && (age<1.4f || story_capturing)) {
        float slide=0;
        if(!story_capturing) slide=age<.18f ? -(1.0f-age/.18f)*2.2f : (age>1.15f ? (age-1.15f)/.25f*2.2f : 0);
        quad(-1+slide,.16f,2,.30f,.01f,.02f,.05f);
        quad(-1+slide,.46f,2,.02f,1,.75f,.30f);
        quad(-1+slide,.14f,2,.02f,1,.75f,.30f);
        float length=(float)strlen(story_effect_text);
        float size=fminf(.034f,1.8f/(length*6.0f));
        float left=-length*6.0f*size*.5f+slide;
        label(left+.006f,.414f-.006f,size,story_effect_text,.02f,.03f,.06f);
        label(left,.414f,size,story_effect_text,1,.92f,.70f);
    }
}
static void story_hud_body(void) {
    if(story_setup) { story_setup_hud(); return; }
    quad(-1,-1,2,2,.015f,.025f,.065f);
    story_update_backdrop();
    story_update_art();
    story_draw_backdrop();
    bool typed_all=story_update_typing();
    const char *speaker_name=story_run.event==STORY_EVENT_SAY ? story_event_cmd(&story_run)->speaker : "";
    story_draw_speakers(speaker_name,story_run.event!=STORY_EVENT_SAY);
    quad(-1,.86f,2,.14f,.03f,.07f,.14f);   // header band
    label(-.94f,.985f,.008f,"OMF2115 / STORY",.65f,.92f,1);
    char scene_label[64];
    snprintf(scene_label,sizeof(scene_label),"SCENE %.10s",story_data.scenes[story_run.scene].id);
    label(.10f,.985f,.008f,scene_label,.48f,.60f,.72f);
    if(story_run.bg[0] && !story_art_image.rgb) {   // the scene name over the backdrop, with a dark edge so it reads on any picture
        label(-.935f,.775f,.022f,story_run.bg,.02f,.03f,.06f);
        label(-.94f,.78f,.022f,story_run.bg,.88f,.94f,1);
    }
    if(story_debug_fights) label(.38f,.915f,.0065f,"DEBUG: FIGHTS",1,.75f,.30f);
    if(story_notice_pending) { story_notice_until=SDL_GetTicks64()+5000; story_notice_pending=false; }
    if(story_notice[0] && SDL_GetTicks64()<story_notice_until) label(-.94f,.915f,.008f,story_notice,.85f,1,.70f);
    quad(-.97f,-.98f,1.94f,.74f,.02f,.05f,.11f);
    char lines[8][80];
    float r,g,b;
    const char *hint="";
    if(story_run.event==STORY_EVENT_SAY) {
        const StoryCmd *c=story_event_cmd(&story_run);
        story_speaker_color(c->speaker,&r,&g,&b);
        if(*c->speaker) {   // narration has no name tab
            quad(-.97f,-.37f,.10f+.072f*(float)strlen(c->speaker),.13f,r*.30f,g*.30f,b*.30f);   // name tab
            quad(-.97f,-.37f,.012f,.13f,r,g,b);
            label(-.93f,-.285f,.012f,c->speaker,r,g,b);
        }
        int n=story_wrap(story_say_text(&story_run),34,lines,6);
        int shown=(int)story_typed;
        for(int i=0;i<n && shown>0;i++) {
            int length=(int)strlen(lines[i]);
            int take=shown<length ? shown : length;
            char part[80];
            memcpy(part,lines[i],(size_t)take);
            part[take]=0;
            label(-.92f,-.42f-.085f*(float)i,.009f,part,.92f,.95f,.98f);
            shown-=length+1;
        }
        if(typed_all && ((SDL_GetTicks64()/420)&1)) label(.88f,-.90f,.012f,">",1,.85f,.40f);   // blinking "next" arrow
        hint=typed_all ? "ENTER NEXT  S SKIP  L LOG" : "ENTER SHOW ALL  S SKIP  L LOG";
    } else if(story_run.event==STORY_EVENT_CHOICE) {
        label(-.92f,-.30f,.012f,"CHOOSE",.80f,.90f,.55f);
        float y=-.42f;
        for(int i=0;i<story_run.choice_count;i++) {
            const StoryCmd *c=story_choice_cmd(&story_run,i);
            int n=story_wrap(c->text,31,lines,2);
            bool on=i==story_sel;
            for(int k=0;k<n;k++) {
                label(-.92f,y,.009f,k==0 ? (on ? ">" : " ") : " ",1,.85f,.40f);
                label(-.86f,y,.009f,lines[k],on ? 1.0f : .55f,on ? .95f : .62f,on ? .75f : .70f);
                y-=.085f;
            }
            y-=.03f;
        }
        hint="UP DOWN SELECT  ENTER CHOOSE  L LOG";
    } else if(story_run.event==STORY_EVENT_FIGHT) {
        const StoryCmd *c=story_event_cmd(&story_run);
        label(-.92f,-.30f,.012f,"MATCH",1,.80f,.45f);
        char who[2][80];
        for(int i=0;i<2;i++) {
            char har[STORY_NAME];
            if(!story_fight_har(&story_run,c,i,har,sizeof(har))) snprintf(har,sizeof(har),"?");
            snprintf(who[i],sizeof(who[i]),"%s IN %s",c->pilot[i],har);
        }
        label(-.92f,-.44f,.009f,who[0],.55f,.90f,1);
        label(-.92f,-.53f,.009f,"VS",.70f,.78f,.85f);
        label(-.92f,-.62f,.009f,who[1],1,.70f,.62f);
        if(story_match_state==1) {
            label(-.92f,-.74f,.009f,"MATCH IN PROGRESS",1,.80f,.45f);
            label(-.92f,-.83f,.009f,"PLAY IN THE MATCH WINDOW.",.92f,.95f,.98f);
            hint="CLOSE THE MATCH WINDOW TO CANCEL";
        } else {
            label(-.92f,-.74f,.009f,"ENTER START MATCH",.92f,.95f,.98f);
            if(story_match_message[0]) label(-.92f,-.83f,.009f,story_match_message,1,.70f,.55f);
            hint=story_debug_fights ? "DEBUG: Y WIN  N LOSE" : "ENTER START  L LOG";
        }
    } else {
        label(-.92f,-.30f,.012f,"THE END",.80f,.90f,.55f);
        label(-.92f,-.44f,.009f,"R RESTART  ESC QUIT",.92f,.95f,.98f);
        hint="L LOG";
    }
    if(!story_log_open) label(-.92f,-.93f,.008f,hint,.48f,.60f,.72f);
    if(story_log_open) {
        quad(-.95f,-.92f,1.90f,1.80f,.01f,.02f,.05f);
        label(-.90f,.80f,.013f,"LOG",.65f,.92f,1);
        int count=story_log_count(&story_run);
        float y=.66f;
        for(int i=count>7 ? count-7 : 0;i<count;i++) {
            const StoryLogEntry *e=story_log_at(&story_run,i);
            char text[STORY_TEXT+STORY_NAME+4];
            snprintf(text,sizeof(text),"%s%s%s",e->speaker,*e->speaker ? ": " : "",e->text);
            story_speaker_color(e->speaker,&r,&g,&b);
            int n=story_wrap(text,38,lines,3);
            for(int k=0;k<n;k++) { label(-.90f,y,.008f,lines[k],r,g,b); y-=.07f; }
            y-=.025f;
        }
        label(-.90f,-.88f,.008f,"L CLOSE",.48f,.60f,.72f);
    }
}
static void story_hud(void) {
    story_tex_draw.active=false;
    story_music_sync(story_setup ? "menu" : story_run.music);
    story_update_effect();
    story_hud_body();
    if(!story_setup) story_draw_effect();
}
static void story_notify(const char *text) {
    snprintf(story_notice,sizeof(story_notice),"%s",text);
    story_notice_pending=true;   // the 5 s timer starts when the notice is first drawn
}
static void story_make_dirs(void) {
#ifdef _WIN32
    _mkdir("project"); _mkdir("project/build"); _mkdir("project/build/story");
#else
    mkdir("project",0755); mkdir("project/build",0755); mkdir("project/build/story",0755);
#endif
}
static void story_autosave(void) {
    if(!story_save_enabled || !story_run.story) return;
    char error[256];
    story_make_dirs();
    if(!story_save(&story_run,story_save_path,error,sizeof(error))) {
        fprintf(stderr,"%s\n",error);
        story_notify("SAVE FAILED");
    }
}
// ---- real matches: run the live pipeline as a child process and wait for its result file ----
// Windows only (the live link uses shared memory). The child runs inside a job object that is killed when
// this window exits, so closing the story can never leave a hidden OpenOMF running.
static char story_match_result_path[512];
#ifdef _WIN32
static HANDLE story_match_job;
static HANDLE story_match_child;
#endif
static bool story_har_equal(const char *a,const char *b) {
    for(;*a && *b;a++,b++) if((*a|32)!=(*b|32)) return false;
    return *a==*b;
}
static void story_notify(const char *text);
static void story_autosave(void);
static void story_match_finish(bool win) {
    story_record(&story_run,"MATCH",win ? "You won the match." : "You lost the match.");
    story_fight_result(&story_run,win);
    story_sel=0;
    story_match_state=0;
    story_match_message[0]=0;
    story_autosave();
}
static void story_match_start(void) {
    if(story_run.event!=STORY_EVENT_FIGHT || story_match_state==1) return;
    const StoryCmd *c=story_event_cmd(&story_run);
    story_match_message[0]=0;
    char har0[STORY_NAME],har1[STORY_NAME];
    if(!story_fight_har(&story_run,c,0,har0,sizeof(har0)) || !story_fight_har(&story_run,c,1,har1,sizeof(har1))) {
        snprintf(story_match_message,sizeof(story_match_message),"A FIGHTER HAS NO HAR: CHECK THE SCRIPT.");
        return;
    }
    if(story_har_equal(har0,har1)) {
        snprintf(story_match_message,sizeof(story_match_message),"BOTH FIGHTERS USE %s: NOT SUPPORTED YET.",har0);
        return;
    }
#ifdef _WIN32
    char launcher[512],result[512];
    if(!_fullpath(launcher,"project/scripts/run-blockout-jaguar.ps1",sizeof(launcher)) ||
       !_fullpath(result,"project/build/story/match-result.txt",sizeof(result))) {
        snprintf(story_match_message,sizeof(story_match_message),"CANNOT FIND THE MATCH LAUNCHER.");
        return;
    }
    FILE *probe=fopen(launcher,"rb");
    if(!probe) {
        snprintf(story_match_message,sizeof(story_match_message),"MATCH LAUNCHER MISSING: RUN FROM THE REPO ROOT.");
        return;
    }
    fclose(probe);
    story_make_dirs();
    remove(result);
    snprintf(story_match_result_path,sizeof(story_match_result_path),"%s",result);
    char cmd[1600];
    snprintf(cmd,sizeof(cmd),"powershell.exe -NoProfile -ExecutionPolicy Bypass -File \"%s\" -Player %s -Pilot %s "
             "-RivalPilot %s -ResultFile \"%s\"%s",launcher,har0,c->pilot[0],c->pilot[1],result,
             story_muted ? "" : " -Sound");
    if(!story_match_job) {
        story_match_job=CreateJobObjectA(NULL,NULL);
        if(story_match_job) {
            JOBOBJECT_EXTENDED_LIMIT_INFORMATION limits;
            memset(&limits,0,sizeof(limits));
            limits.BasicLimitInformation.LimitFlags=JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE;
            SetInformationJobObject(story_match_job,JobObjectExtendedLimitInformation,&limits,sizeof(limits));
        }
    }
    STARTUPINFOA startup;
    PROCESS_INFORMATION process;
    memset(&startup,0,sizeof(startup));
    startup.cb=sizeof(startup);
    memset(&process,0,sizeof(process));
    if(!CreateProcessA(NULL,cmd,NULL,NULL,FALSE,CREATE_SUSPENDED|CREATE_NO_WINDOW,NULL,NULL,&startup,&process)) {
        snprintf(story_match_message,sizeof(story_match_message),"COULD NOT START THE MATCH.");
        return;
    }
    if(story_match_job) AssignProcessToJobObject(story_match_job,process.hProcess);
    ResumeThread(process.hThread);
    CloseHandle(process.hThread);
    story_match_child=process.hProcess;
    story_match_state=1;
    story_sound(SND_SELECT);
#else
    snprintf(story_match_message,sizeof(story_match_message),"REAL MATCHES NEED WINDOWS FOR NOW.");
#endif
}
// Called every frame: notices when the match process has ended and reads its result.
static void story_match_poll(void) {
#ifdef _WIN32
    if(story_match_state!=1 || !story_match_child) return;
    if(WaitForSingleObject(story_match_child,0)!=WAIT_OBJECT_0) return;
    CloseHandle(story_match_child);
    story_match_child=NULL;
    int winner=-1;
    FILE *f=fopen(story_match_result_path,"r");
    if(f) {
        if(fscanf(f,"winner=%d",&winner)!=1) winner=-1;
        fclose(f);
    }
    if(winner==0 || winner==1) {
        story_match_finish(winner==0);
    } else {
        story_match_state=2;
        snprintf(story_match_message,sizeof(story_match_message),"MATCH CLOSED WITH NO RESULT. ENTER TO RETRY.");
    }
#endif
}
static void story_restart(void) {
    if(story_data.has_cast) {
        memset(&story_run,0,sizeof(story_run));
        story_setup=true;
        story_setup_har=story_data.player_har[0]=='S' || story_data.player_har[0]=='s';
    } else {
        story_start(&story_run,&story_data,story_start_scene);
    }
    story_sel=0;
    story_log_open=false;
    if(story_save_enabled) {
        remove(story_save_path);
        story_notify("RESTARTED  SAVE CLEARED");
    }
}
// One input, shared by the keyboard and the scripted --script option. Tokens: a, c<N>, u, d, w, l, s, g, r.
static void story_act(char action,int number) {
    if(story_setup) return;   // nothing to act on until a HAR is chosen
    if(action=='a' && !story_script_running) {
        if(story_banner_left()>0) return;   // let a banner finish
        if(story_run.event==STORY_EVENT_SAY && story_typed_line==(unsigned)story_run.log_total &&
           (size_t)story_typed<strlen(story_say_text(&story_run))) {   // the first Enter shows the whole line
            story_typed=(float)strlen(story_say_text(&story_run));
            return;
        }
    }
    StoryEventKind before=story_run.event;
    switch(action) {
        case 'a':
            if(story_run.event==STORY_EVENT_SAY) story_advance(&story_run);
            else if(story_run.event==STORY_EVENT_CHOICE) { story_choose(&story_run,story_sel); story_sel=0; story_sound(SND_SELECT); }
            else if(story_run.event==STORY_EVENT_FIGHT) story_match_start();
            break;
        case 'm': story_match_start(); break;
        case 'c': if(story_choose(&story_run,number)) { story_sel=0; story_sound(SND_SELECT); } break;
        case 'u': if(story_run.event==STORY_EVENT_CHOICE) { story_sel=(story_sel+story_run.choice_count-1)%story_run.choice_count; story_sound(SND_MOVE); } break;
        case 'd': if(story_run.event==STORY_EVENT_CHOICE) { story_sel=(story_sel+1)%story_run.choice_count; story_sound(SND_MOVE); } break;
        case 'w':
            if(story_run.event==STORY_EVENT_FIGHT) story_note(&story_run,"Match skipped: win");
            story_fight_result(&story_run,true);
            break;
        case 'l':
            if(story_run.event==STORY_EVENT_FIGHT) story_note(&story_run,"Match skipped: loss");
            story_fight_result(&story_run,false);
            break;
        case 's': story_skip(&story_run); story_sel=0; break;
        case 'g': story_log_open=!story_log_open; break;
        case 'r': story_restart(); break;
    }
    // Autosave when a choice or match is decided, and whenever play stops at a choice, match, or the end.
    bool progressed=action=='a' || action=='c' || action=='w' || action=='l' || action=='s';
    if(progressed && (before!=STORY_EVENT_SAY || story_run.event!=STORY_EVENT_SAY)) story_autosave();
}
static void story_key(SDL_Scancode key) {
    if(key==SDL_SCANCODE_M) {
        story_muted=!story_muted;
        story_notify(story_muted ? "SOUND OFF" : "SOUND ON");
        return;
    }
    if(story_setup) {
        if(key==SDL_SCANCODE_UP || key==SDL_SCANCODE_DOWN || key==SDL_SCANCODE_W || key==SDL_SCANCODE_S) {
            if(story_data.has_route) { if(story_switch_route()) { story_setup=true; story_sound(SND_MOVE); } }
            else { story_setup_har^=1; story_sound(SND_MOVE); }
        } else if(key==SDL_SCANCODE_LEFT || key==SDL_SCANCODE_RIGHT || key==SDL_SCANCODE_A || key==SDL_SCANCODE_D) {
            story_setup_har^=1; story_sound(SND_MOVE);
        }
        else if(key==SDL_SCANCODE_RETURN || key==SDL_SCANCODE_SPACE) story_begin(story_setup_har);
        return;
    }
    switch(key) {
        case SDL_SCANCODE_SPACE: case SDL_SCANCODE_RETURN: story_act('a',0); break;
        case SDL_SCANCODE_UP: story_act('u',0); break;
        case SDL_SCANCODE_DOWN: story_act('d',0); break;
        case SDL_SCANCODE_S: story_act('s',0); break;
        case SDL_SCANCODE_L: story_act('g',0); break;
        case SDL_SCANCODE_R: story_act('r',0); break;
        case SDL_SCANCODE_Y: if(story_debug_fights) story_act('w',0); break;
        case SDL_SCANCODE_N: if(story_debug_fights) story_act('l',0); break;
        default: break;
    }
}
static void story_run_script(const char *script) {
    story_script_running=true;
    for(const char *p=script;*p;) {
        char action=*p++;
        int number=0;
        if(action=='c') { char *end; number=(int)strtol(p,&end,10); p=end; }
        story_act(action,number);
        while(*p==',') p++;
    }
    story_script_running=false;
}
static void world(void) {
    if(model_preview_mode) {
        const float angle=model_preview_view==0 ? -1.5707963f :
                          model_preview_view==1 ? 3.14159265f : 0.0f;
        Fighter jaguar={.x=-1.55f,.facing=angle,.pose_height=1};
        Fighter shadow={.x=1.55f,.facing=angle,.pose_height=1};
        if(model_preview_pose==1 || model_preview_pose==2) {
            jaguar.source_animation=model_preview_pose==1 ? 42 : 41;
            shadow.source_animation=model_preview_pose==1 ? 43 : 42;
            jaguar.pose_reach=shadow.pose_reach=.9f;
            jaguar.kind=shadow.kind=model_preview_pose==2 ? 2 : 1;
            jaguar.source_sprite=3;
            shadow.source_sprite=model_preview_pose==1 ? 2 : 3;
        } else if(model_preview_pose==3) {
            jaguar.guard=shadow.guard=true;
        } else if(model_preview_pose==4) {
            jaguar.pose_height=shadow.pose_height=.68f;
        } else if(model_preview_pose==5) {
            jaguar.pose_stride=shadow.pose_stride=.28f;
        } else if(model_preview_pose==6) {
            jaguar.y=shadow.y=.72f;
            jaguar.source_state=shadow.source_state=6;
        } else if(model_preview_pose==7) {
            jaguar.stun=shadow.stun=1;
            jaguar.source_state=shadow.source_state=7;
        } else if(model_preview_pose==8) {
            jaguar.source_animation=21;
            shadow.source_animation=23;
            jaguar.source_sprite=3;
            shadow.source_sprite=2;
        }
        box(0,-.10f,0,7.0f,.12f,1.8f,0,.10f,.14f,.19f);
        box(-1.55f,.005f,0,1.3f,.012f,.03f,0,.15f,.46f,.30f);
        box(1.55f,.005f,0,1.3f,.012f,.03f,0,.15f,.46f,.30f);
        robot(&jaguar,0,0);
        robot(&shadow,1,0);
        return;
    }
    camera_x = source_replay_mode ? 0 : (player.x+rival.x)*.5f;
    camera_y = source_replay_mode ? clampf(fmaxf(player.y, rival.y) * .90f, 0, 2.9f) : 0;
    player.presentation_x = 0;
    rival.presentation_x = 0;
    if(source_replay_mode && source_replay.count) {
        const SourceFrame *frame=&source_replay.frames[source_replay_index];
        int player_har=frame->fighter[0].har;
        int rival_har=frame->fighter[1].har;
        float player_reach=source_close_contact_attack(player_har,player.source_animation) ? player.pose_reach : 0;
        float rival_reach=source_close_contact_attack(rival_har,rival.source_animation) ? rival.pose_reach : 0;
        float engagement=fmaxf(player_reach,rival_reach);
        float source_distance=distance_x(&player,&rival);
        float vertical_distance=fabsf(player.y-rival.y);
        if(engagement>.35f && vertical_distance<1.25f && source_distance<1.20f) {
            // Separate overlapping blockout torsos only during source-keyed contact poses.
            // Source positions, hit results, and projectile locations remain unchanged.
            float blend=clampf((engagement-.35f)/.65f,0,1);
            float offset=(1.20f-source_distance)*.5f*blend;
            if(player.x<=rival.x) {
                player.presentation_x=-offset;
                rival.presentation_x=offset;
            } else {
                player.presentation_x=offset;
                rival.presentation_x=-offset;
            }
        }
    }
    stadium_background();
    box(0,-.28f,0,17.0f,.42f,8.0f,0,.065f,.105f,.16f);
    box(0,-.045f,0,15.1f,.045f,6.5f,0,.10f,.16f,.24f);
    for(int i=-8;i<=8;i+=2) box((float)i,.002f,0,.027f,.012f,7.7f,0,.12f,.29f,.38f);
    for(int i=-4;i<=4;i+=2) box(0,.005f,(float)i,16.5f,.012f,.027f,0,.12f,.29f,.38f);
    box(0,.035f,0,.055f,.02f,7.7f,0,.21f,.63f,.70f);
    box(0,.035f,0,16.5f,.02f,.055f,0,.21f,.63f,.70f);
    ring(0,0,2.55f,2.60f,.20f,.43f,.53f);
    ring(0,0,3.50f,3.54f,.12f,.26f,.35f);
    for(int i=-4;i<=4;i+=2) {
        box(-8.3f,.57f,(float)i,.28f,1.13f,.28f,0,.18f,.44f,.56f);
        box(8.3f,.57f,(float)i,.28f,1.13f,.28f,0,.18f,.44f,.56f);
        box(-8.3f,1.18f,(float)i,.37f,.12f,.37f,0,.50f,.91f,.99f);
        box(8.3f,1.18f,(float)i,.37f,.12f,.37f,0,.50f,.91f,.99f);
    }
    box(0,.68f,4.2f,17,.08f,.12f,0,.22f,.63f,.73f);
    box(0,.68f,-4.2f,17,.08f,.12f,0,.22f,.63f,.73f);
    // The front apron gives the arena a visible edge below the fight plane.
    box(0,-1.38f,4.18f,17.0f,2.65f,.35f,0,.045f,.075f,.125f);
    box(0,-.16f,4.39f,17.0f,.12f,.08f,0,.15f,.37f,.46f);
    box(0,-2.53f,4.39f,17.0f,.12f,.08f,0,.12f,.25f,.34f);
    for(int i=-7;i<=7;i+=2) {
        float x=(float)i;
        box(x,-1.34f,4.40f,1.56f,1.74f,.035f,0,.075f,.12f,.19f);
        box(x,-.77f,4.44f,1.12f,.045f,.025f,0,.17f,.42f,.48f);
        box(x,-1.03f,4.44f,.86f,.035f,.025f,0,.11f,.27f,.34f);
        box(x,-1.30f,4.44f,.62f,.035f,.025f,0,.11f,.27f,.34f);
    }
    ring(player.x,0,.65f,.72f,.12f,.58f,.72f);
    ring(rival.x,0,.65f,.72f,.72f,.17f,.34f);
    if(source_replay_mode && live_impact_time>0) {
        float progress=1.0f-live_impact_time/.20f;
        float radius=.62f+progress*.62f;
        float brightness=1.0f-progress*.72f;
        if(live_impact_kind==2)
            ring(live_impact_x,0,radius,radius+.09f,brightness*.30f,brightness*.86f,brightness);
        else
            ring(live_impact_x,0,radius,radius+.09f,brightness,brightness*.79f,brightness*.32f);
    }
    float pose_time=source_follow_mode ? source_visual_time : elapsed;
    int player_har=source_replay_mode && source_replay.count ?
                   source_replay.frames[source_replay_index].fighter[0].har : 0;
    int rival_har=source_replay_mode && source_replay.count ?
                  source_replay.frames[source_replay_index].fighter[1].har : 1;
    robot(&player,player_har,pose_time);
    robot(&rival,rival_har,pose_time+1);
    source_projectiles();
}
static void hud(void) {
    if(model_preview_mode) {
        const char *view=model_preview_view==0 ? "RIGHT SIDE" :
                         model_preview_view==1 ? "FRONT" : "BACK";
        const char *pose[]={"IDLE","PUNCH","KICK","GUARD","CROUCH",
                            "WALK","JUMP","HIT","SPECIAL"};
        quad(-1,.80f,2,.20f,.02f,.04f,.10f);
        label(-.92f,.94f,.014f,"OMF2115 / MODEL BLOCKOUTS",.72f,.90f,1);
        label(-.92f,.85f,.012f,view,.60f,.95f,.67f);
        label(-.12f,.85f,.012f,pose[model_preview_pose],.60f,.95f,.67f);
        label(-.67f,-.64f,.015f,"JAGUAR",.80f,.87f,.94f);
        label(.24f,-.64f,.015f,"SHADOW",.80f,.87f,.94f);
        label(-.92f,-.76f,.009f,"8 WALK  9 JUMP  H HIT  M SPECIAL",.57f,.65f,.72f);
        label(-.92f,-.84f,.009f,"1 SIDE  2 FRONT  3 BACK  0 IDLE",.57f,.65f,.72f);
        label(-.92f,-.92f,.0085f,"4 PUNCH  5 KICK  6 GUARD  7 CROUCH",.57f,.65f,.72f);
        return;
    }
    quad(-1,.83f,2,.17f,.02f,.04f,.10f);
    label(-.94f,.95f,.0145f,source_follow_mode ? "OMF2115 / LIVE SOURCE" :
          (source_replay_mode ? "OMF2115 / SOURCE REPLAY" : "OMF2115 / SIDE ON SPIKE"),
          .62f,.89f,.96f);
    if(phase==1) {
        quad(-.94f,.78f,.78f,.035f,.14f,.18f,.25f);
        quad(-.94f,.78f,.78f*player.hp/player.max_hp,.035f,.16f,.83f,.94f);
        quad(.16f,.78f,.78f,.035f,.14f,.18f,.25f);
        quad(.16f,.78f,.78f*rival.hp/rival.max_hp,.035f,.94f,.30f,.47f);
        if(source_replay_mode) {
            char left[48], right[48];
            const SourceFrame *frame = &source_replay.frames[source_replay_index];
            const char *left_name = source_follow_mode && source_live_pilot_name ?
                                    source_live_pilot_name : source_har_name(frame->fighter[0].har);
            const char *right_name = source_follow_mode && source_live_rival_name ?
                                     source_live_rival_name : source_har_name(frame->fighter[1].har);
            snprintf(left,sizeof(left),"%s %d",left_name,
                     frame->fighter[0].health > 0 ? frame->fighter[0].health : 0);
            snprintf(right,sizeof(right),"%s %d",right_name,
                     frame->fighter[1].health > 0 ? frame->fighter[1].health : 0);
            label(-.94f,.72f,.011f,left,.72f,.90f,1);
            label(.16f,.72f,.011f,right,1,.72f,.79f);
        } else {
            const char *left = source_follow_mode && source_live_pilot_name ? source_live_pilot_name : "JAGUAR";
            const char *right = source_follow_mode && source_live_rival_name ? source_live_rival_name : "SHADOW";
            label(-.94f,.72f,.013f,left,.72f,.90f,1);
            label(.37f,.72f,.013f,right,1,.72f,.79f);
        }
        quad(-1,-1,2,.26f,.02f,.04f,.10f);
        label(-.94f,-.79f,.011f,source_input_enabled ? "A D MOVE  W JUMP  S DUCK" :
              (source_follow_mode ? "LIVE OPENOMF MATCH  ESC QUIT" :
              (source_replay_mode ? "SPACE PAUSE  LEFT RIGHT SEEK" : "A D MOVE  W JUMP  J PUNCH")),
              .78f,.84f,.91f);
        if(source_replay_mode) {
            char replay_footer[64];
            snprintf(replay_footer,sizeof(replay_footer),source_input_enabled ? "J PUNCH  K KICK  TICK %u" :
                     (source_follow_mode ? "SOURCE TICK %u" :
                     "R RESTART  ESC QUIT  TICK %u"),
                     source_replay.frames[source_replay_index].tick);
            label(-.94f,-.91f,.011f,replay_footer,.78f,.84f,.91f);
        } else {
            label(-.94f,-.91f,.011f,"K KICK  HOLD BACK TO BLOCK",.78f,.84f,.91f);
        }
        if(source_replay_mode && source_replay.count) {
            const SourceFrame *frame=&source_replay.frames[source_replay_index];
            bool player_down=frame->fighter[0].health<=0;
            bool rival_down=frame->fighter[1].health<=0;
            bool match_decided=frame->has_match_result && frame->match_winner>=0;
            bool round_decided=frame->has_events && frame->round_winner>=0;
            if(source_follow_mode && source_live_winner >= 0) {
                const char *result=source_live_winner==0 ? "YOU WIN" : "YOU LOSE";
                float result_x=-(float)strlen(result)*.022f*3.0f;
                quad(-.67f,-.02f,1.34f,.72f,.025f,.045f,.10f);
                label(result_x,.25f,.022f,result,
                      source_live_winner==0?.67f:1.0f,
                      source_live_winner==0?.95f:.58f,
                      source_live_winner==0?.77f:.63f);
                if(live_result_path) {
                    label(-.60f,.08f,.015f,"ENTER: BACK TO THE STORY",.85f,.9f,.96f);
                } else {
                    label(-.68f,.10f,.015f,"TRY AGAIN?",.85f,.9f,.96f);
                    label(-.40f,-.08f,.018f,"YES",try_again_choice==0?.38f:.48f,
                          try_again_choice==0?.92f:.55f,try_again_choice==0?1.0f:.64f);
                    label(.12f,-.08f,.018f,"NO",try_again_choice==1?.38f:.48f,
                          try_again_choice==1?.92f:.55f,try_again_choice==1?1.0f:.64f);
                    label(-.59f,-.23f,.009f,"LEFT/RIGHT SELECT  ENTER CONFIRM",.57f,.70f,.80f);
                }
            } else if(match_decided || round_decided || player_down || rival_down) {
                bool player_won=match_decided ? frame->match_winner==0 :
                                round_decided ? frame->round_winner==0 : rival_down && !player_down;
                const char *result=match_decided ? (player_won ? "YOU WIN" : "YOU LOSE") :
                                   !round_decided && player_down && rival_down ? "ROUND DRAW" :
                                   player_won ? "ROUND WON" : "ROUND LOST";
                float size=match_decided ? .022f : .018f;
                float result_x=-(float)strlen(result)*size*3.0f;
                quad(-.67f,-.22f,1.34f,.48f,.025f,.045f,.10f);
                label(result_x,.14f,size,result,
                      player_won ? .67f : 1.0f,
                      player_won ? .95f : .58f,
                      player_won ? .77f : .63f);
                label(-.37f,-.08f,.012f,"PLAYER 1",.80f,.88f,.94f);
            }
        }
        if(source_follow_mode && live_round_intro_time>0) {
            const char *intro=live_round_intro_time>.75f ? "ROUND 1" : "FIGHT";
            float size=live_round_intro_time>.75f ? .026f : .030f;
            quad(-.65f,-.15f,1.30f,.34f,.025f,.045f,.10f);
            label(-(float)strlen(intro)*size*3.0f,.09f,size,intro,.72f,.95f,1.0f);
        }
    } else {
        quad(-.78f,-.39f,1.56f,.65f,.025f,.045f,.10f);
        if(phase==0) {
            label(-.68f,.15f,.021f,"OMF2115",.74f,.94f,1);
            label(-.68f,.00f,.015f,source_follow_mode ? "LIVE SOURCE VIEW" :
                  "SIDE ON FIGHTING SPIKE",.85f,.9f,.96f);
            label(-.68f,-.11f,.015f,source_follow_mode ? "STARTING OPENOMF MATCH" :
                  "DEFEAT THE RIVAL FRAME.",.85f,.9f,.96f);
            label(-.68f,-.28f,.017f,source_follow_mode ? "ESC TO QUIT" :
                  "ENTER TO DEPLOY",.38f,.88f,.98f);
        } else if(phase==2) {
            label(-.68f,.15f,.021f,"YOU WIN",.74f,.94f,1);
            label(-.68f,.04f,.015f,"TRY AGAIN?",.85f,.9f,.96f);
            label(-.40f,-.12f,.018f,"YES",try_again_choice==0?.38f:.48f,
                  try_again_choice==0?.92f:.55f,try_again_choice==0?1.0f:.64f);
            label(.12f,-.12f,.018f,"NO",try_again_choice==1?.38f:.48f,
                  try_again_choice==1?.92f:.55f,try_again_choice==1?1.0f:.64f);
            label(-.68f,-.24f,.009f,"LEFT/RIGHT SELECT  ENTER CONFIRM",.57f,.70f,.80f);
        } else {
            label(-.68f,.15f,.021f,"YOU LOSE",1,.52f,.62f);
            label(-.68f,.04f,.015f,"TRY AGAIN?",.85f,.9f,.96f);
            label(-.40f,-.12f,.018f,"YES",try_again_choice==0?.38f:.48f,
                  try_again_choice==0?.92f:.55f,try_again_choice==0?1.0f:.64f);
            label(.12f,-.12f,.018f,"NO",try_again_choice==1?.38f:.48f,
                  try_again_choice==1?.92f:.55f,try_again_choice==1?1.0f:.64f);
            label(-.68f,-.24f,.009f,"LEFT/RIGHT SELECT  ENTER CONFIRM",.57f,.70f,.80f);
        }
    }
}
static GLuint make_shader(GLenum type,const char *source) {
    GLuint s=glCreateShader(type); glShaderSource(s,1,&source,NULL); glCompileShader(s);
    GLint ok=0; glGetShaderiv(s,GL_COMPILE_STATUS,&ok);
    if(!ok) { char log[1024]; glGetShaderInfoLog(s,sizeof(log),NULL,log); fprintf(stderr,"Shader: %s\n",log); exit(1); }
    return s;
}
// Captures go to project/build, next to the files the OMF2115 tools generate, not into OpenOMF's build tree.
static void ensure_capture_dir(void) {
#ifdef _WIN32
    _mkdir("project");
    _mkdir("project/build");
#else
    mkdir("project",0755);
    mkdir("project/build",0755);
#endif
}

static bool save_frame_bmp(const char *path) {
    ensure_capture_dir();
    SDL_Surface *shot=SDL_CreateRGBSurfaceWithFormat(0,win_width,win_height,32,SDL_PIXELFORMAT_RGBA32);
    if(!shot) return false;
    glReadPixels(0,0,win_width,win_height,GL_RGBA,GL_UNSIGNED_BYTE,shot->pixels);
    unsigned char *tmp=malloc((size_t)shot->pitch);
    if(!tmp) { SDL_FreeSurface(shot); return false; }
    for(int y=0;y<win_height/2;y++) {
        unsigned char *top=(unsigned char*)shot->pixels+y*shot->pitch;
        unsigned char *bottom=(unsigned char*)shot->pixels+(win_height-1-y)*shot->pitch;
        memcpy(tmp,top,(size_t)shot->pitch);
        memcpy(top,bottom,(size_t)shot->pitch);
        memcpy(bottom,tmp,(size_t)shot->pitch);
    }
    free(tmp);
    bool saved=SDL_SaveBMP(shot,path)==0;
    SDL_FreeSurface(shot);
    return saved;
}
static int self_test(void) {
    reset_fight();
    unsigned char keys[SDL_NUM_SCANCODES]={0};
    keys[SDL_SCANCODE_J]=1;
    for(int i=0;i<900 && phase==1;i++) tick(keys);
    if(phase != 2 || player.hp <= 0) {
        fprintf(stderr,"Expected a reachable win with held light attack; phase=%d player=%.0f rival=%.0f\n",
                phase,player.hp,rival.hp);
        return 1;
    }
    float remaining=player.hp;
    reset_fight(); player.x=3.0f; rival.x=-3.0f;
    tick((unsigned char[SDL_NUM_SCANCODES]){0});
    if(fabsf(player.facing-1.5707963f)>.05f || fabsf(rival.facing+1.5707963f)>.05f) {
        fputs("Fighters failed to turn toward one another after crossing\n",stderr);
        return 1;
    }
    reset_fight();
    unsigned char jump_keys[SDL_NUM_SCANCODES]={0};
    jump_keys[SDL_SCANCODE_W]=1;
    tick(jump_keys);
    if(player.y <= 0 || player.vy <= 0) {
        fputs("Jump did not leave the fighting plane\n",stderr);
        return 1;
    }
    for(int i=0;i<90;i++) tick((unsigned char[SDL_NUM_SCANCODES]){0});
    if(player.y != 0 || player.vy != 0) {
        fputs("Jump did not land on the fighting plane\n",stderr);
        return 1;
    }
    reset_fight();
    unsigned char back_keys[SDL_NUM_SCANCODES]={0};
    back_keys[SDL_SCANCODE_A]=1;
    tick(back_keys);
    if(!player.guard) {
        fputs("Holding back failed to guard while facing right\n",stderr);
        return 1;
    }
    reset_fight(); player.x=3.0f; rival.x=-3.0f;
    back_keys[SDL_SCANCODE_A]=0;
    back_keys[SDL_SCANCODE_D]=1;
    tick(back_keys);
    if(!player.guard) {
        fputs("Holding back failed to guard after crossing\n",stderr);
        return 1;
    }
    printf("3D side-on spike OK: win, facing, jump, and back-to-block verified; %.0f HP left\n",remaining);
    return 0;
}
int main(int argc,char **argv) {
    if(argc>1 && strcmp(argv[1],"--self-test")==0) return self_test();
    selection_mode=argc>1 && strcmp(argv[1],"--select")==0;
    selection_path=selection_mode && argc==3 ? argv[2] : NULL;
    if(selection_mode && !selection_path) {
        fputs("Usage: omf3d_prototype --select selection.txt\n",stderr);
        return 1;
    }
    model_preview_mode=argc>1 && (strcmp(argv[1],"--model-preview")==0 ||
                                  strcmp(argv[1],"--model-preview-capture")==0);
    bool model_preview_capture=argc>1 && strcmp(argv[1],"--model-preview-capture")==0;
    if(model_preview_mode && argc!=2) {
        fputs("Usage: omf3d_prototype --model-preview | --model-preview-capture\n",stderr);
        return 1;
    }
    story_mode=argc>1 && strcmp(argv[1],"--story")==0;
    const char *story_path=NULL,*story_script=NULL,*story_shot_path=NULL,*story_save_file=NULL,*story_arg_har=NULL;
    bool story_new=false;
    if(story_mode) {
        bool good=argc>=3;
        for(int i=3;good && i<argc;) {
            if(strcmp(argv[i],"--new")==0) { story_new=true; i++; continue; }
            if(strcmp(argv[i],"--debug-fights")==0) { story_debug_fights=true; i++; continue; }
            if(strcmp(argv[i],"--mute")==0) { story_muted=true; i++; continue; }
            if(i+1>=argc) { good=false; break; }
            if(strcmp(argv[i],"--scene")==0) story_start_scene=argv[i+1];
            else if(strcmp(argv[i],"--script")==0) story_script=argv[i+1];
            else if(strcmp(argv[i],"--shot")==0) story_shot_path=argv[i+1];
            else if(strcmp(argv[i],"--save-file")==0) story_save_file=argv[i+1];
            else if(strcmp(argv[i],"--har")==0) story_arg_har=argv[i+1];
            else if(strcmp(argv[i],"--typed")==0) story_shot_typed=atoi(argv[i+1]);
            else good=false;
            i+=2;
        }
        if(!good) {
            fputs("Usage: omf3d_prototype --story script.story [--new] [--debug-fights] [--mute] [--save-file path] [--scene id] [--har Jaguar|Shadow]\n"
                  "                       [--script a,c1,w,...] [--shot out.bmp]\n",stderr);
            return 1;
        }
        story_path=argv[2];
        story_save_named=story_save_file!=NULL;
        if(story_save_file) snprintf(story_save_buf,sizeof(story_save_buf),"%s",story_save_file);
        story_set_script_path(story_path);
        story_save_path=story_save_buf;
        story_capturing=story_shot_path!=NULL;
    }
    bool smoke = argc>1 && strcmp(argv[1],"--smoke")==0;
    bool capture = argc>1 && strcmp(argv[1],"--capture")==0;
    bool sandbox = argc==2 && strcmp(argv[1],"--sandbox")==0;
    bool source_check = argc>1 && strcmp(argv[1],"--source-replay-check")==0;
    source_follow_mode = argc>1 && strcmp(argv[1],"--source-live")==0;
    if(source_follow_mode) {
        source_live_pilot_name = getenv("OMF3K_LIVE_PILOT_NAME");
        source_live_rival_name = getenv("OMF3K_LIVE_RIVAL_NAME");
    }
    source_replay_mode = source_follow_mode || (argc>1 && strcmp(argv[1],"--source-replay")==0);
    if(!selection_mode && !story_mode && !model_preview_mode && !smoke && !capture && !sandbox && !source_check && !source_replay_mode) {
        // Real fights come from OpenOMF (the original-game engine). The built-in combat
        // loop is a provisional placeholder kept only for rendering and self-tests.
        fputs("OMF2115 fights run on the OpenOMF engine. Start one with:\n"
              "  powershell -ExecutionPolicy Bypass -File project/scripts/run-blockout-jaguar.ps1\n"
              "Other modes: --source-live trace.csv | --source-replay trace.csv | --source-replay-check trace.csv\n"
              "             --model-preview | --select selection.txt | --story script.story | --self-test | --sandbox (provisional non-OMF combat)\n",stderr);
        return 1;
    }
    bool source_capture = false;
    const char *capture_tick_arg = NULL;
    bool bad_source_args = !selection_mode && source_replay_mode && (argc < 3 || argc % 2 == 0);
    if(source_replay_mode && !bad_source_args) {
        for(int i=3; i<argc; i+=2) {
            if(strcmp(argv[i],"--capture-tick")==0 && !source_capture) {
                source_capture=true;
                capture_tick_arg=argv[i+1];
            } else if(strcmp(argv[i],"--input-file")==0 && source_follow_mode && !source_input_path) {
                source_input_path=argv[i+1];
            } else if(strcmp(argv[i],"--result-file")==0 && source_follow_mode && !live_result_path) {
                live_result_path=argv[i+1];
            } else {
                bad_source_args=true;
            }
        }
    }
    if(!selection_mode && ((source_check && argc!=3) || bad_source_args)) {
        fputs("Usage: omf3d_prototype --source-replay-check trace.csv | --source-replay trace.csv [--capture-tick N] | --source-live trace.csv [--input-file input.txt] [--capture-tick N]\n",stderr);
        return 1;
    }
    source_input_enabled=source_input_path!=NULL;
#ifdef _WIN32
    const char *source_input_map_name=source_follow_mode ? getenv("OMF3K_INPUT_MAP") : NULL;
    if(source_input_map_name && *source_input_map_name) source_input_enabled=true;
    source_state_map_name=source_follow_mode ? getenv("OMF3K_STATE_MAP") : NULL;
#endif
    if(source_check || (source_replay_mode && !source_follow_mode)) {
        char error[256];
        if(!source_replay_load(argv[2],&source_replay,error,sizeof(error))) {
            fprintf(stderr,"%s\n",error);
            return 1;
        }
        if(source_check) {
            printf("Source replay OK: %zu frames, ticks %u..%u, HARs %d and %d\n",source_replay.count,
                   source_replay.frames[0].tick,source_replay.frames[source_replay.count-1].tick,
                   source_replay.frames[0].fighter[0].har,source_replay.frames[0].fighter[1].har);
            source_replay_free(&source_replay);
            return 0;
        }
    }
    if(story_mode) {
        char error[256];
        if(!story_load(&story_data,story_path,error,sizeof(error))) { fprintf(stderr,"%s\n",error); return 1; }
        if(!story_start(&story_run,&story_data,story_start_scene)) {
            fprintf(stderr,"Unknown scene: %s\n",story_start_scene);
            story_free(&story_data);
            return 1;
        }
        // Scripted and screenshot runs are tests: they neither resume nor overwrite the player's save,
        // unless a save file is named explicitly.
        story_save_enabled=story_save_file || (!story_shot_path && !story_script);
        // With two routes, resume the one saved most recently.
        if(story_save_enabled && !story_new && !story_save_named && story_data.has_route) {
            char route[512],route_save[512];
            struct stat mine,theirs;
            story_route_path(story_script_path,&story_data,route,sizeof(route));
            story_save_path_for(route,route_save,sizeof(route_save));
            if(stat(route_save,&theirs)==0 && (stat(story_save_path,&mine)!=0 || theirs.st_mtime>mine.st_mtime)) {
                if(story_switch_route()) story_start(&story_run,&story_data,story_start_scene);
            }
        }
        bool story_resumed=false;
        if(story_save_enabled && !story_new && story_save_exists(story_save_path)) {
            StoryRun restored;
            if(story_load_save(&restored,&story_data,story_save_path,error,sizeof(error))) {
                story_run=restored;
                story_resumed=true;
                story_notify("RESUMED FROM SAVE  R RESTARTS");
            } else {
                fprintf(stderr,"Save ignored: %s\n",error);
                story_notify("SAVE IGNORED  STARTING OVER");
            }
        }
        if(story_data.has_cast) {
            story_load_cast_portraits();
            if(story_arg_har && strcmp(story_arg_har,"Jaguar") && strcmp(story_arg_har,"Shadow")) {
                fprintf(stderr,"--har must be Jaguar or Shadow\n");
                story_free(&story_data);
                return 1;
            }
            if(!story_resumed) {
                if(story_arg_har || story_script) {
                    story_begin(story_arg_har ? story_arg_har[0]=='S' : story_setup_har);
                } else {
                    memset(&story_run,0,sizeof(story_run));
                    story_setup=true;
                }
            }
        }
        if(story_script) story_run_script(story_script);
    }
    uint32_t capture_tick=0;
    if(source_capture) {
        char *end;
        unsigned long tick_value=strtoul(capture_tick_arg,&end,10);
        if(!capture_tick_arg[0] || *end || tick_value>UINT32_MAX ||
           (!source_follow_mode &&
            (source_replay_index=source_replay_find_tick(&source_replay,(uint32_t)tick_value))==source_replay.count)) {
            fprintf(stderr,"Invalid or unavailable source tick: %s\n",capture_tick_arg);
            source_replay_free(&source_replay);
            return 1;
        }
        capture_tick=(uint32_t)tick_value;
        if(!source_follow_mode) source_replay_paused=true;
    }
    SDL_SetMainReady();
    if(SDL_Init(SDL_INIT_VIDEO|SDL_INIT_EVENTS)!=0) { fprintf(stderr,"SDL: %s\n",SDL_GetError()); return 1; }
    if(story_mode && !story_shot_path) story_audio_init();
#ifdef _WIN32
    if(source_input_map_name && *source_input_map_name) {
        source_input_mapping=CreateFileMappingA(INVALID_HANDLE_VALUE,NULL,PAGE_READWRITE,0,
                                                sizeof(Omf3kLiveInput),source_input_map_name);
        if(source_input_mapping) source_shared_input=MapViewOfFile(source_input_mapping,FILE_MAP_ALL_ACCESS,0,0,
                                                                   sizeof(Omf3kLiveInput));
        if(!source_shared_input) {
            fprintf(stderr,"Cannot create live input channel\n");
            if(source_input_mapping) CloseHandle(source_input_mapping);
            SDL_Quit();
            return 1;
        }
    }
#endif
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION,3);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION,3);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK,SDL_GL_CONTEXT_PROFILE_CORE);
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE,24);
    SDL_GL_SetAttribute(SDL_GL_MULTISAMPLEBUFFERS,1);
    SDL_GL_SetAttribute(SDL_GL_MULTISAMPLESAMPLES,4);
    SDL_Window *window=SDL_CreateWindow("OMF2115 / PROTOTYPE",SDL_WINDOWPOS_CENTERED,SDL_WINDOWPOS_CENTERED,
                                       WIDTH,HEIGHT,SDL_WINDOW_OPENGL|SDL_WINDOW_RESIZABLE|
                                       ((smoke || capture || source_capture || model_preview_capture || story_shot_path) ? SDL_WINDOW_HIDDEN : SDL_WINDOW_SHOWN));
    if(!window) { fprintf(stderr,"Window: %s\n",SDL_GetError()); SDL_Quit(); return 1; }
    SDL_GLContext context=SDL_GL_CreateContext(window);
    if(!context) { fprintf(stderr,"OpenGL: %s\n",SDL_GetError()); SDL_DestroyWindow(window); SDL_Quit(); return 1; }
    // Live mode has its own 60 Hz pacing below. Driver vsync can block a
    // hidden or hybrid-GPU window for hundreds of milliseconds.
    SDL_GL_SetSwapInterval(source_follow_mode || model_preview_capture ? 0 : 1);
    const char *vs="#version 330 core\nlayout(location=0) in vec3 p;layout(location=1) in vec3 c;out vec3 color;void main(){gl_Position=vec4(p,1);color=c;}";
    const char *fs="#version 330 core\nin vec3 color;out vec4 outColor;void main(){outColor=vec4(color,1);}";
    GLuint v=make_shader(GL_VERTEX_SHADER,vs), f=make_shader(GL_FRAGMENT_SHADER,fs), program=glCreateProgram();
    glAttachShader(program,v); glAttachShader(program,f); glLinkProgram(program);
    GLint linked=0; glGetProgramiv(program,GL_LINK_STATUS,&linked);
    if(!linked) { fprintf(stderr,"OpenGL program link failed\n"); return 1; }
    glDeleteShader(v); glDeleteShader(f);
    GLuint vao,vbo; glGenVertexArrays(1,&vao); glGenBuffers(1,&vbo);
    glBindVertexArray(vao); glBindBuffer(GL_ARRAY_BUFFER,vbo);
    glBufferData(GL_ARRAY_BUFFER,sizeof(vertices),NULL,GL_STREAM_DRAW);
    glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,sizeof(Vertex),(void*)0); glEnableVertexAttribArray(0);
    glVertexAttribPointer(1,3,GL_FLOAT,GL_FALSE,sizeof(Vertex),(void*)(3*sizeof(float))); glEnableVertexAttribArray(1);
    if(story_mode) story_tex_init(program,vao);
    glUseProgram(program); glEnable(GL_DEPTH_TEST); glDepthFunc(GL_LESS);
    reset_fight();
    if(selection_mode) phase=1;
    else if(story_mode) phase=1;
    else if(model_preview_mode) phase=1;
    else if(source_follow_mode) phase=0;
    else if(source_replay_mode) apply_source_frame(source_replay_index);
    else phase=capture ? 1 : 0;
    bool running=true, capture_ok=true; int frames=0, model_preview_capture_index=0;
    Uint64 last=SDL_GetPerformanceCounter(); double accumulator=0;
    Uint64 live_start_ms=SDL_GetTicks64();
    bool profile_live=source_follow_mode && getenv("OMF3K_PROFILE_LIVE")!=NULL;
    if(profile_live) printf("OpenGL renderer: %s (swap interval %d)\n",
                            glGetString(GL_RENDERER),SDL_GL_GetSwapInterval());
    double max_input_ms=0,max_poll_ms=0,max_draw_ms=0,max_swap_ms=0,max_frame_ms=0,max_source_gap_ms=0;
    double max_build_ms=0,max_upload_ms=0,max_gpu_ms=0;
    unsigned int profile_frames=0,slow_frames=0,source_gaps=0,max_tick_advance=0;
    Uint64 last_source_arrival=0;
    double seek_hold=0,seek_ticks=0;   // how long LEFT/RIGHT has been held, and the fractional ticks owed
    while(running) {
        Uint64 profile_begin=SDL_GetPerformanceCounter();
        double profile_frequency=(double)SDL_GetPerformanceFrequency();
        SDL_Event e;
        while(SDL_PollEvent(&e)) {
            if(e.type==SDL_QUIT) running=false;
            if(e.type==SDL_KEYDOWN && !e.key.repeat) {
                if(selection_mode) {
                    if(e.key.keysym.scancode==SDL_SCANCODE_ESCAPE) {
                        FILE *cancel=fopen(selection_path,"w");
                        if(cancel) { fputs("cancelled\n",cancel); fclose(cancel); }
                        running=false;
                    } else if(e.key.keysym.scancode==SDL_SCANCODE_UP ||
                              e.key.keysym.scancode==SDL_SCANCODE_DOWN) {
                        selection_har=(selection_har+1)%2;
                    } else if(e.key.keysym.scancode==SDL_SCANCODE_LEFT) {
                        selection_pilot=(selection_pilot+9)%10;
                    } else if(e.key.keysym.scancode==SDL_SCANCODE_RIGHT) {
                        selection_pilot=(selection_pilot+1)%10;
                    } else if(e.key.keysym.scancode==SDL_SCANCODE_RETURN) {
                        if(!write_selection()) {
                            fprintf(stderr,"Unable to write fighter selection: %s\n",selection_path);
                            running=false;
                            capture_ok=false;
                        } else {
                            running=false;
                        }
                    }
                } else if(e.key.keysym.scancode==SDL_SCANCODE_ESCAPE) running=false;
                else if(story_mode) story_key(e.key.keysym.scancode);
                else if(model_preview_mode) {
                    if(e.key.keysym.scancode>=SDL_SCANCODE_1 && e.key.keysym.scancode<=SDL_SCANCODE_3)
                        model_preview_view=e.key.keysym.scancode-SDL_SCANCODE_1;
                    if(e.key.keysym.scancode==SDL_SCANCODE_0) model_preview_pose=0;
                    if(e.key.keysym.scancode>=SDL_SCANCODE_4 && e.key.keysym.scancode<=SDL_SCANCODE_7)
                        model_preview_pose=e.key.keysym.scancode-SDL_SCANCODE_4+1;
                    if(e.key.keysym.scancode==SDL_SCANCODE_8) model_preview_pose=5;
                    if(e.key.keysym.scancode==SDL_SCANCODE_9) model_preview_pose=6;
                    if(e.key.keysym.scancode==SDL_SCANCODE_H) model_preview_pose=7;
                    if(e.key.keysym.scancode==SDL_SCANCODE_M) model_preview_pose=8;
                } else if(source_follow_mode && live_result_path) {
                    if(live_result_written && (e.key.keysym.scancode==SDL_SCANCODE_RETURN ||
                                               e.key.keysym.scancode==SDL_SCANCODE_SPACE)) live_result_timer=0;
                } else if(source_follow_mode) {
                    if(source_live_winner >= 0) {
                        if(e.key.keysym.scancode==SDL_SCANCODE_LEFT || e.key.keysym.scancode==SDL_SCANCODE_A)
                            try_again_choice=0;
                        else if(e.key.keysym.scancode==SDL_SCANCODE_RIGHT || e.key.keysym.scancode==SDL_SCANCODE_D)
                            try_again_choice=1;
                        else if(e.key.keysym.scancode==SDL_SCANCODE_Y) request_live_restart();
                        else if(e.key.keysym.scancode==SDL_SCANCODE_N) running=false;
                        else if(e.key.keysym.scancode==SDL_SCANCODE_RETURN) {
                            if(try_again_choice==0) request_live_restart();
                            else running=false;
                        }
                    }
                } else if(source_replay_mode) {
                    if(e.key.keysym.scancode==SDL_SCANCODE_SPACE) {
                        source_replay_paused=!source_replay_paused;
                        accumulator=0;
                    }
                    if(e.key.keysym.scancode==SDL_SCANCODE_R) {
                        apply_source_frame(0);
                        source_replay_paused=false;
                        accumulator=0;
                    }
                    if(source_replay_paused && e.key.keysym.scancode==SDL_SCANCODE_RIGHT &&
                       source_replay_index+1<source_replay.count) apply_source_frame(source_replay_index+1);
                    if(source_replay_paused && e.key.keysym.scancode==SDL_SCANCODE_LEFT && source_replay_index>0)
                        apply_source_frame(source_replay_index-1);
                } else if(phase==2 || phase==3) {
                    if(e.key.keysym.scancode==SDL_SCANCODE_LEFT || e.key.keysym.scancode==SDL_SCANCODE_A)
                        try_again_choice=0;
                    if(e.key.keysym.scancode==SDL_SCANCODE_RIGHT || e.key.keysym.scancode==SDL_SCANCODE_D)
                        try_again_choice=1;
                    if(e.key.keysym.scancode==SDL_SCANCODE_Y) reset_fight();
                    if(e.key.keysym.scancode==SDL_SCANCODE_N) running=false;
                    if(e.key.keysym.scancode==SDL_SCANCODE_RETURN) {
                        if(try_again_choice==0) reset_fight();
                        else running=false;
                    }
                } else if(e.key.keysym.scancode==SDL_SCANCODE_RETURN && phase==0) reset_fight();
            }
        }
        if(source_follow_mode && source_replay.count)
            write_source_input(source_live_winner >= 0 ? NULL : SDL_GetKeyboardState(NULL));
        Uint64 profile_after_input=SDL_GetPerformanceCounter();
        Uint64 now=SDL_GetPerformanceCounter();
        double frame=(double)(now-last)/(double)SDL_GetPerformanceFrequency(); last=now;
        if(source_replay_mode) {
            float visual_step=(float)fmin(frame,.10);
            if(source_follow_mode) source_visual_time+=visual_step;
            live_impact_time=fmaxf(0,live_impact_time-visual_step);
            live_round_intro_time=fmaxf(0,live_round_intro_time-visual_step);
        }
        if(story_mode) story_match_poll();
        if(selection_mode || story_mode) {
            // The selection and story screens wait for input and do not advance a fight.
        } else if(source_follow_mode) {
            char error[256];
            size_t old_count=source_replay.count;
            int follow_result;
#ifdef _WIN32
            if(source_state_map_name && *source_state_map_name) {
                follow_result=poll_shared_source_state(error,sizeof(error));
            } else
#endif
            {
                follow_result=source_replay_follow_poll(argv[2],&source_replay,&source_follow,error,sizeof(error));
            }
            if(follow_result<0) {
                fprintf(stderr,"%s\n",error);
                running=false;
                capture_ok=false;
            } else if(follow_result>0) {
                apply_source_frame(source_replay.count-1);
                if(!old_count) live_round_intro_time=1.5f;
                source_follow_arrival=now;
                if(profile_live) {
                    unsigned int advance=(unsigned int)(source_replay.count-old_count);
                    if(advance>max_tick_advance) max_tick_advance=advance;
                    if(last_source_arrival) {
                        double gap=(now-last_source_arrival)*1000.0/profile_frequency;
                        if(gap>max_source_gap_ms) max_source_gap_ms=gap;
                        if(gap>60) {
                            source_gaps++;
                            const SourceFrame *latest=&source_replay.frames[source_replay.count-1];
                            printf("Source gap: tick=%u duration=%.1fms health=%d/%d animation=%d/%d\n",
                                   latest->tick,gap,latest->fighter[0].health,latest->fighter[1].health,
                                   latest->fighter[0].animation,latest->fighter[1].animation);
                        }
                    }
                    last_source_arrival=now;
                }
            }
#ifdef _WIN32
            if(source_state_map_name && *source_state_map_name && !source_replay.count &&
               SDL_GetTicks64()-live_start_ms>10000) {
                fputs("Timed out waiting for OpenOMF live state\n",stderr);
                running=false;
                capture_ok=false;
            }
#endif
        } else if(model_preview_mode) {
            // A fixed inspection pose must not advance the fight simulation.
        } else if(source_replay_mode) {
            // A tap steps one tick while paused (key-down handler above). Holding LEFT or RIGHT past a short
            // delay seeks, paused or playing, and speeds up the longer it is held.
            const unsigned char *seek_keys=SDL_GetKeyboardState(NULL);
            int seek_dir=(seek_keys[SDL_SCANCODE_RIGHT]?1:0)-(seek_keys[SDL_SCANCODE_LEFT]?1:0);
            bool seeking=false;
            if(seek_dir) {
                seek_hold+=frame>.25 ? .25 : frame;
                if(seek_hold>.25) {
                    seeking=true;
                    double ramp=(seek_hold-.25)/1.5;
                    seek_ticks+=(frame>.25 ? .25 : frame)*(40.0+200.0*(ramp>1 ? 1 : ramp));
                    while(seek_ticks>=1) {
                        seek_ticks-=1;
                        if(seek_dir>0 && source_replay_index+1<source_replay.count) apply_source_frame(source_replay_index+1);
                        else if(seek_dir<0 && source_replay_index>0) apply_source_frame(source_replay_index-1);
                    }
                    accumulator=0;
                }
            } else {
                seek_hold=0;
                seek_ticks=0;
            }
            if(!source_replay_paused && !seeking) {
                accumulator+=frame>.25 ? .25 : frame;
                while(accumulator>=source_tick_seconds && !source_replay_paused) {
                    accumulator-=source_tick_seconds;
                    if(source_replay_index+1<source_replay.count) apply_source_frame(source_replay_index+1);
                    else source_replay_paused=true;
                }
            }
        } else {
            accumulator+=frame>.25 ? .25 : frame;
            const unsigned char *keys=SDL_GetKeyboardState(NULL);
            while(accumulator>=DT) { tick(keys); accumulator-=DT; }
        }
        Uint64 profile_after_poll=SDL_GetPerformanceCounter();
        if(source_follow_mode && live_result_path && source_live_winner>=0 && source_replay.count) {
            if(!live_result_written) {
                const SourceFrame *last=&source_replay.frames[source_replay_index];
                FILE *result=fopen(live_result_path,"w");
                if(result) {
                    fprintf(result,"winner=%d\nhealth=%d\n",source_live_winner,(int)last->fighter[source_live_winner].health);
                    fclose(result);
                    printf("Match decided at tick %u: winner=%d health=%d\n",last->tick,source_live_winner,
                           (int)last->fighter[source_live_winner].health);
                    fflush(stdout);
                } else {
                    fprintf(stderr,"Could not write the result file: %s\n",live_result_path);
                    capture_ok=false;
                }
                live_result_written=true;
                live_result_timer=3.5;
            }
            live_result_timer-=frame>.25 ? .25 : frame;
            if(live_result_timer<=0) running=false;
        }
        interpolate_live_fighters(now,source_capture && source_replay.count &&
                                  source_replay.frames[source_replay_index].tick>=capture_tick);
        if((source_replay_mode || source_follow_mode) && source_replay.count)
            smooth_source_facing(frame>.25 ? .25 : frame,source_capture);
        SDL_GetWindowSize(window,&win_width,&win_height);
        if(win_height<1) win_height=1;
        glViewport(0,0,win_width,win_height);
        glClearColor(.015f,.025f,.065f,1); glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
        vertex_count=0;
        int world_count;
        if(selection_mode) {
            selection_hud();
            world_count=0;
        } else if(story_mode) {
            story_hud();
            world_count=0;
        } else {
            world();
            world_count=vertex_count;
            hud();
        }
        Uint64 profile_after_build=SDL_GetPerformanceCounter();
        // Give each upload fresh storage, avoiding waits on the prior draw.
        glBindBuffer(GL_ARRAY_BUFFER,vbo);
        glBufferData(GL_ARRAY_BUFFER,sizeof(vertices),NULL,GL_STREAM_DRAW);
        glBufferSubData(GL_ARRAY_BUFFER,0,(size_t)vertex_count*sizeof(Vertex),vertices);
        Uint64 profile_after_upload=SDL_GetPerformanceCounter();
        glEnable(GL_DEPTH_TEST); glDrawArrays(GL_TRIANGLES,0,world_count);
        glDisable(GL_DEPTH_TEST);
        int split=story_mode && story_tex_draw.active ? story_tex_draw.split : world_count;
        glDrawArrays(GL_TRIANGLES,world_count,split-world_count);
        if(story_mode) story_tex_flush();
        glDrawArrays(GL_TRIANGLES,split,vertex_count-split);
        Uint64 profile_after_gpu=SDL_GetPerformanceCounter();
        bool capture_now=capture || story_shot_path || (source_capture && (!source_follow_mode ||
                         (source_replay.count && source_replay.frames[source_replay_index].tick>=capture_tick)));
        if(model_preview_capture) {
            const char *paths[]={"project/build/omf3d_model_side.bmp","project/build/omf3d_model_front.bmp",
                                 "project/build/omf3d_model_back.bmp","project/build/omf3d_model_punch.bmp",
                                 "project/build/omf3d_model_kick.bmp","project/build/omf3d_model_guard.bmp",
                                 "project/build/omf3d_model_crouch.bmp","project/build/omf3d_model_walk.bmp",
                                 "project/build/omf3d_model_jump.bmp","project/build/omf3d_model_hit.bmp",
                                 "project/build/omf3d_model_special.bmp"};
            capture_ok=save_frame_bmp(paths[model_preview_capture_index]);
            if(!capture_ok) fprintf(stderr,"Could not save %s: %s\n",
                                    paths[model_preview_capture_index],SDL_GetError());
        } else if(capture_now) {
            const char *path=story_shot_path ? story_shot_path :
                             source_capture ? "project/build/omf3d_source_replay_capture.bmp" : "project/build/omf3d_sideon_capture.bmp";
            capture_ok=save_frame_bmp(path);
            if(!capture_ok) fprintf(stderr,"Could not save %s: %s\n",path,SDL_GetError());
        }
        Uint64 profile_after_draw=SDL_GetPerformanceCounter();
        // Hidden batch captures read the back buffer directly. Swapping the
        // hidden window between views can invalidate its surface on Windows.
        if(!model_preview_capture) SDL_GL_SwapWindow(window);
        Uint64 profile_after_swap=SDL_GetPerformanceCounter();
        if(profile_live && !capture_now) {
            double input_ms=(profile_after_input-profile_begin)*1000.0/profile_frequency;
            double poll_ms=(profile_after_poll-profile_after_input)*1000.0/profile_frequency;
            double draw_ms=(profile_after_draw-profile_after_poll)*1000.0/profile_frequency;
            double build_ms=(profile_after_build-profile_after_poll)*1000.0/profile_frequency;
            double upload_ms=(profile_after_upload-profile_after_build)*1000.0/profile_frequency;
            double gpu_ms=(profile_after_gpu-profile_after_upload)*1000.0/profile_frequency;
            double swap_ms=(profile_after_swap-profile_after_draw)*1000.0/profile_frequency;
            double frame_ms=(profile_after_swap-profile_begin)*1000.0/profile_frequency;
            if(input_ms>max_input_ms) max_input_ms=input_ms;
            if(poll_ms>max_poll_ms) max_poll_ms=poll_ms;
            if(draw_ms>max_draw_ms) max_draw_ms=draw_ms;
            if(build_ms>max_build_ms) max_build_ms=build_ms;
            if(upload_ms>max_upload_ms) max_upload_ms=upload_ms;
            if(gpu_ms>max_gpu_ms) max_gpu_ms=gpu_ms;
            if(swap_ms>max_swap_ms) max_swap_ms=swap_ms;
            if(frame_ms>max_frame_ms) max_frame_ms=frame_ms;
            if(frame_ms>25) {
                slow_frames++;
                printf("Slow live frame: tick=%u total=%.1fms input=%.1f poll=%.1f draw=%.1f build=%.1f upload=%.1f gpu=%.1f swap=%.1f vertices=%d\n",
                       source_replay.count ? source_replay.frames[source_replay_index].tick : 0,
                       frame_ms,input_ms,poll_ms,draw_ms,build_ms,upload_ms,gpu_ms,swap_ms,vertex_count);
            }
            profile_frames++;
        }
        if(source_follow_mode && !capture_now) {
            double draw_seconds=(double)(SDL_GetPerformanceCounter()-now)/(double)SDL_GetPerformanceFrequency();
            if(draw_seconds<DT-.001) SDL_Delay((Uint32)((DT-draw_seconds)*1000));
        }
        if(model_preview_capture) {
            if(!capture_ok || ++model_preview_capture_index>=11) running=false;
            else if(model_preview_capture_index<3) model_preview_view=model_preview_capture_index;
            else {
                model_preview_view=0;
                model_preview_pose=model_preview_capture_index-2;
            }
        } else if((smoke && ++frames >= 10) || capture_now) running=false;
    }
    write_source_input(NULL);
    glDeleteBuffers(1,&vbo); glDeleteVertexArrays(1,&vao); glDeleteProgram(program);
    SDL_GL_DeleteContext(context); SDL_DestroyWindow(window); SDL_Quit();
#ifdef _WIN32
    if(source_shared_input) UnmapViewOfFile(source_shared_input);
    if(source_input_mapping) CloseHandle(source_input_mapping);
    if(source_shared_state) UnmapViewOfFile(source_shared_state);
    if(source_state_mapping) CloseHandle(source_state_mapping);
#endif
    source_replay_follow_close(&source_follow);
    source_replay_free(&source_replay);
    story_free(&story_data);
    if(profile_live) printf("Live timing: frames=%u slow=%u max_frame=%.1fms input=%.1fms poll=%.1fms draw=%.1fms build=%.1fms upload=%.1fms gpu=%.1fms swap=%.1fms source_gaps=%u max_gap=%.1fms max_tick_advance=%u\n",
                            profile_frames,slow_frames,max_frame_ms,max_input_ms,max_poll_ms,max_draw_ms,
                            max_build_ms,max_upload_ms,max_gpu_ms,max_swap_ms,source_gaps,max_source_gap_ms,max_tick_advance);
    if(smoke) puts("3D prototype OpenGL smoke check OK");
    if(capture && capture_ok) puts("Saved project/build/omf3d_sideon_capture.bmp");
    if(source_capture && capture_ok) puts("Saved project/build/omf3d_source_replay_capture.bmp");
    if(story_shot_path && capture_ok) printf("Saved %s\n",story_shot_path);
    if(model_preview_capture && capture_ok)
        puts("Saved project/build/omf3d_model_{side,front,back,punch,kick,guard,crouch,walk,jump,hit,special}.bmp");
    return capture_ok ? 0 : 1;
}
