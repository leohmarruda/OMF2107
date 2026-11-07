#include "story.h"

#include <ctype.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// The ten playable pilots and the two HARs the prototype can render.
static const char *const known_pilots[] = {"Crystal", "Steffan", "Milano", "Christian", "Shirro",
                                           "JeanPaul", "Ibrahim", "Angel", "Cossette", "Raven", "Ari", "Selene", "Mara", "Ren", "Lyra", "Nova"};
static const char *const known_hars[] = {"Jaguar", "Shadow", "Katana"};

static bool ieq(const char *a, const char *b) {
    for(; *a && *b; a++, b++)
        if(tolower((unsigned char)*a) != tolower((unsigned char)*b)) return false;
    return *a == *b;
}

static bool in_list(const char *s, const char *const *list, size_t count) {
    for(size_t i = 0; i < count; i++)
        if(ieq(s, list[i])) return true;
    return false;
}

static void fail(char *err, size_t err_size, const char *name, int line, const char *fmt, ...) {
    if(!err || !err_size) return;
    int n = snprintf(err, err_size, "%s:%d: ", name, line);
    if(n < 0 || (size_t)n >= err_size) return;
    va_list ap;
    va_start(ap, fmt);
    vsnprintf(err + n, err_size - (size_t)n, fmt, ap);
    va_end(ap);
}

static char *trim(char *s) {
    while(*s && isspace((unsigned char)*s)) s++;
    char *end = s + strlen(s);
    while(end > s && isspace((unsigned char)end[-1])) *--end = 0;
    return s;
}

// Copies src into dst; false when it does not fit.
static bool copy(char *dst, size_t size, const char *src) {
    size_t n = strlen(src);
    if(n >= size) return false;
    memcpy(dst, src, n + 1);
    return true;
}

// Next whitespace-separated token, advancing *p. Returns NULL at the end of the line.
static char *token(char **p) {
    char *s = *p;
    while(*s && isspace((unsigned char)*s)) s++;
    if(!*s) { *p = s; return NULL; }
    char *start = s;
    while(*s && !isspace((unsigned char)*s)) s++;
    if(*s) *s++ = 0;
    *p = s;
    return start;
}

// "flag=value" into its two parts.
static bool split_assignment(char *text, char *flag, char *value) {
    char *eq = strchr(text, '=');
    if(!eq) return false;
    *eq = 0;
    char *f = trim(text), *v = trim(eq + 1);
    if(!*f || !*v) return false;
    return copy(flag, STORY_NAME, f) && copy(value, STORY_NAME, v);
}

static StoryCmd *add_cmd(Story *s, StoryCmdKind kind, int line) {
    StoryCmd *grown = realloc(s->cmds, (size_t)(s->cmd_count + 1) * sizeof(*grown));
    if(!grown) return NULL;
    s->cmds = grown;
    StoryCmd *c = &s->cmds[s->cmd_count++];
    memset(c, 0, sizeof(*c));
    c->kind = kind;
    c->line = line;
    c->target = c->target2 = -1;
    return c;
}

void story_free(Story *story) {
    free(story->scenes);
    free(story->cmds);
    memset(story, 0, sizeof(*story));
}

int story_find_scene(const Story *story, const char *id) {
    for(int i = 0; i < story->scene_count; i++)
        if(strcmp(story->scenes[i].id, id) == 0) return i;
    return -1;
}

static bool resolve(const Story *s, const char *name, int line, const char *what, int *out, const char *src,
                    char *err, size_t err_size) {
    int index = story_find_scene(s, name);
    if(index < 0) {
        fail(err, err_size, src, line, "%s refers to unknown scene '%s'", what, name);
        return false;
    }
    *out = index;
    return true;
}

