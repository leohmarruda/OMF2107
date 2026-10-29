// Command-line checker for story scripts.
//   story_check check <script>                       validate and list unreachable scenes
//   story_check play <script> [--scene id] [--har Jaguar|Shadow] [--choices 0,1,...] [--results W,L,...]
//                                                    play a script with scripted answers and print a transcript
//   story_check selftest                             run the module's own tests
#include "story.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int failures;
#define CHECK(cond) do { if(!(cond)) { printf("FAIL line %d: %s\n", __LINE__, #cond); failures++; } } while(0)

static int cmd_check(const char *path) {
    Story story;
    char err[256];
    if(!story_load(&story, path, err, sizeof(err))) {
        fprintf(stderr, "%s\n", err);
        return 1;
    }
    printf("Story OK: %d scenes, %d commands\n", story.scene_count, story.cmd_count);
    int unreachable[64];
    int n = story_unreachable(&story, unreachable, 64);
    for(int i = 0; i < n; i++)
        printf("warning: scene '%s' (line %d) is not reachable from '%s'\n", story.scenes[unreachable[i]].id,
               story.scenes[unreachable[i]].line, story.scenes[0].id);
    story_free(&story);
    return 0;
}

// Reads the next number from a comma-separated list; returns def when the list is used up.
static int next_number(const char **list, int def) {
    if(!*list || !**list) return def;
    char *end;
    long v = strtol(*list, &end, 10);
    *list = *end == ',' ? end + 1 : end;
    return (int)v;
}

static int cmd_play(int argc, char **argv) {
    const char *path = argv[2], *scene = NULL, *choices = NULL, *results = NULL, *har = NULL;
    for(int i = 3; i + 1 < argc; i += 2) {
        if(strcmp(argv[i], "--scene") == 0) scene = argv[i + 1];
        else if(strcmp(argv[i], "--har") == 0) har = argv[i + 1];
        else if(strcmp(argv[i], "--choices") == 0) choices = argv[i + 1];
        else if(strcmp(argv[i], "--results") == 0) results = argv[i + 1];
        else { fprintf(stderr, "unknown option %s\n", argv[i]); return 2; }
    }
    Story story;
    char err[256];
    if(!story_load(&story, path, err, sizeof(err))) { fprintf(stderr, "%s\n", err); return 1; }
    StoryRun run;
    StoryFlag flags[2];
    int flag_count = 0;
    if(story.has_cast) {
        // The selection screen's job: the player's HAR (default the recommended one) and the rival's other HAR.
        const char *player_har = har ? har : story.player_har;
        const char *rival_har = strcmp(player_har, "Shadow") == 0 ? "Jaguar" : "Shadow";
        snprintf(flags[0].name, STORY_NAME, "player_har"); snprintf(flags[0].value, STORY_NAME, "%s", player_har);
        snprintf(flags[1].name, STORY_NAME, "rival_har"); snprintf(flags[1].value, STORY_NAME, "%s", rival_har);
        flag_count = 2;
        printf("[%s in %s versus %s in %s]\n", story.player_pilot, player_har, story.rival_pilot, rival_har);
    }
    if(!story_start_with_flags(&run, &story, scene, flags, flag_count)) {
        fprintf(stderr, "unknown scene '%s'\n", scene);
        story_free(&story);
        return 1;
    }
    char shown_art[STORY_NAME] = "";
    for(int guard = 0; guard < 1000; guard++) {
        const StoryCmd *c;
        if(strcmp(run.art, shown_art) != 0) {
            printf("[art: %s%s%s]\n", run.art[0] ? run.art : "off", run.art[0] ? " " : "", run.art[0] ? run.art_effect : "");
            snprintf(shown_art, sizeof(shown_art), "%s", run.art);
        }
        static char shown_music[STORY_NAME];
        if(strcmp(run.music, shown_music) != 0) {
            printf("[music: %s]\n", run.music[0] ? run.music : "off");
            snprintf(shown_music, sizeof(shown_music), "%s", run.music);
        }
        static unsigned shown_effects;
        if(run.effect_serial != shown_effects) {
            printf("[%s%s%s]\n", run.effect_kind, *run.effect_text ? ": " : "", run.effect_text);
            shown_effects = run.effect_serial;
        }
        if(run.event == STORY_EVENT_SAY) {
            c = story_event_cmd(&run);
            printf("%s%s%s\n", c->speaker, *c->speaker ? ": " : "", story_say_text(&run));
            story_advance(&run);
        } else if(run.event == STORY_EVENT_CHOICE) {
            int pick = next_number(&choices, 0);
            for(int i = 0; i < run.choice_count; i++)
                printf("  %c %d. %s\n", i == pick ? '>' : ' ', i, story_choice_cmd(&run, i)->text);
            if(!story_choose(&run, pick)) { fprintf(stderr, "choice %d is out of range\n", pick); story_free(&story); return 1; }
        } else if(run.event == STORY_EVENT_FIGHT) {
            c = story_event_cmd(&run);
            bool win = next_number(&results, 1) != 0;
            char har0[STORY_NAME], har1[STORY_NAME];
            if(!story_fight_har(&run, c, 0, har0, sizeof(har0)) || !story_fight_har(&run, c, 1, har1, sizeof(har1))) {
                fprintf(stderr, "the fight at line %d has no usable HAR (%s, %s)\n", c->line, har0, har1);
                story_free(&story);
                return 1;
            }
            printf("[FIGHT %s/%s vs %s/%s -> %s]\n", c->pilot[0], har0, c->pilot[1], har1, win ? "win" : "lose");
            story_fight_result(&run, win);
        } else {
            break;
        }
    }
    printf("[END] flags:");
    for(int i = 0; i < run.flag_count; i++) printf(" %s=%s", run.flags[i].name, run.flags[i].value);
    printf("%s\n", run.flag_count ? "" : " (none)");
    story_free(&story);
    return 0;
}

