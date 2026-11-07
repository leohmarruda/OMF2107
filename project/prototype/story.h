// Story scene scripts for the OMF2107 prototype: a small line-based format, a validator, and a runner.
// Pure C with no SDL or OpenGL, so it can be tested headlessly and integrated elsewhere later.
//
// Script format (one command per line, '#' starts a comment line, indentation is ignored):
//   scene <id>                          starts a scene; the first scene is where a run begins
//   bg <name>                           names the background (for the viewer; free text)
//   art <name> [effect]                 shows a full-width illustration; effect is none, fade, zoom, or pan;
//                                       the name may contain {flag}; "art off" returns to the background
//   music <track>                       background music: menu, arena0 to arena4, end, or off (the original
//                                       game's tracks; the viewer plays them from OMF2097/ when it can)
//   present <image> <left|right> [name] a character portrait slides in from that side over the current picture, which
//                                       is blurred a little. Two characters can be shown, one on each side, so a
//                                       conversation shows both; a new present replaces that side's portrait. The name
//                                       slides in from the portrait's own side and out again when the line after the first one
//                                       appears, and only the first time that portrait is ever shown.
//                                       <image> is project/build/art/<image>_cut.bmp (a 32-bit cut-out). Leave the
//                                       name out to show the portrait alone; "present off" removes both
//   flash                               a quick white flash over the picture (a presentation beat; does not wait)
//   banner <text>                       a big banner across the picture for a moment (does not wait)
//   say <speaker>: <text>               one line of dialogue; an empty speaker (say : text) is narration
//   choice <text> -> <scene> [set f=v]  a menu entry; consecutive choice lines form one menu
//   set <flag>=<value>                  stores a flag
//   if <flag>=<value> -> <scene>        jumps when the flag has that value, otherwise continues
//   jump <scene>                        continues in another scene
//   fight <pilot> <har> vs <pilot> <har> win -> <scene> lose -> <scene> [difficulty <0-6>]
//                                       hands off to a match; the host reports the result. difficulty is the
//                                       rival's AI level (0 punching bag to 6 ultimate); left out, the game's setting
//   end                                 finishes the story
// Header directives (before the first scene) describe who is playing, for a selection screen:
//   player <pilot> <har>                the pilot the player controls and the HAR the story recommends
//   rival <pilot>                       the AI opponent's pilot
//   card <pilot>: <text>                context shown for that pilot on the selection screen
//   blurb <text>                        a short premise shown on the selection screen
//   opponents <pilot>, <pilot>, ...     the faces the route meets, shown on the selection screen in place of a
//                                       single rival (up to 8; the rival line is still what @rival_har and
//                                       {rival_pilot} refer to)
//   route <pilot> <script>              another script the player can pick instead, written from that pilot's
//                                       side (a path relative to this script); at most one per script, and each
//                                       script of a pair names the other
// A fight's HAR may be written @flag, taking the HAR from a flag when the match is reached, and say text may
// contain {flag}, replaced by that flag's value (left as written when the flag is unset).
// Every scene must finish with jump, end, fight, or a choice menu; nothing may follow those.
#ifndef OMF2107_STORY_H
#define OMF2107_STORY_H

#include <stdbool.h>
#include <stddef.h>

#define STORY_NAME 32
#define STORY_TEXT 256
#define STORY_MAX_CHOICES 6
#define STORY_MAX_FLAGS 32
#define STORY_LOG 64

typedef enum {
    STORY_CMD_NONE = 0,       // keeps zero-initialised commands invalid
    STORY_CMD_BG,
    STORY_CMD_ART,
    STORY_CMD_MUSIC,
    STORY_CMD_FLASH,
    STORY_CMD_BANNER,
    STORY_CMD_PRESENT,
    STORY_CMD_SAY,
    STORY_CMD_CHOICE,
    STORY_CMD_SET,
    STORY_CMD_IF,
    STORY_CMD_JUMP,
    STORY_CMD_FIGHT,
    STORY_CMD_END
} StoryCmdKind;

typedef struct {
    StoryCmdKind kind;
    int line;                       // line in the script, for messages
    char speaker[STORY_NAME];       // say
    char text[STORY_TEXT];          // say and choice text; bg name; art name
    char flag[STORY_NAME];          // set, if, and choice-set
    char value[STORY_NAME];
    bool has_set;                   // choice: also sets flag=value
    char target_name[STORY_NAME];   // jump, if, choice, fight win
    char target2_name[STORY_NAME];  // fight lose
    int target, target2;            // resolved scene indices
    char pilot[2][STORY_NAME];      // fight
    char har[2][STORY_NAME];
    int difficulty;                 // fight: the rival's AI level 0-6, or -1 for the game's own setting
} StoryCmd;

typedef struct {
    char id[STORY_NAME];
    int first, count;               // commands of this scene
    int line;
} StoryScene;

#define STORY_MAX_CARDS 4
#define STORY_MAX_OPPONENTS 8

typedef struct { char pilot[STORY_NAME]; char text[STORY_TEXT]; } StoryCard;
typedef struct { char pilot[STORY_NAME]; char path[256]; } StoryRoute;