// Parses one command line (already trimmed, not a comment) into the story.
static bool parse_line(Story *s, char *line_text, int line, const char *name, char *err, size_t err_size) {
    char *rest = line_text;
    char *word = token(&rest);
    rest = trim(rest);
    StoryScene *scene = s->scene_count ? &s->scenes[s->scene_count - 1] : NULL;

    if(strcmp(word, "player") == 0 || strcmp(word, "rival") == 0 || strcmp(word, "card") == 0 ||
       strcmp(word, "route") == 0 || strcmp(word, "blurb") == 0 || strcmp(word, "opponents") == 0) {
        if(scene) { fail(err, err_size, name, line, "'%s' must come before the first scene", word); return false; }
        if(strcmp(word, "blurb") == 0) {
            if(!*rest) { fail(err, err_size, name, line, "blurb has no text"); return false; }
            if(s->blurb[0]) { fail(err, err_size, name, line, "a script can have only one blurb"); return false; }
            if(!copy(s->blurb, STORY_TEXT, rest)) { fail(err, err_size, name, line, "blurb is too long"); return false; }
        } else if(strcmp(word, "opponents") == 0) {
            if(!*rest) { fail(err, err_size, name, line, "opponents needs a list of pilots"); return false; }
            if(s->opponent_count) { fail(err, err_size, name, line, "a script can have only one opponents line"); return false; }
            while(*rest) {
                char *comma = strchr(rest, ',');
                if(comma) *comma = 0;
                char *pilot = trim(rest);
                if(!in_list(pilot, known_pilots, sizeof(known_pilots) / sizeof(known_pilots[0]))) {
                    fail(err, err_size, name, line, "unknown pilot '%s'", pilot); return false;
                }
                if(s->opponent_count >= STORY_MAX_OPPONENTS) {
                    fail(err, err_size, name, line, "at most %d opponents", STORY_MAX_OPPONENTS); return false;
                }
                copy(s->opponents[s->opponent_count++], STORY_NAME, pilot);
                if(!comma) break;
                rest = comma + 1;
            }
        } else if(strcmp(word, "card") == 0) {
            char *colon = strchr(rest, ':');
            if(!colon) { fail(err, err_size, name, line, "card needs '<pilot>: <text>'"); return false; }
            *colon = 0;
            char *pilot = trim(rest), *text = trim(colon + 1);
            if(!in_list(pilot, known_pilots, sizeof(known_pilots) / sizeof(known_pilots[0]))) {
                fail(err, err_size, name, line, "unknown pilot '%s'", pilot); return false;
            }
            if(!*text) { fail(err, err_size, name, line, "card has no text"); return false; }
            if(s->card_count >= STORY_MAX_CARDS) { fail(err, err_size, name, line, "at most %d cards", STORY_MAX_CARDS); return false; }
            StoryCard *card = &s->cards[s->card_count++];
            if(!copy(card->pilot, STORY_NAME, pilot) || !copy(card->text, STORY_TEXT, text)) {
                fail(err, err_size, name, line, "card text is too long"); return false;
            }
        } else if(strcmp(word, "route") == 0) {
            char *pilot = token(&rest), *path = trim(rest);
            if(!pilot || !*path) { fail(err, err_size, name, line, "route needs '<pilot> <script path>'"); return false; }
            if(!in_list(pilot, known_pilots, sizeof(known_pilots) / sizeof(known_pilots[0]))) {
                fail(err, err_size, name, line, "unknown pilot '%s'", pilot); return false;
            }
            if(s->has_route) { fail(err, err_size, name, line, "a script can name only one route"); return false; }
            if(!copy(s->route.pilot, STORY_NAME, pilot) || !copy(s->route.path, sizeof(s->route.path), path)) {
                fail(err, err_size, name, line, "route is too long"); return false;
            }
            s->has_route = true;
        } else if(strcmp(word, "player") == 0) {
            char *pilot = token(&rest), *har = token(&rest), *extra = token(&rest);
            if(!pilot || !har || extra) { fail(err, err_size, name, line, "player needs '<pilot> <recommended har>'"); return false; }
            if(!in_list(pilot, known_pilots, sizeof(known_pilots) / sizeof(known_pilots[0]))) {
                fail(err, err_size, name, line, "unknown pilot '%s'", pilot); return false;
            }
            if(!in_list(har, known_hars, sizeof(known_hars) / sizeof(known_hars[0]))) {
                fail(err, err_size, name, line, "unknown HAR '%s' (the story offers Jaguar, Shadow and Katana)", har); return false;
            }
            copy(s->player_pilot, STORY_NAME, pilot);
            copy(s->player_har, STORY_NAME, har);
        } else {
            if(!*rest || strchr(rest, ' ')) { fail(err, err_size, name, line, "rival needs one pilot"); return false; }
            if(!in_list(rest, known_pilots, sizeof(known_pilots) / sizeof(known_pilots[0]))) {
                fail(err, err_size, name, line, "unknown pilot '%s'", rest); return false;
            }
            copy(s->rival_pilot, STORY_NAME, rest);
        }
        return true;
    }

    if(strcmp(word, "scene") == 0) {
        if(!*rest || strchr(rest, ' ')) { fail(err, err_size, name, line, "scene needs one id"); return false; }
        if(story_find_scene(s, rest) >= 0) { fail(err, err_size, name, line, "duplicate scene '%s'", rest); return false; }
        StoryScene *grown = realloc(s->scenes, (size_t)(s->scene_count + 1) * sizeof(*grown));
        if(!grown) { fail(err, err_size, name, line, "out of memory"); return false; }
        s->scenes = grown;
        StoryScene *n = &s->scenes[s->scene_count++];
        memset(n, 0, sizeof(*n));
        if(!copy(n->id, STORY_NAME, rest)) { fail(err, err_size, name, line, "scene id is too long"); return false; }
        n->first = s->cmd_count;
        n->line = line;
        return true;
    }
    if(!scene) { fail(err, err_size, name, line, "'%s' appears before any scene", word); return false; }

    StoryCmd *c = NULL;
    if(strcmp(word, "bg") == 0) {
        if(!*rest) { fail(err, err_size, name, line, "bg needs a name"); return false; }
        c = add_cmd(s, STORY_CMD_BG, line);
        if(c && !copy(c->text, STORY_NAME, rest)) { fail(err, err_size, name, line, "bg name is too long"); return false; }
    } else if(strcmp(word, "art") == 0) {
        char *art_name = token(&rest), *effect = token(&rest), *extra = token(&rest);
        if(!art_name || extra) { fail(err, err_size, name, line, "art needs '<name> [none|fade|zoom|pan]'"); return false; }
        if(effect && strcmp(effect, "none") != 0 && strcmp(effect, "fade") != 0 && strcmp(effect, "zoom") != 0 &&
           strcmp(effect, "pan") != 0) {
            fail(err, err_size, name, line, "unknown art effect '%s' (use none, fade, zoom, or pan)", effect); return false;
        }
        for(const char *p = art_name; *p; p++) {
            bool ok = (*p >= 'a' && *p <= 'z') || (*p >= 'A' && *p <= 'Z') || (*p >= '0' && *p <= '9') || *p == '_' ||
                      *p == '{' || *p == '}';
            if(!ok) { fail(err, err_size, name, line, "art names use letters, digits, '_', and {flag} only"); return false; }
        }
        c = add_cmd(s, STORY_CMD_ART, line);
        if(c && (!copy(c->text, STORY_NAME, art_name) || !copy(c->value, STORY_NAME, effect ? effect : "none"))) {
            fail(err, err_size, name, line, "art name is too long"); return false;
        }
    } else if(strcmp(word, "music") == 0) {
        static const char *const tracks[] = {"menu", "arena0", "arena1", "arena2", "arena3", "arena4", "end", "off"};
        bool known = false;
        for(size_t i = 0; i < sizeof(tracks) / sizeof(tracks[0]); i++) known = known || strcmp(rest, tracks[i]) == 0;
        if(!known) {
            fail(err, err_size, name, line, "music needs menu, arena0 to arena4, end, or off");
            return false;
        }
        c = add_cmd(s, STORY_CMD_MUSIC, line);
        if(c) copy(c->text, STORY_NAME, rest);
    } else if(strcmp(word, "flash") == 0) {
        if(*rest) { fail(err, err_size, name, line, "flash takes no arguments"); return false; }
        c = add_cmd(s, STORY_CMD_FLASH, line);
    } else if(strcmp(word, "banner") == 0) {
        if(!*rest) { fail(err, err_size, name, line, "banner needs text"); return false; }
        c = add_cmd(s, STORY_CMD_BANNER, line);
        if(c && !copy(c->text, STORY_NAME, rest)) { fail(err, err_size, name, line, "banner text is too long"); return false; }
    } else if(strcmp(word, "present") == 0) {
        char *image = token(&rest);
        if(!image) { fail(err, err_size, name, line, "present needs '<image> <left|right> [name]' or 'off'"); return false; }
        c = add_cmd(s, STORY_CMD_PRESENT, line);
        if(strcmp(image, "off") == 0) {
            if(*rest) { fail(err, err_size, name, line, "present off takes no arguments"); return false; }
            if(c) copy(c->flag, STORY_NAME, "off");
        } else {
            char *side = token(&rest);
            if(!side || (strcmp(side, "left") != 0 && strcmp(side, "right") != 0)) {
                fail(err, err_size, name, line, "present needs '<image> <left|right> [name]' or 'off'"); return false;
            }
            for(const char *p = image; *p; p++) {
                bool ok = (*p >= 'a' && *p <= 'z') || (*p >= 'A' && *p <= 'Z') || (*p >= '0' && *p <= '9') || *p == '_';
                if(!ok) { fail(err, err_size, name, line, "present image names use letters, digits, and '_' only"); return false; }
            }
            if(c && (!copy(c->flag, STORY_NAME, image) || !copy(c->value, STORY_NAME, side) || !copy(c->text, STORY_NAME, trim(rest)))) {
                fail(err, err_size, name, line, "present image or name is too long"); return false;
            }
        }
    } else if(strcmp(word, "say") == 0) {
        char *colon = strchr(rest, ':');
        if(!colon) { fail(err, err_size, name, line, "say needs 'speaker: text' (use 'say : text' for narration)"); return false; }
        *colon = 0;
        char *speaker = trim(rest), *text = trim(colon + 1);
        if(!*text) { fail(err, err_size, name, line, "say has no text"); return false; }
        c = add_cmd(s, STORY_CMD_SAY, line);
        if(c && (!copy(c->speaker, STORY_NAME, speaker) || !copy(c->text, STORY_TEXT, text))) {
            fail(err, err_size, name, line, "speaker or text is too long"); return false;
        }
    } else if(strcmp(word, "choice") == 0) {
        char *arrow = strstr(rest, "->");
        if(!arrow) { fail(err, err_size, name, line, "choice needs 'text -> scene'"); return false; }
        *arrow = 0;
        char *text = trim(rest), *after = arrow + 2;
        if(!*text) { fail(err, err_size, name, line, "choice has no text"); return false; }
        char *target = token(&after);
        if(!target) { fail(err, err_size, name, line, "choice has no target scene"); return false; }
        c = add_cmd(s, STORY_CMD_CHOICE, line);
        if(!c) return false;
        if(!copy(c->text, STORY_TEXT, text) || !copy(c->target_name, STORY_NAME, target)) {
            fail(err, err_size, name, line, "choice text or target is too long"); return false;
        }
        char *kw = token(&after);
        if(kw) {
            after = trim(after);
            if(strcmp(kw, "set") != 0 || !split_assignment(after, c->flag, c->value)) {
                fail(err, err_size, name, line, "choice may end with 'set flag=value'"); return false;
            }
            c->has_set = true;
        }
    } else if(strcmp(word, "set") == 0) {
        c = add_cmd(s, STORY_CMD_SET, line);
        if(c && !split_assignment(rest, c->flag, c->value)) {
            fail(err, err_size, name, line, "set needs 'flag=value'"); return false;
        }
    } else if(strcmp(word, "if") == 0) {
        char *arrow = strstr(rest, "->");
        if(!arrow) { fail(err, err_size, name, line, "if needs 'flag=value -> scene'"); return false; }
        *arrow = 0;
        char *target = trim(arrow + 2);
        c = add_cmd(s, STORY_CMD_IF, line);
        if(!c) return false;
        if(!split_assignment(rest, c->flag, c->value) || !*target || !copy(c->target_name, STORY_NAME, target)) {
            fail(err, err_size, name, line, "if needs 'flag=value -> scene'"); return false;
        }
    } else if(strcmp(word, "jump") == 0) {
        c = add_cmd(s, STORY_CMD_JUMP, line);
        if(c && (!*rest || !copy(c->target_name, STORY_NAME, rest))) {
            fail(err, err_size, name, line, "jump needs a scene"); return false;
        }
    } else if(strcmp(word, "fight") == 0) {
        c = add_cmd(s, STORY_CMD_FIGHT, line);
        if(!c) return false;
        char *a_pilot = token(&rest), *a_har = token(&rest), *vs = token(&rest), *b_pilot = token(&rest);
        char *b_har = token(&rest), *w = token(&rest), *w_arrow = token(&rest), *w_scene = token(&rest);
        char *l = token(&rest), *l_arrow = token(&rest), *l_scene = token(&rest), *extra = token(&rest);
        if(!l_scene || extra || strcmp(vs, "vs") != 0 || strcmp(w, "win") != 0 || strcmp(w_arrow, "->") != 0 ||
           strcmp(l, "lose") != 0 || strcmp(l_arrow, "->") != 0) {
            fail(err, err_size, name, line,
                 "fight needs '<pilot> <har> vs <pilot> <har> win -> <scene> lose -> <scene>'");
            return false;
        }
        if(!copy(c->pilot[0], STORY_NAME, a_pilot) || !copy(c->har[0], STORY_NAME, a_har) ||
           !copy(c->pilot[1], STORY_NAME, b_pilot) || !copy(c->har[1], STORY_NAME, b_har) ||
           !copy(c->target_name, STORY_NAME, w_scene) || !copy(c->target2_name, STORY_NAME, l_scene)) {
            fail(err, err_size, name, line, "fight has a name that is too long"); return false;
        }
        for(int i = 0; i < 2; i++) {
            if(!in_list(c->pilot[i], known_pilots, sizeof(known_pilots) / sizeof(known_pilots[0]))) {
                fail(err, err_size, name, line, "unknown pilot '%s'", c->pilot[i]); return false;
            }
            if(c->har[i][0] == '@') {
                if(!c->har[i][1]) { fail(err, err_size, name, line, "'@' needs a flag name"); return false; }
            } else if(!in_list(c->har[i], known_hars, sizeof(known_hars) / sizeof(known_hars[0]))) {
                fail(err, err_size, name, line, "unknown HAR '%s' (the story offers Jaguar, Shadow and Katana)",
                     c->har[i]);
                return false;
            }
        }
    } else if(strcmp(word, "end") == 0) {
        if(*rest) { fail(err, err_size, name, line, "end takes no arguments"); return false; }
        c = add_cmd(s, STORY_CMD_END, line);
    } else {
        fail(err, err_size, name, line, "unknown command '%s'", word);
        return false;
    }
    if(!c) { fail(err, err_size, name, line, "out of memory"); return false; }
    s->scenes[s->scene_count - 1].count++;
    return true;
}

