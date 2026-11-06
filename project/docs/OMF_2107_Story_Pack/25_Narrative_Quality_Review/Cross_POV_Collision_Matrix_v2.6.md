# OMF 2107 — NPC relationship collision and scene synchronization matrix v2.6

**Status:** Production specification and editorial to-do. None of the proposed romances below becomes canon by listing it. Many pairings are alternatives in different *selected-pilot* saves; they do not all occur at once.

## Romance / counterpart constraints

| Character shared by multiple routes | Relevant competing routes (not simultaneous) | Default / independent decision requirement | Critical cross-POV check |
|---|---|---|---|
| **Lyra** | Dante → Steffan (default historical triangle); possible Alex post-tournament; optional other single outcomes | Lyra independently chooses breakup/reconciliation; signed media/recusal guard for Alex; Dante default nonromantic toward Steffan | No Steffan ownership of Lyra; verify actual Day-11 separation before any Steffan–Dante romance |
| **Dante** | Lyra, proposed post-tournament Steffan, proposed Mari | Default toward Steffan **nonromantic**; possible new feelings only after three-stage player path; independent Steffan choice | A Steffan player's desire cannot create Dante's reciprocal attraction |
| **Steffan** | Lyra relationship, proposed elective Dante future | Steffan admires/denies attraction to Dante in canon; real attraction to Lyra too; controlling conduct has consequences | His Day-11 confrontation must be identical history in both POVs |
| **Mara** | Ari, proposed Plug, proposed Raven | Independent financial, privacy and career decisions; no prize/trophy substitutes for choice | A Raven campaign cannot claim Mara while she is committed to Ari/another person |
| **Ari** | Mara, proposed Leena | Ganymede evidence independent; Ari alone does not decide Leena's interest | Leena's availability must be reconciled with her other proposed routes |
| **Leena** | Ari, Angel, Christian (proposed) | Independent journalism, recusals, single relationship state | No three concurrent romance epilogues; journalist never trades publication for intimacy |
| **Ren** | Angel, proposed Tessa | Neural symptoms/consent and confidentiality are not romance flags | Angel commitment must agree across Ren and Angel POVs |
| **Angel** | Ren, Crystal, Leena (proposed) | Age/identity/privacy, mutual availability; Crystal must have resolved Raven path | Her identity disclosure cannot become involuntary cost of dating |
| **Crystal** | Raven, proposed Angel | Desire for Raven can be involuntary; acting on it cannot be coerced; Raven's acts must be disclosed | No romantic payoff on first encounter with proof of shuttle culpability; Christian evidence survives Raven refusal |
| **Raven** | Crystal, proposed Mara | Historical facts fixed; intentional exploitation cannot be undone by romance flags | Distinguish coerced compliance, consensual D/s, and rejection; no crossover double commitment |
| **Jean-Paul** | Varga, proposed Selene | Varga's violations real, not romance-created; independent separation/accountability | A Selene player's flirt does not resolve Varga's existing relationship |
| **Selene** | Milano, Jean-Paul | Maintain identity/corporate agency; independently signal availability & reciprocal choice | Milano's model may not unlock her consent merely by succeeding in negotiations |
| **Milano** | Selene | Conflict-of-interest and leverage separation | Validate both sides of proposal at same timestamp and relationship version |
| **Christian** | proposed Leena | His investigation must proceed even if she does not date him | Journalistic ethics and evidence provenance unaffected |
| **Cossette / Ibrahim** | Existing established couple (supporting role) | Preserve established relationship unless explicitly authored change | Do not accidentally treat cameo availability as being single |

## Global event IDs, ownership and visibility

| Canon event | When | Owner | What can vary |
|---|---|---|---|
| `GROUP_MATCh` | Group stage | Tournament model | Player-result binary winners, never draws |
| `K_BIO` | Day 9 midpoint | Ren/Angel validate; player can learn via scoped independent disclosure | Protagonist's interpretation and access path—not Kreissack's survival |
| `VARGA_EVIDENCE` | Days 8–11; Lyra receives protected proof Day 11 | Jean-Paul / independent protected delivery | Public response, privacy, accountability; no fight rigging |
| `DANTE_STEFFAN_PRIVATE` | Day 11 | Dante and Steffan | Dante's tone and elective future curiosity; Steffan cannot dictate response |
| `SF_AB` | Day 11 | Tournament model | Actual qualified contestants and winner |
| `RESCUE` | Day 12 (before C/D semifinal) | Nova autonomous rescue, false command attribution | Person witnessing/helping; not whether rescue was real |
| `SF_CD` | Day 12 after rescue | Tournament model | Actual qualified contestants and winner |
| `FINAL` | Day 13 before Nova emergency | Tournament model | Actual qualified finalists and champion |
| `NOVA_CORE` | Day 13 after tournament final | Same real physical world event, witnessed from different positions | Each protagonist's access/action/reaction, not Nova surviving by default |
| `DEVROE_ORDER_E5` | Day 30 | Christian independent authentication | Audience/player knowledge in epilogue; legal/public response after proof |

**Conflict policy:** A chosen protagonist's dialogue choices are commands only for that protagonist. NPC responses are autonomous, scheduled, mutually exclusive, and evidence/time-dependent. Default off-player scripts must never ignore earlier independent NPC decisions. Incompatible commits produce a blocked route and alternate dialogue, not a silent overwrite.

## Minimum global-world save contract

- `player_pilot`, stable world event clock, and official bracket result IDs.
- Per-person **availability, consent, commitment, breakup timestamps and context**; a one-sided proposed future is *not* a committed couple.
- Narrative scene IDs and event IDs separated from prose scene headings.
- Evidence knows `source`, `custody`, `earliest_verified_day`, and separately `character_knows` versus `audience_knows`.
- NPC consent and professional conflict status cannot be injected by player convenience as unverified flags.
- One actual Day-13 Nova destruction event; one Day-30 authenticated order. No route calls a second historic physical sacrifice.