static const char *const good_script =
    "# a small branching story\n"
    "scene start\n"
    "bg stadium\n"
    "say Crystal: Hello there.\n"
    "say : A narration line.\n"
    "choice Share it -> shared set evidence=shared\n"
    "choice Keep it -> kept set evidence=kept\n"
    "scene shared\n"
    "say Crystal: Shared.\n"
    "jump match\n"
    "scene kept\n"
    "say Crystal: Kept.\n"
    "jump match\n"
    "scene match\n"
    "fight Crystal Jaguar vs Christian Shadow win -> won lose -> lost\n"
    "scene won\n"
    "if evidence=shared -> bonus\n"
    "say Narrator: Won plainly.\n"
    "end\n"
    "scene bonus\n"
    "say Narrator: Won with a bonus.\n"
    "end\n"
    "scene lost\n"
    "say Narrator: Lost.\n"
    "end\n"
    "scene orphan\n"
    "end\n";

static bool rejects(const char *script, const char *expect) {
    Story s;
    char err[256] = "";
    bool ok = story_parse(&s, script, "t", err, sizeof(err));
    if(ok) { story_free(&s); printf("  accepted but should fail: %s\n", expect); return false; }
    if(!strstr(err, expect)) { printf("  wrong error for '%s': %s\n", expect, err); return false; }
    return true;
}

// Two runs are the same stopping point: same event, position, flags, background, and log.
static bool same_run(const StoryRun *a, const StoryRun *b) {
    if(a->event != b->event || a->scene != b->scene || a->pc != b->pc || strcmp(a->bg, b->bg) != 0 ||
       a->flag_count != b->flag_count || story_log_count(a) != story_log_count(b)) return false;
    for(int i = 0; i < a->flag_count; i++)
        if(strcmp(a->flags[i].name, b->flags[i].name) != 0 || strcmp(a->flags[i].value, b->flags[i].value) != 0) return false;
    for(int i = 0; i < story_log_count(a); i++)
        if(strcmp(story_log_at(a, i)->speaker, story_log_at(b, i)->speaker) != 0 ||
           strcmp(story_log_at(a, i)->text, story_log_at(b, i)->text) != 0) return false;
    return true;
}

