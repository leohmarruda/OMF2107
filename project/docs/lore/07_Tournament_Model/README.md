# OMF 2107 — Executable Tournament Branch Model v0.1

**Status:** Working implementation and route consistency test; **not a final gameplay or NPC outcome specification**. Built from the current five-act outline and story-repair archive, including the user's November 1 clarification that **there are no drawn fights**.

## A. Decisive fights: rule and mathematical consequence

Every official battle produces **exactly one winner and one loser**. No drawn bouts, shared victory, disqualification-as-draw or third-result state exists in the validator.

There are four groups with three pilots each. Each pilot has two group fights, and the top two advance to the eight-pilot elimination stage. With no drawn fights, a three-pilot group's final win records are **either**:

- `2–0, 1–1, 0–2`: a unique ranking, no extra rule needed; **or**
- `1–1, 1–1, 1–1`: a *circular ranking*, e.g., A defeats B, B defeats C, C defeats A. This does **not** mean that any fight ended in a tie.

Under the currently agreed four-groups-of-three format, a circular ranking cannot be resolved by head-to-head alone. Three separate possibilities are open: (i) a **prepublished seed** to distinguish circular records (the current **provisional** implementation), (ii) a genuine in-game statistic across fights, provided it is actually measured for both human and NPC combat, or (iii) an extra decisive playoff with associated match/pacing costs. None has been canonized by the user. **Do not present the provisional seed as an approved gameplay rule.**

## B. Graph model

The group participants and default match results are transcribed from `Story_Repair_Pack_v0.2.md`. Ranking outputs feed exactly:

- Q1 = A1 vs B2
- Q2 = A2 vs B1
- Q3 = C1 vs D2
- Q4 = D1 vs C2
- S_AB = winner(Q1) vs winner(Q2)
- S_CD = winner(Q3) vs winner(Q4)
- FINAL = winner(S_AB) vs winner(S_CD)

All these matches are decisive. The later **Nova fight is outside the official competition**. A defeated selected pilot can still access it through a separately scripted credible intervention; the validator does not assign the championship to such a pilot.

## C. Canon boundary: NPC behavior

`DEFAULT_GROUP_WINNERS` encodes established default group results. For other knockout pairings that appear when the player changes results, the script's `DEFAULT_KNOCKOUT_WINNERS` stores the seven exact-pair outcomes from the default cinematic bracket; `NPC_KNOCKOUT_PRIORITY` is a **test fallback only for other pairings**. That fallback ordering between pilots is **not story canon**. All such matches are explicitly tagged `provisional_npc_priority_NOT_CANON` in output. `npc_knockout_winners` can supply authored pair outcomes instead.

`CYCLE_SEED` is similarly **provisional**. The goal here is to demonstrate consistency for every pilot, not to decide an unresolved gameplay design question by stealth.

## D. Running the validator

Requires Python 3.10 or newer; no packages needed.

```bash
# From the directory containing the script:
python3 tournament_validator.py --pilot Ari --group-wins 01 --knockout-wins 111 --brief

# Ari beats both group rivals and therefore faces Ren in Q1, not Mara in Q2:
python3 tournament_validator.py --pilot Ari --group-wins 11 --knockout-wins 111

python3 -m unittest discover -s . -p 'test_*.py' -v
```

`group-wins` has two binary outcomes for the selected pilot's group matchups in the fixed tuple order in `GROUPS`; `knockout-wins` is up to three outcomes consumed as and when the selected pilot faces quarterfinal, semifinal and final. `1` means **the player won that fight**, and `0` means **the player lost it**, not that there was a draw.

## E. Validation performed

- Exact default Ari path and legitimate champion.
- First-place Ari changes from Q2 (against Mara) to Q1 (against Ren).
- A defeated Ari does not become official tournament champion.
- Circular group record resolved with a provisional published ranking without inventing a drawn fight.
- All 12 pilots × 4 binary group outcome patterns × 8 binary knockout decision strings: **384 simulated inputs**, all with 12 valid group fights and seven valid knockout fights.
- Each of the 12 pilots can become champion through three successive knockout victories after winning their two group fights.

This verifies mechanical consistency *under the provisional NPC and circular-order rules*. It does not prove route dialogues, player challenge, dramatic quality, economic consequences or feasibility of all branch cinematics.

## F. Next unresolved decisions

1. Choose the public ranking procedure for a 1–1–1 circular group. Prefer a metric the fighting game truly measures if available; otherwise agree on prepublished seeding rather than smuggling in untracked health or round statistics.
2. Replace arbitrary NPC knockout fallback results with an authored outcome matrix or clear tournament simulation principles.
3. Add story-route event tests checking that all champion lines, character scenes, romance flags, Nova encounter entrances and epilogues match actual results.
4. Test fight count and pacing in the short arcade mode and longer cinematic mode. Avoid introducing needless rematches.

## G. v3.6 integration audit (noncanonical alternatives explicitly exposed)

Run `python3 tournament_audit.py`. The generated `audit_outputs/route_matrix.csv` contains every one of 384 input tuples and records consumed knockout choices, elimination, circular groups, provisional match IDs and whether the outcome uses only currently documented rules. `summary.json` aggregates the coverage. There are 144 distinct player paths after removing ignored choices. The `canon_ready` field is **narrow**: it certifies only tournament resolution provenance, not screenplay continuity, game difficulty, or author approval of the circular-ranking policy.

`simulate(..., require_authored=True)` rejects unapproved circular seeds and fallback NPC winners. Pass an explicit valid `cycle_seed` to indicate that a policy has been provided *for that run*; this does not make it project canon. Pass explicit `npc_knockout_winners` for alternative matchups. The default cinematic bracket's seven specific pair outcomes have been recorded as authored defaults, not extrapolated into a universal ability ranking.

**Still needs author decision:** a public circular-ranking rule (seed/recorded score/extra playoff); an NPC outcome procedure for all reachable nondefault pairings; and whether the tournament narrative should display secondary results in branches where the player was eliminated. Do not treat an arbitrary ranking of pilot strength as an approved narrative outcome.

## H. v3.7 decisions — current authority

**D1 approved:** Use scores the game already tracks as the group-stage 1–1–1 tiebreak. The working interface takes **both fighters' numeric match scores** for each group fight and ranks equal-win pilots by cumulative score across their two matches. Official score definition, normalization and handling of equal cumulative scores are *not* yet approved. Missing or tied totals must block strict validation. The historical `CYCLE_SEED` is a simulation-only fallback, not an approved secondary rule.

**D2 approved method, not outcomes:** deterministic explicit pair results for NPC-only knockout fights. `npc_pair_proposals.py` contains a complete review-pending table; it is opt-in via `use_proposed_npc=True` and still fails `require_authored=True`. Approved default cinematic results take precedence. Do not describe proposed winners as canon. For strict operation, pass approved `npc_knockout_winners` entries instead.

**Screenplay integration:** `tournament_scene_state.py` produces branch-conditioned champion, semifinalists, elimination, group standings, and final participants. `TOURNAMENT_INTEGRATION_v3.7.md` lists the binding contract and editorial review tasks.