static bool validate(Story *s, const char *name, char *err, size_t err_size) {
    if(s->scene_count == 0) { fail(err, err_size, name, 1, "the script has no scenes"); return false; }
    if(s->player_pilot[0] || s->rival_pilot[0]) {
        if(!s->player_pilot[0] || !s->rival_pilot[0]) {
            fail(err, err_size, name, 1, "a script with a selection screen needs both a 'player' and a 'rival' line");
            return false;
        }
        if(ieq(s->player_pilot, s->rival_pilot)) {
            fail(err, err_size, name, 1, "the player and the rival cannot be the same pilot");
            return false;
        }
        s->has_cast = true;
    }
    if(s->has_route && (!s->has_cast || ieq(s->route.pilot, s->player_pilot))) {
        fail(err, err_size, name, 1, "a route needs a cast, and must offer a pilot other than the player");
        return false;
    }
    for(int i = 0; i < s->scene_count; i++) {
        const StoryScene *sc = &s->scenes[i];
        if(sc->count == 0) {
            fail(err, err_size, name, sc->line, "scene '%s' is empty", sc->id); return false;
        }
        int menu = 0;
        for(int k = 0; k < sc->count; k++) {
            StoryCmd *c = &s->cmds[sc->first + k];
            const StoryCmd *next = k + 1 < sc->count ? &s->cmds[sc->first + k + 1] : NULL;
            if(c->kind == STORY_CMD_IF || c->kind == STORY_CMD_JUMP || c->kind == STORY_CMD_CHOICE ||
               c->kind == STORY_CMD_FIGHT) {
                if(!resolve(s, c->target_name, c->line, c->kind == STORY_CMD_IF ? "if" :
                            c->kind == STORY_CMD_JUMP ? "jump" : c->kind == STORY_CMD_FIGHT ? "fight win" : "choice",
                            &c->target, name, err, err_size)) return false;
            }
            if(c->kind == STORY_CMD_FIGHT &&
               !resolve(s, c->target2_name, c->line, "fight lose", &c->target2, name, err, err_size)) return false;
            if(c->kind == STORY_CMD_CHOICE) {
                if(++menu > STORY_MAX_CHOICES) {
                    fail(err, err_size, name, c->line, "a menu may have at most %d choices", STORY_MAX_CHOICES);
                    return false;
                }
                if(next && next->kind != STORY_CMD_CHOICE) {
                    fail(err, err_size, name, next->line, "commands after a choice menu are unreachable"); return false;
                }
            } else {
                menu = 0;
            }
            if((c->kind == STORY_CMD_JUMP || c->kind == STORY_CMD_END || c->kind == STORY_CMD_FIGHT) && next) {
                fail(err, err_size, name, next->line, "unreachable command after jump, end, or fight"); return false;
            }
            if(!next && c->kind != STORY_CMD_JUMP && c->kind != STORY_CMD_END && c->kind != STORY_CMD_FIGHT &&
               c->kind != STORY_CMD_CHOICE) {
                fail(err, err_size, name, sc->line,
                     "scene '%s' can run off its end; finish it with jump, end, fight, or a choice menu", sc->id);
                return false;
            }
        }
    }
    return true;
}