static void write_file(const char *path, const char *text) {
    FILE *f = fopen(path, "wb");
    if(f) { fputs(text, f); fclose(f); }
}

static void selftest_saves(const Story *story) {
    const char *path = "story_selftest.save";
    char err[256];
    StoryRun run, loaded;

    // A save taken at each kind of stopping point restores exactly, and play continues the same way.
    CHECK(story_start(&run, story, NULL));
    CHECK(story_save(&run, path, err, sizeof(err)));                       // at a say line
    CHECK(story_load_save(&loaded, story, path, err, sizeof(err)) && same_run(&run, &loaded));
    story_skip(&run);
    CHECK(story_save(&run, path, err, sizeof(err)));                       // at a choice menu
    CHECK(story_load_save(&loaded, story, path, err, sizeof(err)) && same_run(&run, &loaded));
    CHECK(loaded.event == STORY_EVENT_CHOICE && loaded.choice_count == 2);
    story_choose(&run, 0);
    story_choose(&loaded, 0);
    CHECK(same_run(&run, &loaded));
    story_skip(&run);
    CHECK(run.event == STORY_EVENT_FIGHT);
    CHECK(story_save(&run, path, err, sizeof(err)));                       // at a match
    CHECK(story_load_save(&loaded, story, path, err, sizeof(err)) && same_run(&run, &loaded));
    story_fight_result(&run, true);
    story_fight_result(&loaded, true);
    CHECK(same_run(&run, &loaded));
    story_skip(&run);
    CHECK(run.event == STORY_EVENT_END);
    CHECK(story_save(&run, path, err, sizeof(err)));                       // at the end
    CHECK(story_load_save(&loaded, story, path, err, sizeof(err)) && same_run(&run, &loaded));
    CHECK(loaded.event == STORY_EVENT_END && strcmp(story_flag(&loaded, "evidence"), "shared") == 0);

    // The restored say line is not logged a second time.
    CHECK(story_start(&run, story, NULL));
    CHECK(story_save(&run, path, err, sizeof(err)));
    CHECK(story_load_save(&loaded, story, path, err, sizeof(err)));
    CHECK(story_log_count(&loaded) == 1);

    // A failed load reports why and leaves the run untouched.
    StoryRun keep = run;
    CHECK(!story_load_save(&run, story, "story_selftest_missing.save", err, sizeof(err)) && strstr(err, "cannot open"));
    CHECK(same_run(&keep, &run));
    write_file(path, "OMF2115-STORY-SAVE 2\nscript 00000000\nscene start\npc 0\n");
    CHECK(!story_load_save(&run, story, path, err, sizeof(err)) && strstr(err, "newer build"));
    write_file(path, "OMF2115-STORY-SAVE 0\nscript 00000000\nscene start\npc 0\n");
    CHECK(!story_load_save(&run, story, path, err, sizeof(err)) && strstr(err, "old format"));
    write_file(path, "hello\n");
    CHECK(!story_load_save(&run, story, path, err, sizeof(err)) && strstr(err, "not a story save"));
    write_file(path, "OMF2115-STORY-SAVE 1\nscene start\npc 0\n");
    CHECK(!story_load_save(&run, story, path, err, sizeof(err)) && strstr(err, "missing its position"));
    write_file(path, "OMF2115-STORY-SAVE 1\nscript 12345678\nscene start\npc 0\n");
    CHECK(!story_load_save(&run, story, path, err, sizeof(err)) && strstr(err, "script changed"));
    CHECK(same_run(&keep, &run));

    // Valid fingerprint but a damaged position: build a good save, then edit it.
    CHECK(story_start(&run, story, NULL));
    CHECK(story_save(&run, path, err, sizeof(err)));
    FILE *f = fopen(path, "rb");
    char good[4096] = "";
    if(f) { size_t n = fread(good, 1, sizeof(good) - 1, f); good[n] = 0; fclose(f); }
    char bad[4096];
    char *at = strstr(good, "pc 1");   // the first say line; command 0 is the bg
    CHECK(at != NULL);
    if(at) {
        snprintf(bad, sizeof(bad), "%.*spc 99%s", (int)(at - good), good, at + 4);
        write_file(path, bad);
        CHECK(!story_load_save(&loaded, story, path, err, sizeof(err)) && strstr(err, "outside the script"));
        snprintf(bad, sizeof(bad), "%.*spc 0%s", (int)(at - good), good, at + 4);   // the bg command: not a stopping point
        write_file(path, bad);
        CHECK(!story_load_save(&loaded, story, path, err, sizeof(err)) && strstr(err, "stopping point"));
    }
    write_file(path, "OMF2115-STORY-SAVE 1\nscript 00000000\nbanana\n");
    CHECK(!story_load_save(&loaded, story, path, err, sizeof(err)) && strstr(err, "damaged"));

    // Editing the script changes its fingerprint.
    Story edited;
    char edited_text[4096];
    snprintf(edited_text, sizeof(edited_text), "%s", good_script);
    char *w = strstr(edited_text, "Hello there.");
    CHECK(w != NULL);
    if(w) {
        memcpy(w, "Hullo there.", 12);
        CHECK(story_parse(&edited, edited_text, "edited", err, sizeof(err)));
        CHECK(story_fingerprint(&edited) != story_fingerprint(story));
        story_free(&edited);
    }
    remove(path);
}

