# OMF 2107 — Integration Overview v2.0

**Date:** 2 November 2026  
**Scope:** Jean-Paul selected-pilot campaign *The Observer Effect* (eight total selected-pilot storylines). Adds chaptered screenplay, route specification, executable validator, 20 new consistency/chronology tests, and corresponding index/decision-log updates. Existing original source texts, character bios, and seven earlier active campaigns remain unchanged.

## Core new story

Jean-Paul, age 37 and piloting Shadow, begins as a charming intelligence broker who treats both romantic attention and secrets as commodities. His involvements with Varga become an epistemic and moral trap: he genuinely wants her, and she genuinely wants him, yet her independent unauthorized emotional experiment deliberately rearranges meetings and gathers data without adequate informed consent. Jean-Paul himself infiltrates and may try to profit from the information, so he has no morally simple outsider position. The plot distinguishes unethical experiment, informed desire, romantic reconciliation, and documented accountability.

- **Default competition:** losses to Angel `GD2` and Dante `GD3`, elimination D3. No invented quarterfinal; an independent investigation continues.
- **Alternative competition:** D1 goes `Q4` against C2, D2 goes `Q3` against C1, D3 does not qualify. Semifinal is `S_CD` after Day-12 rescue if actual QF was won. Day-13 `FINAL` only if actual SF won. Championship only by official final win, never romance or intelligence work.
- **Instinct vs control:** Varga influences circumstances and obtains unauthorized study data but cannot manufacture love or rig matches. Kreissack's biological survival is discovered via independent Angel/Ren evidence in Days 8–10; executive veto is not confirmed until Day 13.
- **Relationship branches:** Varga is the central mutual-attraction arc, with an optional earned-but-not-exculpatory later romance. Selene is a provisional alternative requiring actual independence from Milano; friendship and solo endings are complete options. Stylish fundraiser, flirtatious sparring banter, a private dance and optional implied intimacy offer fanservice without substituting for plot.
- **Ethical branches:** independent disclosure, private escrow, compromised brokerage, testimony and self-serving spin have character and legal consequences. None erases participant notices, Lyra's independent choices, or the separately discovered evidence.

## Shared-event integration

- Day 0: legacy procurement discrepancy.
- Days 3–7: Group D fights, unauthorized-research suspicion and funding trail.
- Days 8–10: preliminary authenticated Varga evidence and Kreissack biological survival, **without confronting Varga yet**.
- Day 11: Jean-Paul confronts Varga under independent oversight; Lyra receives protected notice through a channel not controlled by him.
- Day 12: genuine rescue, then optional actual `S_CD` semifinal.
- Day 13: optional official final, then unique shared Nova fight. Kreissack uses `B→L` after damage to executive gateway G, prevents E ejecting during D, and dies with Nova. His last line remains “Apparently, I can still surprise you.”
- Day 30: independent Devroe E5 verification of **Kreissack's** 2092 assassination order, never proof available to Jean-Paul during the tournament.

## Verification status

The validator and static chronology checks cover player result mapping (32 five-bit inputs), group circular-seeding edge cases, no fake fights, trophy ownership, ethical/romance exclusivity, participant notice, reveal timing and shared finale invariants. The existing v1.9 source archive's claimed test total of 209 **does not match re-running its test files with standard `unittest` discovery**, which finds 182 individual `test_*` methods. This release adds 20 discovered tests for a total of **202**. If one counts assertions or cases inside loops, numbers may differ; the reproducible count is the `unittest` reported figure. Tests demonstrate local branching logic, not an end-to-end game engine or dramatic quality.

## Pending editorial decisions

1. Whether Selene's romantic interest becomes implemented canon; Selene–Milano's availability is not settled by Jean-Paul's choices.
2. How far Varga is willing to accept accountability; each conditional proposal should preserve independent consequences.
3. Author the alternative NPC knockout outcomes and final public circular-standing rule (no drawn fights are ever introduced).
4. Resolve one unified shared romance state across the eight protagonist alternatives and assess pacing/unique voices in full playthroughs.
