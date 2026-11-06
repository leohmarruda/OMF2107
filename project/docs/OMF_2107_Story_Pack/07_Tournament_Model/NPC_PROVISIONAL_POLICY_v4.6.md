# NPC offscreen outcome policy — v4.6

Author decision, 2026-11-03: **the remaining 51 proposals are provisionally approved**, not finally signed-off canon. Seven existing cinematic winners and eight individually author-approved winners retain higher authority.

- **Development/preview:** use `npc_provisional_v46.effective_preview_winners()` for all 66 knockout pairs. No NPC-vs-NPC fight footage or choreography.
- **Final-canon audit:** `npc_outcome_registry.current_author_approval_status()` continues reporting the 51 as not individually finalized. Do not silently promote them.
- **Precedence:** cinematic canon > eight explicit v4.5 author choices > 51 v4.6 provisional outcomes. In particular Mara–Steffan is won by Steffan, despite the older `npc_pair_proposals.py` value.
- **Game state:** the resolved winner must feed bracket display and route dialogue. Numeric score remains unavailable unless recorded by the actual game scoring system.
- **Revision rule:** revisit a provisional outcome only when a continuity conflict or substantially better matchup rationale arises; no need for 51 separate approval sessions.

The next development priority is cross-campaign relationship-state consistency and reciprocal choice gates.