static const char *const cast_script =
    "player Crystal Jaguar\n"
    "rival Christian\n"
    "card Crystal: The Seeker. Wants proof.\n"
    "card Christian: The Shield.\n"
    "scene start\n"
    "say Narrator: Crystal fights in {player_har} against {rival_har}. {missing} stays.\n"
    "fight Crystal @player_har vs Christian @rival_har win -> won lose -> lost\n"
    "scene won\n"
    "say : won\n"
    "end\n"
    "scene lost\n"
    "say : lost\n"
    "end\n";

static void selftest_cast(void) {
    Story story;
    char err[256];
    StoryRun run, loaded;
    CHECK(story_parse(&story, cast_script, "cast", err, sizeof(err)));
    CHECK(story.has_cast && strcmp(story.player_pilot, "Crystal") == 0 && strcmp(story.player_har, "Jaguar") == 0);
    CHECK(strcmp(story.rival_pilot, "Christian") == 0 && story.card_count == 2);
    CHECK(strcmp(story_card_text(&story, "crystal"), "The Seeker. Wants proof.") == 0);
    CHECK(story_card_text(&story, "Milano")[0] == 0);

    // Flags chosen on the selection screen reach the text and the fight.
    StoryFlag flags[2] = {{"player_har", "Shadow"}, {"rival_har", "Jaguar"}};
    CHECK(story_start_with_flags(&run, &story, NULL, flags, 2));
    CHECK(strcmp(story_say_text(&run), "Crystal fights in Shadow against Jaguar. {missing} stays.") == 0);
    CHECK(strcmp(story_log_at(&run, 0)->text, story_say_text(&run)) == 0);
    story_advance(&run);
    CHECK(run.event == STORY_EVENT_FIGHT);
    char h0[STORY_NAME], h1[STORY_NAME];
    CHECK(story_fight_har(&run, story_event_cmd(&run), 0, h0, sizeof(h0)) && strcmp(h0, "Shadow") == 0);
    CHECK(story_fight_har(&run, story_event_cmd(&run), 1, h1, sizeof(h1)) && strcmp(h1, "Jaguar") == 0);

    // The state still round-trips through a save.
    CHECK(story_save(&run, "story_selftest_cast.save", err, sizeof(err)));
    CHECK(story_load_save(&loaded, &story, "story_selftest_cast.save", err, sizeof(err)) && same_run(&run, &loaded));
    CHECK(story_fight_har(&loaded, story_event_cmd(&loaded), 0, h0, sizeof(h0)) && strcmp(h0, "Shadow") == 0);
    remove("story_selftest_cast.save");

    // Without the flags the placeholders stay visible and the fight has no HAR.
    CHECK(story_start(&run, &story, NULL));
    CHECK(strstr(story_say_text(&run), "{player_har}") != NULL);
    story_advance(&run);
    CHECK(!story_fight_har(&run, story_event_cmd(&run), 0, h0, sizeof(h0)));
    StoryFlag bad[1] = {{"player_har", "Katana"}};
    CHECK(story_start_with_flags(&run, &story, NULL, bad, 1));
    story_advance(&run);
    CHECK(!story_fight_har(&run, story_event_cmd(&run), 0, h0, sizeof(h0)));

    // Editing a card changes the fingerprint, so an old save is refused.
    Story edited;
    char text[2048];
    snprintf(text, sizeof(text), "%s", cast_script);
    char *w = strstr(text, "Wants proof");
    CHECK(w != NULL);
    if(w) {
        memcpy(w, "Wants truth", 11);
        CHECK(story_parse(&edited, text, "edited", err, sizeof(err)));
        CHECK(story_fingerprint(&edited) != story_fingerprint(&story));
        story_free(&edited);
    }
    story_free(&story);

    CHECK(rejects("player Bob Jaguar\nscene a\nend\n", "unknown pilot"));
    CHECK(rejects("player Crystal Katana\nscene a\nend\n", "unknown HAR"));
    CHECK(rejects("player Crystal\nscene a\nend\n", "player needs"));
    CHECK(rejects("player Crystal Jaguar\nscene a\nend\n", "needs both"));
    CHECK(rejects("rival Christian\nscene a\nend\n", "needs both"));
    CHECK(rejects("player Crystal Jaguar\nrival Crystal\nscene a\nend\n", "same pilot"));
    CHECK(rejects("scene a\nend\nplayer Crystal Jaguar\n", "before the first scene"));
    CHECK(rejects("card Bob: hi\nscene a\nend\n", "unknown pilot"));
    CHECK(rejects("card Crystal hi\nscene a\nend\n", "card needs"));
    CHECK(rejects("scene a\nfight Crystal @ vs Christian Shadow win -> a lose -> a\n", "'@' needs"));
}