bool story_parse(Story *story, const char *text, const char *name, char *err, size_t err_size) {
    memset(story, 0, sizeof(*story));
    if(err && err_size) err[0] = 0;
    char *copy_text = malloc(strlen(text) + 1);
    if(!copy_text) { fail(err, err_size, name, 0, "out of memory"); return false; }
    strcpy(copy_text, text);
    int line = 0;
    bool ok = true;
    for(char *p = copy_text; ok && *p;) {
        char *eol = strchr(p, '\n');
        if(eol) *eol = 0;
        line++;
        char *t = trim(p);
        if(*t && *t != '#') ok = parse_line(story, t, line, name, err, err_size);
        p = eol ? eol + 1 : p + strlen(p);
    }
    free(copy_text);
    if(ok) ok = validate(story, name, err, err_size);
    if(!ok) story_free(story);
    return ok;
}

bool story_load(Story *story, const char *path, char *err, size_t err_size) {
    memset(story, 0, sizeof(*story));
    FILE *f = fopen(path, "rb");
    if(!f) { fail(err, err_size, path, 0, "cannot open the script"); return false; }
    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    fseek(f, 0, SEEK_SET);
    if(size < 0 || size > 1 << 20) { fclose(f); fail(err, err_size, path, 0, "the script is empty or too large"); return false; }
    char *text = malloc((size_t)size + 1);
    if(!text) { fclose(f); fail(err, err_size, path, 0, "out of memory"); return false; }
    size_t got = fread(text, 1, (size_t)size, f);
    fclose(f);
    text[got] = 0;
    bool ok = story_parse(story, text, path, err, err_size);
    free(text);
    return ok;
}

