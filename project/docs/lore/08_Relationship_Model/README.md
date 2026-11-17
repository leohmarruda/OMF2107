# Relationship route model — design validation v0.1

> **Current versions (see `../00_README/CURRENT_FILES.md`):** Current Ari chapters are Chapter 1 v0.6, Chapters 2 to 5 v0.7 and Chapter 6 v0.8 (not the v0.2 versions named below).

**Scope:** Optional social/romance slots and ending selection in Chapters 1–6 **v0.2**. This is an auditable proof-of-concept, not an in-game quest engine and not approval of new couples.

## Separation of concerns

- **Tournament state** is authoritative for combat outcomes and opponents. All fights end in a win and loss. Social flags never modify winner, bracket, combat statistics or ending access to the Nova battle.
- **Main relationship scenes** require positive, independent reciprocal attraction, adult eligibility, no incompatible exclusivity, and any relevant ethical/professional clearances. The scenes still contain player choices: passing the gate does **not** mean a kiss/date was chosen.
- **Supporting interactions** provide technical, investigative, personal or comic material even when romance is refused or unavailable.
- **Global plot** (Ganymede evidence, the neural-link mystery, Nova's autonomy and collapse) does not depend on choosing a romantic partner.

## Integrated optional scenes in v0.2

| Chapter | Insert | Pilot-specific outcome | Nonromantic alternative |
| --- | --- | --- | --- |
| 1 | 2E *The Proper Question* | Ari/Leena rapport | Public records remain accessible |
| 2 | 1B *Off Air* | Lyra/Alex professional rapport | Objective match analysis |
| 2 | 4B *Neon Respite* | Entire playable ensemble fanservice | Workshop/reading lounge |
| 3 | 3B *The Velvet Problem* | Jean-Paul/Varga tension | Suspicion or withdrawal |
| 3 | 5B *Five More Seconds* | Ari/Mara physical chemistry without first kiss | Friendship or sparring |
| 3 | 10B *Two Inventors, One Dance* | Cossette/Ibrahim affectionate comedy | Independent public schematics |
| 3 | Choice 5B update | Ari/Mara optional private evening | Goodnight, discussion, or friendship |
| 4 | 3B *Cooling System* | Mara/Plug invitation if legally/ethically eligible | Working alliance or diagnostics |
| 4 | 4B *The Blue Hour* | Ari/Mara optional intimate night | Conversation, goodnight or distance |
| 5 | 2B *A Clean Chain of Custody* | Ari/Leena future possibility | Investigative collaboration |
| 5 | 5B *The Document You Didn't Burn* | Crystal/Raven possible later trust repair | Independent custody and distance |
| 5 | 7B *Own the Spotlight* | Lyra's controlled glamorous portrait | Solo or no publicity |
| 6 | 15B *No Interview Tonight* | Lyra/Alex optional date only after assignment | Friendship or freedom |
| 6 | 16B *Alternative Relationship Epilogues* | Ari/Leena, Mara/Plug, Crystal/Raven | Friendship/solo personal closures |

## Known limits and unresolved owner decisions

1. This continues the **Ari-focused** six-chapter spine. Inserts for other player characters are scene overlays, not their complete cinematic runs. Full 11 non-Ari storylines are not yet scripted.
2. New romantic pairings (Ari/Leena, Mara/Plug, Lyra/Alex) and exact scenes remain proposals; artist/game writer must approve who genuinely reciprocates and the gender/attraction constraints. Leena, Alex, Plug need verified ages.
3. Some new contacts (e.g. Dante/Steffan, Angel/Ren, JP/Selene) remain in the modular scene-card library and are **not** integrated as full romances yet. They should not be marked implemented.
4. Endings are authored selector scenes. A production state machine must separately record which optional dialogue choice the player actually takes, plus offscreen NPC default histories.
5. Source chapter dialogue still contains Ari-centric references; a future full pilot POV conversion must adapt *all* mandatory scenes, not just insert optional branches.
6. The tournament's circular three-way group ranking rule and nondefault NPC winner selection remain provisional in the separate `07_Tournament_Model`.

## Run checks

From this archive root:

```bash
python -m unittest discover -s 07_Tournament_Model -v
python -m unittest discover -s 08_Relationship_Model -v
```

The relationship checks cover basic eligibility, professional recusals, exclusivity, independent evidentiary review, supportive nonromantic routes, and independence from combat results. These are static/prototype checks, not exhaustive cinematic playtests.