static void selftest_art(void) {
    static const char *const script =
        "player Crystal Jaguar\n"
        "rival Christian\n"
        "scene a\n"
        "art stadium_title fade\n"
        "say : one\n"
        "art faceoff_{player_har} zoom\n"
        "say : two\n"
        "art plain\n"
        "say : three\n"
        "art off\n"
        "say : four\n"
        "end\n";
    Story story;
    StoryRun run, loaded;
    char err[256];
    CHECK(story_parse(&story, script, "art", err, sizeof(err)));
    StoryFlag flags[2] = {{"player_har", "Shadow"}, {"rival_har", "Jaguar"}};
    CHECK(story_start_with_flags(&run, &story, NULL, flags, 2));
    CHECK(strcmp(run.art, "stadium_title") == 0 && strcmp(run.art_effect, "fade") == 0);
    story_advance(&run);
    CHECK(strcmp(run.art, "faceoff_Shadow") == 0 && strcmp(run.art_effect, "zoom") == 0);   // {flag} expanded
    CHECK(story_save(&run, "story_selftest_art.save", err, sizeof(err)));
    CHECK(story_load_save(&loaded, &story, "story_selftest_art.save", err, sizeof(err)));
    CHECK(strcmp(loaded.art, "faceoff_Shadow") == 0 && strcmp(loaded.art_effect, "zoom") == 0);   // saved and restored
    remove("story_selftest_art.save");
    story_advance(&run);
    CHECK(strcmp(run.art, "plain") == 0 && strcmp(run.art_effect, "none") == 0);                  // effect defaults to none
    story_advance(&run);
    CHECK(run.art[0] == 0 && strcmp(run.art_effect, "none") == 0);                                // "art off"
    story_free(&story);

    CHECK(rejects("scene a\nart\nend\n", "art needs"));
    CHECK(rejects("scene a\nart x fade extra\nend\n", "art needs"));
    CHECK(rejects("scene a\nart x spin\nend\n", "unknown art effect"));
    CHECK(rejects("scene a\nart ../x fade\nend\n", "letters, digits"));
}