int story_unreachable(const Story *story, int *out, int max) {
    if(story->scene_count == 0) return 0;
    bool *seen = calloc((size_t)story->scene_count, sizeof(bool));
    int *queue = malloc((size_t)story->scene_count * sizeof(int));
    if(!seen || !queue) { free(seen); free(queue); return 0; }
    int head = 0, tail = 0;
    seen[0] = true;
    queue[tail++] = 0;
    while(head < tail) {
        const StoryScene *sc = &story->scenes[queue[head++]];
        for(int k = 0; k < sc->count; k++) {
            const StoryCmd *c = &story->cmds[sc->first + k];
            int targets[2] = {c->target, c->kind == STORY_CMD_FIGHT ? c->target2 : -1};
            for(int t = 0; t < 2; t++)
                if(targets[t] >= 0 && !seen[targets[t]]) { seen[targets[t]] = true; queue[tail++] = targets[t]; }
        }
    }
    int n = 0;
    for(int i = 0; i < story->scene_count && n < max; i++)
        if(!seen[i]) out[n++] = i;
    free(seen);
    free(queue);
    return n;
}

// ---- runner ----

static const StoryScene *scene_of(const StoryRun *r) { return &r->story->scenes[r->scene]; }
static const StoryCmd *cmd_at(const StoryRun *r, int pc) { return &r->story->cmds[scene_of(r)->first + pc]; }

static void log_add(StoryRun *r, const char *speaker, const char *text) {
    StoryLogEntry *e = &r->log[r->log_total % STORY_LOG];
    snprintf(e->speaker, sizeof(e->speaker), "%s", speaker);
    snprintf(e->text, sizeof(e->text), "%s", text);
    r->log_total++;
}

static void set_flag(StoryRun *r, const char *name, const char *value) {
    for(int i = 0; i < r->flag_count; i++)
        if(strcmp(r->flags[i].name, name) == 0) { snprintf(r->flags[i].value, STORY_NAME, "%s", value); return; }
    if(r->flag_count < STORY_MAX_FLAGS) {
        snprintf(r->flags[r->flag_count].name, STORY_NAME, "%s", name);
        snprintf(r->flags[r->flag_count].value, STORY_NAME, "%s", value);
        r->flag_count++;
    }
}

const char *story_flag(const StoryRun *run, const char *name) {
    for(int i = 0; i < run->flag_count; i++)
        if(strcmp(run->flags[i].name, name) == 0) return run->flags[i].value;
    return "";
}

static const char *find_flag(const StoryRun *r, const char *name) {
    for(int i = 0; i < r->flag_count; i++)
        if(strcmp(r->flags[i].name, name) == 0) return r->flags[i].value;
    return NULL;
}

// Copies src to dst, replacing {flag} with the flag's value. An unset flag is left as written so a typo shows up.
static void expand(const StoryRun *r, const char *src, char *dst, size_t size) {
    size_t n = 0;
    for(const char *p = src; *p && n + 1 < size;) {
        if(*p == '{') {
            const char *end = strchr(p, '}');
            size_t len = end ? (size_t)(end - p - 1) : 0;
            if(end && len > 0 && len < STORY_NAME) {
                char name[STORY_NAME];
                memcpy(name, p + 1, len);
                name[len] = 0;
                const char *value = find_flag(r, name);
                if(value) {
                    for(const char *v = value; *v && n + 1 < size; v++) dst[n++] = *v;
                    p = end + 1;
                    continue;
                }
            }
        }
        dst[n++] = *p++;
    }
    dst[n] = 0;
}

static void goto_scene(StoryRun *r, int scene) { r->scene = scene; r->pc = 0; }

