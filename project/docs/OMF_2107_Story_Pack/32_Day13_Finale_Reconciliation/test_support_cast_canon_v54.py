"""D13-06 support-cast canon, v5.4.

Ratified rule (Option A+C from the drafted decision, approved by the author):
Angel/Ren/Plug are the default technical trio when not playing; Crystal
(investigation/comms), Mara (worker-safety/labor-liaison) and Ari
(HAR-deployment support) take their own specialties when not playing. The
roster itself is prose, not something this test can verify. What *is*
mechanically testable, per the three constraints adopted alongside the
roster, is that no campaign's Day-13 finale text ever credits a
non-selected pilot with physically damaging the executive gateway G --
G-credit belongs only to the selected pilot (or their own HAR, or "the
player"), in every one of the twelve campaigns, never to one of the other
eleven named pilots appearing as support cast in that scene.

This does not re-verify the G-damage *wording* itself (test_day13_reconciliation.py
and the per-campaign route validators already do that); it verifies the
narrower, cross-campaign invariant that only a support-cast mix-up could
violate: that some *other* named pilot was never substituted in as the one
who lands the blow.
"""
import csv, re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
PILOTS = {'Ari', 'Lyra', 'Mara', 'Ren', 'Angel', 'Crystal', 'Raven',
          'Jean-Paul', 'Steffan', 'Dante', 'Selene', 'Milano'}
# G-damage phrasing varies a lot per campaign (confirmed across all 12
# active scripts: "damages Nova's executive suppression gateway **G**",
# "Jaguar ... damages executive gateway **G**", "feint damages the local
# executive-suppression gateway **G**", "strikes the exposed G housing",
# etc.) -- rather than chase every verb-phrase permutation, flag any
# clause that contains a damage/strike verb *and* a standalone reference
# to G (bold or not) or "gateway" anywhere in the same clause.
_DAMAGE_VERB = re.compile(
    r'\b(damages?|damaged|strikes?|struck|disables?|disabled|breaks?|broke|broken)\b',
    re.IGNORECASE,
)
_G_REFERENCE = re.compile(r'\*{0,2}\bG\b\*{0,2}|\bgateway\b', re.IGNORECASE)

def _scene_block(path: Path, scene_ids: str) -> str:
    """Extract from the first scene id's heading through (not including) the
    next heading at the same or shallower '#' depth that is not itself one
    of this row's own scene ids -- handles Ari's two-scene, sub-headed
    finale the same as every other campaign's single flat heading."""
    ids = [s.strip() for s in scene_ids.split(';')]
    lines = path.read_text(encoding='utf8').splitlines()

    def heading_depth(line: str) -> int:
        stripped = line.lstrip()
        return len(stripped) - len(stripped.lstrip('#')) if stripped.startswith('#') else 0

    def matches_any_id(line: str) -> bool:
        norm = line.replace(' ', '').upper()
        return any(i.replace(' ', '').upper() in norm for i in ids)

    start = next((i for i, l in enumerate(lines) if heading_depth(l) and matches_any_id(l)), None)
    assert start is not None, f'no heading found for {scene_ids!r} in {path}'
    start_depth = heading_depth(lines[start])
    end = len(lines)
    for j in range(start + 1, len(lines)):
        d = heading_depth(lines[j])
        if d and d <= start_depth and not matches_any_id(lines[j]):
            end = j
            break
    return '\n'.join(lines[start:end])

class SupportCastCanonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (HERE / 'DAY13_POV_ACCESS_MATRIX_v3.4.csv').open(newline='', encoding='utf8') as f:
            cls.rows = list(csv.DictReader(f))

    def test_g_credit_never_assigned_to_a_non_selected_pilot(self):
        """For every damage-verb occurrence that is about G (a G/gateway
        reference appears within the same clause, looking forward), check
        only the SUBJECT span immediately before the verb (back to the
        previous clause boundary) for another pilot's name. This pack's own
        boilerplate consistently puts the true actor right before the verb
        and any support cast *after* it (joined by comma/semicolon/while/as
        into the same sentence, e.g. "Lyra's feint damages G while Plug and
        Angel isolate R") -- so a forward-only subject window avoids
        flagging the support cast named in that trailing clause, while
        still catching a real mis-credit (another pilot's name appearing as
        the actual subject of the damage verb)."""
        violations = []
        matched_pilots = set()
        clause_start = re.compile(r'[.!?;]')
        for r in self.rows:
            pilot = r['pilot']
            block = _scene_block(ROOT / r['source'], r['scene_ids'])
            for verb_match in _DAMAGE_VERB.finditer(block):
                forward_window = block[verb_match.end(): verb_match.end() + 120]
                if not _G_REFERENCE.search(forward_window):
                    continue  # this damage verb isn't about G at all
                matched_pilots.add(pilot)
                prior_boundary = max(
                    (m.end() for m in clause_start.finditer(block[:verb_match.start()])),
                    default=0,
                )
                subject_span = block[prior_boundary:verb_match.start()]
                for other in PILOTS - {pilot}:
                    if re.search(rf'\b{re.escape(other)}\b', subject_span):
                        violations.append(
                            f"{r['source']} ({pilot}'s finale): {other!r} appears as the "
                            f"subject immediately before a G-damage verb: "
                            f"{subject_span.strip()!r} [{verb_match.group()}]"
                        )
        # Sanity check on the check itself: every one of the 12 campaigns
        # must contain at least one G-damage clause, or the regex above has
        # gone stale/too narrow and this test would be silently vacuous for
        # whichever pilots it stopped matching -- exactly the kind of
        # silent-pass failure mode this review found elsewhere in the pack.
        missing = PILOTS - matched_pilots
        self.assertEqual(missing, set(),
            f'no G-damage clause detected for: {sorted(missing)} -- '
            f'the detector regex may be stale, not that the scenes lack one')
        self.assertEqual(violations, [], '\n' + '\n'.join(violations))

if __name__ == '__main__':
    unittest.main()
