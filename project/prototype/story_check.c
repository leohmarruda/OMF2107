// Command-line checker for story scripts.
//   story_check check <script>                       validate and list unreachable scenes
//   story_check play <script> [--scene id] [--choices 0,1,...] [--results W,L,...]
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
    const char *path = argv[2], *scene = NULL, *choices = NULL, *results = NULL;
    for(int i = 3; i + 1 < argc; i += 2) {
        if(strcmp(argv[i], "--scene") == 0) scene = argv[i + 1];
        else if(strcmp(argv[i], "--choices") == 0) choices = argv[i + 1];
        else if(strcmp(argv[i], "--results") == 0) results = argv[i + 1];
        else { fprintf(stderr, "unknown option %s\n", argv[i]); return 2; }
    }
    Story story;
    char err[256];
    if(!story_load(&story, path, err, sizeof(err))) { fprintf(stderr, "%s\n", err); return 1; }
    StoryRun run;
    if(!story_start(&run, &story, scene)) { fprintf(stderr, "unknown scene '%s'\n", scene); story_free(&story); return 1; }
    for(int guard = 0; guard < 1000; guard++) {
        const StoryCmd *c;
        if(run.event == STORY_EVENT_SAY) {
            c = story_event_cmd(&run);
            printf("%s%s%s\n", c->speaker, *c->speaker ? ": " : "", c->text);
            story_advance(&run);
        } else if(run.event == STORY_EVENT_CHOICE) {
            int pick = next_number(&choices, 0);
            for(int i = 0; i < run.choice_count; i++)
                printf("  %c %d. %s\n", i == pick ? '>' : ' ', i, story_choice_cmd(&run, i)->text);
            if(!story_choose(&run, pick)) { fprintf(stderr, "choice %d is out of range\n", pick); story_free(&story); return 1; }
        } else if(run.event == STORY_EVENT_FIGHT) {
            c = story_event_cmd(&run);
            bool win = next_number(&results, 1) != 0;
            printf("[FIGHT %s/%s vs %s/%s -> %s]\n", c->pilot[0], c->har[0], c->pilot[1], c->har[1], win ? "win" : "lose");
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
    fputs("Usage: story_check check <script> | play <script> [--scene id] [--choices 0,1] [--results 1,0] | selftest\n", stderr);
    return 2;
}