// Runs commands that need no input until one needs the host. log_say is false when restoring a save,
// whose log already holds the say line it stopped on.
static void step_to_event(StoryRun *r, bool log_say) {
    for(int guard = 0; guard < 100000; guard++) {
        if(r->pc >= scene_of(r)->count) { r->event = STORY_EVENT_END; return; }  // not reachable once validated
        const StoryCmd *c = cmd_at(r, r->pc);
        switch(c->kind) {
            case STORY_CMD_BG: snprintf(r->bg, sizeof(r->bg), "%s", c->text); r->pc++; break;
            case STORY_CMD_MUSIC:
                snprintf(r->music, sizeof(r->music), "%s", strcmp(c->text, "off") == 0 ? "" : c->text);
                r->pc++;
                break;
            case STORY_CMD_FLASH:
            case STORY_CMD_BANNER:
                r->effect_serial++;
                snprintf(r->effect_kind, sizeof(r->effect_kind), "%s", c->kind == STORY_CMD_FLASH ? "flash" : "banner");
                snprintf(r->effect_text, sizeof(r->effect_text), "%s", c->kind == STORY_CMD_BANNER ? c->text : "");
                r->pc++;
                break;
            case STORY_CMD_PRESENT:
                if(strcmp(c->flag, "off") == 0) {
                    memset(r->present, 0, sizeof(r->present));
                } else {
                    StoryPresent *p = &r->present[strcmp(c->value, "left") == 0 ? 0 : 1];
                    bool seen = false;
                    for(int i = 0; i < r->name_seen_count; i++) if(strcmp(r->name_seen[i], c->flag) == 0) seen = true;
                    snprintf(p->image, sizeof(p->image), "%s", c->flag);
                    // The name plate shows the first time this portrait appears and never again.
                    snprintf(p->name, sizeof(p->name), "%s", seen ? "" : c->text);
                    p->stage = p->name[0] ? 1 : 3;
                    if(!seen && c->text[0] && r->name_seen_count < STORY_NAME_SEEN)
                        snprintf(r->name_seen[r->name_seen_count++], STORY_NAME, "%s", c->flag);
                }
                r->pc++;
                break;
            case STORY_CMD_ART:
                if(strcmp(c->text, "off") == 0) {
                    r->art[0] = 0;
                    snprintf(r->art_effect, sizeof(r->art_effect), "none");
                } else {
                    expand(r, c->text, r->art, sizeof(r->art));
                    snprintf(r->art_effect, sizeof(r->art_effect), "%s", c->value);
                }
                r->pc++;
                break;
            case STORY_CMD_SET: set_flag(r, c->flag, c->value); r->pc++; break;
            case STORY_CMD_IF:
                if(strcmp(story_flag(r, c->flag), c->value) == 0) goto_scene(r, c->target);
                else r->pc++;
                break;
            case STORY_CMD_JUMP: goto_scene(r, c->target); break;
            case STORY_CMD_SAY:
                expand(r, c->text, r->say_text, sizeof(r->say_text));
                if(log_say) {
                    log_add(r, c->speaker, r->say_text);
                    for(int i = 0; i < 2; i++) {
                        if(r->present[i].stage == 1) r->present[i].stage = 2;        // the name arrives with its first line
                        else if(r->present[i].stage == 2) r->present[i].stage = 3;   // and leaves with the next
                    }
                }
                r->event = STORY_EVENT_SAY;
                return;
            case STORY_CMD_CHOICE:
                r->event = STORY_EVENT_CHOICE;
                r->choice_first = r->pc;
                r->choice_count = 0;
                while(r->pc + r->choice_count < scene_of(r)->count &&
                      cmd_at(r, r->pc + r->choice_count)->kind == STORY_CMD_CHOICE) r->choice_count++;
                return;
            case STORY_CMD_FIGHT: r->event = STORY_EVENT_FIGHT; return;
            case STORY_CMD_END:
            default: r->event = STORY_EVENT_END; return;
        }
    }
    r->event = STORY_EVENT_END;  // a loop of jumps with no dialogue; stop rather than hang
}

static void step(StoryRun *r) { step_to_event(r, true); }

bool story_start_with_flags(StoryRun *run, const Story *story, const char *scene_id, const StoryFlag *flags, int count) {
    memset(run, 0, sizeof(*run));
    run->story = story;
    int scene = scene_id ? story_find_scene(story, scene_id) : 0;
    if(scene < 0) return false;
    for(int i = 0; i < count && i < STORY_MAX_FLAGS; i++) set_flag(run, flags[i].name, flags[i].value);
    goto_scene(run, scene);
    step(run);
    return true;
}

bool story_start(StoryRun *run, const Story *story, const char *scene_id) {
    return story_start_with_flags(run, story, scene_id, NULL, 0);
}

bool story_fight_har(const StoryRun *run, const StoryCmd *fight, int side, char *out, size_t out_size) {
    const char *har = fight->har[side];
    if(har[0] == '@') {
        const char *value = find_flag(run, har + 1);
        snprintf(out, out_size, "%s", value ? value : "");
    } else {
        snprintf(out, out_size, "%s", har);
    }
    return in_list(out, known_hars, sizeof(known_hars) / sizeof(known_hars[0]));
}

const char *story_say_text(const StoryRun *run) { return run->say_text; }

const char *story_card_text(const Story *story, const char *pilot) {
    for(int i = 0; i < story->card_count; i++)
        if(ieq(story->cards[i].pilot, pilot)) return story->cards[i].text;
    return "";
}

const StoryCmd *story_event_cmd(const StoryRun *run) {
    if(run->event != STORY_EVENT_SAY && run->event != STORY_EVENT_FIGHT) return NULL;
    return cmd_at(run, run->pc);
}

const StoryCmd *story_choice_cmd(const StoryRun *run, int index) {
    if(run->event != STORY_EVENT_CHOICE || index < 0 || index >= run->choice_count) return NULL;
    return cmd_at(run, run->choice_first + index);
}

void story_advance(StoryRun *run) {
    if(run->event != STORY_EVENT_SAY) return;
    run->pc++;
    step(run);
}

bool story_choose(StoryRun *run, int index) {
    const StoryCmd *c = story_choice_cmd(run, index);
    if(!c) return false;
    log_add(run, "YOU", c->text);
    if(c->has_set) set_flag(run, c->flag, c->value);
    goto_scene(run, c->target);
    step(run);
    return true;
}

bool story_fight_result(StoryRun *run, bool win) {
    if(run->event != STORY_EVENT_FIGHT) return false;
    const StoryCmd *c = cmd_at(run, run->pc);
    goto_scene(run, win ? c->target : c->target2);
    step(run);
    return true;
}