static void selftest_effects(void) {
    static const char *const script =
        "scene a\n"
        "flash\n"
        "say : one\n"
        "banner Tier-2\n"
        "say : two\n"
        "end\n";
    Story story;
    StoryRun run;
    char err[256];
    CHECK(story_parse(&story, script, "effects", err, sizeof(err)));
    CHECK(story_start(&run, &story, NULL));
    CHECK(run.effect_serial == 1 && strcmp(run.effect_kind, "flash") == 0 && run.effect_text[0] == 0);
    CHECK(run.event == STORY_EVENT_SAY);                                  // a beat does not wait
    story_advance(&run);
    CHECK(run.effect_serial == 2 && strcmp(run.effect_kind, "banner") == 0 && strcmp(run.effect_text, "Tier-2") == 0);
    story_free(&story);
    CHECK(rejects("scene a\nflash now\nend\n", "flash takes no arguments"));
    CHECK(rejects("scene a\nbanner\nend\n", "banner needs text"));
}

static void selftest_music(void) {
    static const char *const script =
        "scene a\n"
        "music menu\n"
        "say : one\n"
        "music arena3\n"
        "say : two\n"
        "music off\n"
        "say : three\n"
        "end\n";
    Story story;
    StoryRun run, loaded;
    char err[256];
    CHECK(story_parse(&story, script, "music", err, sizeof(err)));
    CHECK(story_start(&run, &story, NULL));
    CHECK(strcmp(run.music, "menu") == 0);
    story_advance(&run);
    CHECK(strcmp(run.music, "arena3") == 0);
    CHECK(story_save(&run, "story_selftest_music.save", err, sizeof(err)));
    CHECK(story_load_save(&loaded, &story, "story_selftest_music.save", err, sizeof(err)) && strcmp(loaded.music, "arena3") == 0);
    remove("story_selftest_music.save");
    story_advance(&run);
    CHECK(run.music[0] == 0);                                  // "music off"
    story_free(&story);
    CHECK(rejects("scene a\nmusic\nend\n", "music needs"));
    CHECK(rejects("scene a\nmusic loud\nend\n", "music needs"));
}

