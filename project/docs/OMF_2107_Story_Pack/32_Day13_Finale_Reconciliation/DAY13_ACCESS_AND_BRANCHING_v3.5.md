# Day-13 access and branching implementation — v3.5 (ratified v5.4)

**Status:** ratified canon as of v5.4 for the authorization chain, zone adjacency and clearance-authority points below; see each point for what changed. Applies separately to each selected-pilot save.

## Authorization chain and safe route

1. Official `FINAL` is concluded and declared separate from the emergency. Champions and eliminated pilots face the **same** independent emergency safety review.
2. An emergency safety decision checks available qualified personnel, machine integrity, contaminated/compromised credentials, and whether the selected pilot is the safest available deployment. It explicitly records `cleared` or `denied`; WAR employment, fame, sponsorship, championship, and previous access cannot substitute. **Ratified (v5.4): this review is deliberately impersonal** — no named safety office, committee, or individual ever issues the decision; "an independent emergency safety review" stays exactly that, in every save, matching what the active text already implied everywhere and avoiding any invented security personnel/credentials.
3. If cleared, pilot equipment is inspected at **Z0**. Pilot moves under controlled escort to the **Z2** combat enclosure, which contains **Z3** (the protected retention/core subsystem — not a separate entrance for pilot or executives). Independent technicians operate from **Z1**. **Ratified adjacency (v5.4): Z1 is a hub connected to Z0 and Z4 by corridor, and to Z2/Z3 only by data/command lines — never a walkable door.** Technicians are never physically in the same room as the live Nova chassis; this is the literal reading of "isolated command/data paths" below, now canon rather than a functional abstraction.
4. If denied, combat is conducted by one independently cleared non-player pilot *within that alternative history*; a selected-player noncombat path is presently supported only for **Raven**. Other selected pilots require a compatible cleared deployment or the route pauses for authoring—not magical access.
5. After G is damaged and R isolated, commands for D and physical shutter/seal must occur only after the qualified crew's personnel-clear confirmation. The pilot retreats along their designated Z2→Z0 withdrawal corridor; crew evacuates to **Z4**. No NPC is simultaneously both an exclusive player boss and the same save's other protagonist.
6. Core escape E starts only after destruction D passes its irreversible point. Kreissack engages B→L independently, then destruction completes. Evidence for subsequent oversight is retained outside the destroyed core, but authenticated E5 remains Day 30.

## Selected protagonist ownership

- **Dante**: selected-player Shredder action damages G. Angel's verified timing window and independent technician R isolation do not replace the playable action.
- **Selene**: selected-player machine damages G; authenticated supplier records enable local maintenance isolation but never corporate remote domination of Nova. Technical team performs R isolation.
- **Raven, cleared**: selected-player Katana damages G; separate technician isolation.
- **Raven, denied**: selected player verifies map, coordinates safety extraction, and transmits a safe route; independent cleared fighter damages G. If he refuses or supplies inadequate evidence, team relies on its slower independent survey; Raven gains neither clearance nor boss-credit. This is the *ratified authoring exception* (v5.3) to blanket 'all selected pilots win SPECIAL_NOVA'.
- **Steffan** (added v5.3, same pattern as Dante/Selene above): selected-player Pyros fire-control lock damages G; technicians protected by his clearance corridor perform R isolation, not credited with damaging G themselves.

## Decisions still requiring approval

- ~~Whether the Raven noncombat exception is final canon or remains a provisional gameplay exception.~~ **Decided (v5.3): final canon.** Option B is ratified — see `DAY13_RECONCILIATION_v3.4.md` D13-03. `finale_flow.py` and the active R6.3 text already matched this exactly; nothing in code or prose changed, only the open-decision status.
- ~~Exact Z0–Z4 facility adjacency, personnel authority and signage.~~ **Decided (v5.4): hub topology + impersonal authority.** See points 2–3 above.
- ~~Explicit failure/retry presentation, stakes and timings for Dante, Selene and Raven.~~ **Decided (v5.5).** Dante's and Selene's active text already stated retry-from-checkpoint on a failed strike. Raven's cleared/combat branch did not; one sentence appended (no line-number shift) stating the same retry-from-checkpoint behavior, and clarifying that his noncombat branch's failed/withheld map is final for that attempt (losing the chance to shape the extraction), not retried the way a combat strike is — those are different kinds of failure by design, not an oversight.
- ~~Cross-route fully qualified support cast for each alternative save.~~ **Decided (v5.4).** See `DAY13_RECONCILIATION_v3.4.md` D13-06 and `test_support_cast_canon_v54.py`.

## Safeguards

No route changes the official trophy. No alternative ending lets Nova's *unique* core escape. No unauthenticated early E5 evidence. Kreissack alone chooses latch engagement through B→L. Player choice cannot coerce another character to consent.