int story_skip(StoryRun *run) {
    int skipped = 0;
    while(run->event == STORY_EVENT_SAY && skipped < 100000) {
        story_advance(run);
        skipped++;
    }
    return skipped;
}

void story_note(StoryRun *run, const char *text) { log_add(run, "DEBUG", text); }

void story_record(StoryRun *run, const char *speaker, const char *text) { log_add(run, speaker, text); }

int story_log_count(const StoryRun *run) { return run->log_total < STORY_LOG ? run->log_total : STORY_LOG; }

const StoryLogEntry *story_log_at(const StoryRun *run, int index) {
    int count = story_log_count(run);
    if(index < 0 || index >= count) return NULL;
    int first = run->log_total - count;
    return &run->log[(first + index) % STORY_LOG];
}

// ---- save data ----

static unsigned fnv_bytes(unsigned h, const void *data, size_t n) {
    const unsigned char *p = data;
    for(size_t i = 0; i < n; i++) { h ^= p[i]; h *= 16777619u; }
    return h;
}

static unsigned fnv_str(unsigned h, const char *s) { return fnv_bytes(h, s, strlen(s) + 1); }

unsigned story_fingerprint(const Story *story) {
    unsigned h = 2166136261u;
    h = fnv_str(h, story->player_pilot);
    h = fnv_str(h, story->player_har);
    h = fnv_str(h, story->rival_pilot);
    for(int i = 0; i < story->card_count; i++) { h = fnv_str(h, story->cards[i].pilot); h = fnv_str(h, story->cards[i].text); }
    for(int i = 0; i < story->scene_count; i++) {
        const StoryScene *sc = &story->scenes[i];
        h = fnv_str(h, sc->id);
        for(int k = 0; k < sc->count; k++) {
            const StoryCmd *c = &story->cmds[sc->first + k];
            int kind = (int)c->kind;
            h = fnv_bytes(h, &kind, sizeof(kind));
            h = fnv_str(h, c->speaker);
            h = fnv_str(h, c->text);
            h = fnv_str(h, c->flag);
            h = fnv_str(h, c->value);
            h = fnv_bytes(h, &c->has_set, sizeof(c->has_set));
            h = fnv_str(h, c->target_name);
            h = fnv_str(h, c->target2_name);
            for(int p = 0; p < 2; p++) { h = fnv_str(h, c->pilot[p]); h = fnv_str(h, c->har[p]); }
        }
    }
    return h;
}

bool story_save_exists(const char *path) {
    FILE *f = fopen(path, "rb");
    if(f) fclose(f);
    return f != NULL;
}

// Writes s with tabs and line breaks replaced by spaces, so each save field stays on one line.
static void put_clean(FILE *f, const char *s) {
    for(; *s; s++) fputc(*s == '\t' || *s == '\n' || *s == '\r' ? ' ' : *s, f);
}

bool story_save(const StoryRun *run, const char *path, char *err, size_t err_size) {
    char tmp[512];
    if(snprintf(tmp, sizeof(tmp), "%s.tmp", path) >= (int)sizeof(tmp)) {
        fail(err, err_size, path, 0, "the save path is too long");
        return false;
    }
    FILE *f = fopen(tmp, "wb");
    if(!f) { fail(err, err_size, path, 0, "cannot write the save file"); return false; }
    fprintf(f, "OMF2107-STORY-SAVE %d\n", STORY_SAVE_VERSION);
    fprintf(f, "script %08x\n", story_fingerprint(run->story));
    fprintf(f, "scene %s\n", run->story->scenes[run->scene].id);
    fprintf(f, "pc %d\n", run->pc);
    fputs("bg ", f); put_clean(f, run->bg); fputc('\n', f);
    fputs("music ", f); put_clean(f, run->music); fputc('\n', f);
    fputs("art ", f); put_clean(f, run->art); fputc(' ', f); put_clean(f, run->art_effect[0] ? run->art_effect : "none");
    fputc('\n', f);
    for(int i = 0; i < 2; i++) {   // the portraits on stage: image, side, name-plate stage, name
        const StoryPresent *p = &run->present[i];
        if(!p->image[0]) continue;
        fputs("present ", f); put_clean(f, p->image); fprintf(f, " %s %d", i == 0 ? "left" : "right", p->stage);
        if(p->name[0]) { fputc(' ', f); put_clean(f, p->name); }
        fputc('\n', f);
    }
    for(int i = 0; i < run->name_seen_count; i++) { fputs("seen ", f); put_clean(f, run->name_seen[i]); fputc('\n', f); }
    for(int i = 0; i < run->flag_count; i++) {
        fputs("flag ", f); put_clean(f, run->flags[i].name); fputc('=', f);
        put_clean(f, run->flags[i].value); fputc('\n', f);
    }
    for(int i = 0; i < story_log_count(run); i++) {
        const StoryLogEntry *e = story_log_at(run, i);
        fputs("log ", f); put_clean(f, e->speaker); fputc('\t', f); put_clean(f, e->text); fputc('\n', f);
    }
    bool ok = fflush(f) == 0 && !ferror(f);
    ok = fclose(f) == 0 && ok;
    if(!ok) { remove(tmp); fail(err, err_size, path, 0, "the save file could not be written"); return false; }
    remove(path);  // rename does not replace an existing file on Windows
    if(rename(tmp, path) != 0) { remove(tmp); fail(err, err_size, path, 0, "the save file could not be replaced"); return false; }
    return true;
}