static int cmd_selftest(void) {
    Story story;
    char err[256];
    CHECK(story_parse(&story, good_script, "good", err, sizeof(err)));
    if(failures) { printf("%s\n", err); return 1; }
    CHECK(story.scene_count == 8);

    int unreachable[8];
    CHECK(story_unreachable(&story, unreachable, 8) == 1);
    CHECK(strcmp(story.scenes[unreachable[0]].id, "orphan") == 0);

    StoryRun run;
    CHECK(story_start(&run, &story, NULL));
    CHECK(run.event == STORY_EVENT_SAY && strcmp(story_event_cmd(&run)->text, "Hello there.") == 0);
    CHECK(strcmp(run.bg, "stadium") == 0);
    story_advance(&run);
    CHECK(run.event == STORY_EVENT_SAY && story_event_cmd(&run)->speaker[0] == 0);
    story_advance(&run);
    CHECK(run.event == STORY_EVENT_CHOICE && run.choice_count == 2);
    CHECK(!story_choose(&run, 2));
    CHECK(story_choose(&run, 0));
    CHECK(strcmp(story_flag(&run, "evidence"), "shared") == 0);
    CHECK(run.event == STORY_EVENT_SAY && strcmp(story_event_cmd(&run)->text, "Shared.") == 0);
    story_advance(&run);
    CHECK(run.event == STORY_EVENT_FIGHT);
    CHECK(strcmp(story_event_cmd(&run)->pilot[1], "Christian") == 0);
    CHECK(!story_choose(&run, 0));
    CHECK(story_fight_result(&run, true));
    CHECK(run.event == STORY_EVENT_SAY && strcmp(story_event_cmd(&run)->text, "Won with a bonus.") == 0);
    story_advance(&run);
    CHECK(run.event == STORY_EVENT_END);

    // The other branch, with a loss.
    CHECK(story_start(&run, &story, NULL));
    CHECK(story_skip(&run) == 2 && run.event == STORY_EVENT_CHOICE);   // skip stops at the menu
    CHECK(story_log_count(&run) == 2);
    CHECK(story_choose(&run, 1));
    CHECK(strcmp(story_flag(&run, "evidence"), "kept") == 0);
    CHECK(story_skip(&run) == 1 && run.event == STORY_EVENT_FIGHT);
    CHECK(story_fight_result(&run, false));
    CHECK(strcmp(story_event_cmd(&run)->text, "Lost.") == 0);
    CHECK(story_log_count(&run) == 5 && strcmp(story_log_at(&run, 2)->speaker, "YOU") == 0);

    CHECK(story_start(&run, &story, "won"));
    CHECK(strcmp(story_event_cmd(&run)->text, "Won plainly.") == 0);   // flag unset: the if falls through
    CHECK(!story_start(&run, &story, "nowhere"));
    selftest_saves(&story);
    selftest_cast();
    selftest_art();
    selftest_effects();
    selftest_music();
    story_free(&story);

    // A long run keeps only the newest log entries.
    char big[64 * 1024] = "scene a\n";
    for(int i = 0; i < 100; i++) strcat(big, "say X: line\n");
    strcat(big, "end\n");
    CHECK(story_parse(&story, big, "big", err, sizeof(err)));
    CHECK(story_start(&run, &story, NULL));
    story_skip(&run);
    CHECK(story_log_count(&run) == STORY_LOG && run.event == STORY_EVENT_END);
    story_free(&story);

    // Scripts that must be rejected, each for the right reason.
    CHECK(rejects("say A: hi\n", "before any scene"));
    CHECK(rejects("scene a\nscene a\nend\n", "duplicate scene"));
    CHECK(rejects("scene a\nwave\nend\n", "unknown command"));
    CHECK(rejects("scene a\njump b\n", "unknown scene 'b'"));
    CHECK(rejects("scene a\nsay A: hi\n", "run off its end"));
    CHECK(rejects("scene a\nend\nsay A: hi\n", "unreachable command"));
    CHECK(rejects("scene a\nchoice X -> a\nsay A: hi\n", "after a choice menu"));
    CHECK(rejects("scene a\nsay hi\nend\n", "needs 'speaker: text'"));
    CHECK(rejects("scene a\nchoice X a\nend\n", "needs 'text -> scene'"));
    CHECK(rejects("scene a\nset evidence\nend\n", "set needs"));
    CHECK(rejects("scene a\nfight Bob Jaguar vs Crystal Shadow win -> a lose -> a\n", "unknown pilot"));
    CHECK(rejects("scene a\nfight Crystal Katana vs Christian Shadow win -> a lose -> a\n", "unknown HAR"));
    CHECK(rejects("scene a\nfight Crystal Jaguar vs Christian Shadow win -> a\n", "fight needs"));
    CHECK(rejects("scene a\nchoice 1 -> a\nchoice 2 -> a\nchoice 3 -> a\nchoice 4 -> a\nchoice 5 -> a\n"
                  "choice 6 -> a\nchoice 7 -> a\n", "at most"));
    CHECK(rejects("scene a\n", "is empty"));
    CHECK(rejects("# nothing\n", "no scenes"));

    printf(failures ? "%d self-test failure(s)\n" : "story self-test passed\n", failures);
    return failures ? 1 : 0;
}

int main(int argc, char **argv) {
    if(argc == 3 && strcmp(argv[1], "check") == 0) return cmd_check(argv[2]);
    if(argc >= 3 && strcmp(argv[1], "play") == 0) return cmd_play(argc, argv);
    if(argc == 2 && strcmp(argv[1], "selftest") == 0) return cmd_selftest();
    fputs("Usage: story_check check <script> | play <script> [--scene id] [--har Jaguar|Shadow] [--choices 0,1] [--results 1,0] | selftest\n", stderr);
    return 2;
}