typedef struct {
    StoryScene *scenes;
    int scene_count;
    StoryCmd *cmds;
    int cmd_count;
    bool has_cast;                   // the script declared a player and a rival
    char player_pilot[STORY_NAME];
    char player_har[STORY_NAME];     // the HAR the story recommends for the player
    char rival_pilot[STORY_NAME];
    StoryCard cards[STORY_MAX_CARDS];
    int card_count;
    char blurb[STORY_TEXT];          // the selection screen's premise line; empty for none
    int opponent_count;              // the pilots listed by opponents, in order
    char opponents[STORY_MAX_OPPONENTS][STORY_NAME];
    bool has_route;                  // the script offers another pilot's script (see route)
    StoryRoute route;
} Story;

// Parses and validates script text. On failure returns false and writes "name:line: message" to err.
bool story_parse(Story *story, const char *text, const char *name, char *err, size_t err_size);
bool story_load(Story *story, const char *path, char *err, size_t err_size);
void story_free(Story *story);
// Scenes that cannot be reached from the first scene; returns how many were written to out.
int story_unreachable(const Story *story, int *out, int max);
int story_find_scene(const Story *story, const char *id);

typedef enum { STORY_EVENT_SAY, STORY_EVENT_CHOICE, STORY_EVENT_FIGHT, STORY_EVENT_END } StoryEventKind;

#define STORY_NAME_SEEN 40
typedef struct {
    char image[STORY_NAME];         // the portrait on this side; empty for none
    char name[STORY_NAME];          // the name plate's text; empty for none (a plate shows only the first time a portrait appears)
    int stage;                      // 0 none; 1 name just introduced; 2 name shown with its first line; 3 name gone
} StoryPresent;
typedef struct { char name[STORY_NAME]; char value[STORY_NAME]; } StoryFlag;
typedef struct { char speaker[STORY_NAME]; char text[STORY_TEXT]; } StoryLogEntry;

// The whole run state is plain data (scene, command index, flags, log) so it can be saved later.
typedef struct {
    const Story *story;
    int scene, pc;                  // current scene and command index within it
    StoryEventKind event;           // what the host should show or do now
    int choice_first, choice_count; // for STORY_EVENT_CHOICE: commands (within the scene) of the menu
    char bg[STORY_NAME];
    char art[STORY_NAME];           // the current illustration with {flag} placeholders replaced; empty for none
    char art_effect[STORY_NAME];    // none, fade, zoom, or pan
    char music[STORY_NAME];         // the track now playing (menu, arena0..arena4, end); empty for none
    int flag_count;
    StoryFlag flags[STORY_MAX_FLAGS];
    char say_text[STORY_TEXT];      // the current say line with {flag} placeholders replaced
    unsigned effect_serial;         // counts flash and banner beats; the host plays one when this changes
    char effect_kind[16];           // "flash" or "banner"
    char effect_text[STORY_NAME];   // the banner's text (not saved: effects are momentary)
    StoryPresent present[2];        // the portraits now shown (see present): [0] stands on the left, [1] on the right
    char name_seen[STORY_NAME_SEEN][STORY_NAME];   // the portraits whose name plate has already been shown; a plate shows once
    int name_seen_count;
    int log_total;                  // entries ever logged; the last STORY_LOG are kept
    StoryLogEntry log[STORY_LOG];
} StoryRun;

// Starts at the given scene (NULL for the first) and runs to the first event. False if the scene is unknown.
bool story_start(StoryRun *run, const Story *story, const char *scene_id);
// The same, with flags set before the first line runs (for example the HARs chosen on a selection screen).
bool story_start_with_flags(StoryRun *run, const Story *story, const char *scene_id, const StoryFlag *flags, int count);
// The HAR for one side (0 or 1) of a fight command, resolving @flag. False when it is unset or not a known HAR.
bool story_fight_har(const StoryRun *run, const StoryCmd *fight, int side, char *out, size_t out_size);
const char *story_say_text(const StoryRun *run);                   // the current say line, placeholders replaced
const char *story_card_text(const Story *story, const char *pilot); // "" when the script has no card for the pilot
const StoryCmd *story_event_cmd(const StoryRun *run);              // the say or fight command now shown
const StoryCmd *story_choice_cmd(const StoryRun *run, int index);  // a menu entry
void story_advance(StoryRun *run);                                 // after a say event
bool story_choose(StoryRun *run, int index);                       // after a choice event
bool story_fight_result(StoryRun *run, bool win);                  // after a fight event
int story_skip(StoryRun *run);                                     // skips say lines up to the next choice, fight, or end
const char *story_flag(const StoryRun *run, const char *name);     // "" when unset
void story_note(StoryRun *run, const char *text);                   // adds a "DEBUG" entry to the log
void story_record(StoryRun *run, const char *speaker, const char *text);  // adds an entry to the log
int story_log_count(const StoryRun *run);
const StoryLogEntry *story_log_at(const StoryRun *run, int index); // 0 is the oldest kept entry

// ---- save data ----
// A save is a small versioned text file holding the stopping point (scene id and command), flags, and log.
// It records a fingerprint of the script, so a save made against an edited script is refused, not misread.
#define STORY_SAVE_VERSION 1
unsigned story_fingerprint(const Story *story);
bool story_save(const StoryRun *run, const char *path, char *err, size_t err_size);
// Restores a saved run. On any failure returns false with a message and leaves *run untouched.
bool story_load_save(StoryRun *run, const Story *story, const char *path, char *err, size_t err_size);
bool story_save_exists(const char *path);

#endif