bool story_load_save(StoryRun *run, const Story *story, const char *path, char *err, size_t err_size) {
    if(err && err_size) err[0] = 0;
    FILE *f = fopen(path, "rb");
    if(!f) { fail(err, err_size, path, 0, "cannot open the save file"); return false; }
    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    fseek(f, 0, SEEK_SET);
    if(size <= 0 || size > 1 << 20) { fclose(f); fail(err, err_size, path, 0, "the save file is empty or too large"); return false; }
    char *text = malloc((size_t)size + 1);
    if(!text) { fclose(f); fail(err, err_size, path, 0, "out of memory"); return false; }
    size_t got = fread(text, 1, (size_t)size, f);
    fclose(f);
    text[got] = 0;

    StoryRun tmp;
    memset(&tmp, 0, sizeof(tmp));
    tmp.story = story;
    char scene_id[STORY_NAME] = "";
    bool have_scene = false, have_pc = false, have_script = false;
    unsigned script = 0;
    int pc = 0, line = 0;
    bool ok = true;
    for(char *p = text; ok && *p;) {
        char *eol = strchr(p, '\n');
        if(eol) *eol = 0;
        char *l = p;
        p = eol ? eol + 1 : p + strlen(p);
        line++;
        size_t len = strlen(l);
        if(len && l[len - 1] == '\r') l[--len] = 0;
        if(!len) continue;
        if(line == 1) {
            const char *magic = "OMF2107-STORY-SAVE ";
            if(strncmp(l, magic, strlen(magic)) != 0) { fail(err, err_size, path, line, "not a story save file"); ok = false; break; }
            int version = atoi(l + strlen(magic));
            if(version != STORY_SAVE_VERSION) {
                fail(err, err_size, path, line, version > STORY_SAVE_VERSION ?
                     "this save was written by a newer build (format version %d; this build reads version %d)" :
                     "this save uses an old format (version %d) that this build (version %d) cannot read",
                     version, STORY_SAVE_VERSION);
                ok = false;
            }
            continue;
        }
        if(strncmp(l, "script ", 7) == 0) { script = (unsigned)strtoul(l + 7, NULL, 16); have_script = true; }
        else if(strncmp(l, "scene ", 6) == 0) { have_scene = copy(scene_id, STORY_NAME, l + 6); ok = have_scene; }
        else if(strncmp(l, "pc ", 3) == 0) { pc = atoi(l + 3); have_pc = true; }
        else if(strncmp(l, "bg", 2) == 0 && (l[2] == ' ' || l[2] == 0)) { ok = copy(tmp.bg, sizeof(tmp.bg), l[2] ? l + 3 : ""); }
        else if(strncmp(l, "music", 5) == 0 && (l[5] == ' ' || l[5] == 0)) { ok = copy(tmp.music, sizeof(tmp.music), l[5] ? l + 6 : ""); }
        else if(strncmp(l, "art ", 4) == 0) {
            char *space = strrchr(l + 4, ' ');
            if(!space) ok = false;
            else {
                *space = 0;
                ok = copy(tmp.art, sizeof(tmp.art), l + 4) && copy(tmp.art_effect, sizeof(tmp.art_effect), space + 1);
            }
        }
        else if(strncmp(l, "present ", 8) == 0) {
            char *image = l + 8, *side = strchr(image, ' ');
            char *stage = side ? strchr(side + 1, ' ') : NULL;
            char *name = stage ? strchr(stage + 1, ' ') : NULL;   // the stage is a single digit; the name follows a space
            if(!stage) ok = false;   // a portrait without a name ends after its stage
            else {
                *side = 0; *stage = 0;
                if(name) *name = 0;
                StoryPresent *p = &tmp.present[strcmp(side + 1, "left") == 0 ? 0 : 1];
                ok = copy(p->image, sizeof(p->image), image) && copy(p->name, sizeof(p->name), name ? name + 1 : "");
                p->stage = atoi(stage + 1);
            }
        }
        else if(strncmp(l, "seen ", 5) == 0) {   // a portrait whose name plate was already shown
            ok = tmp.name_seen_count < STORY_NAME_SEEN && copy(tmp.name_seen[tmp.name_seen_count], STORY_NAME, l + 5);
            if(ok) tmp.name_seen_count++;
        }
        else if(strncmp(l, "flag ", 5) == 0) {
            char *eq = strchr(l + 5, '=');
            if(!eq || eq == l + 5 || tmp.flag_count >= STORY_MAX_FLAGS) ok = false;
            else {
                *eq = 0;
                StoryFlag *fl = &tmp.flags[tmp.flag_count++];
                ok = copy(fl->name, STORY_NAME, l + 5) && copy(fl->value, STORY_NAME, eq + 1);
            }
        } else if(strncmp(l, "log ", 4) == 0) {
            char *tab = strchr(l + 4, '\t');
            if(!tab || tmp.log_total >= STORY_LOG) ok = false;
            else {
                *tab = 0;
                StoryLogEntry *e = &tmp.log[tmp.log_total++];
                ok = copy(e->speaker, STORY_NAME, l + 4) && copy(e->text, STORY_TEXT, tab + 1);
            }
        } else {
            ok = false;
        }
        if(!ok && (!err || !*err)) fail(err, err_size, path, line, "the save file is damaged");
    }
    free(text);
    if(!ok) return false;
    if(!have_script || !have_scene || !have_pc) { fail(err, err_size, path, 0, "the save file is missing its position"); return false; }
    if(script != story_fingerprint(story)) {
        fail(err, err_size, path, 0, "the script changed since this save was made, so it cannot be resumed");
        return false;
    }
    int scene = story_find_scene(story, scene_id);
    if(scene < 0 || pc < 0 || pc >= story->scenes[scene].count) {
        fail(err, err_size, path, 0, "the save points outside the script");
        return false;
    }
    tmp.scene = scene;
    tmp.pc = pc;
    step_to_event(&tmp, false);
    if(tmp.pc != pc) { fail(err, err_size, path, 0, "the save is not at a stopping point"); return false; }
    *run = tmp;
    return true;
}
