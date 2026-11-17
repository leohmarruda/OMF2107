import csv
import unittest
from pathlib import Path
HERE=Path(__file__).parent
class TestDossiers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (HERE/'NPC_PRIORITY_MATCHUP_DOSSIERS_v4.0.csv').open(encoding='utf-8') as f:cls.rows=list(csv.DictReader(f))
        with (HERE/'NPC_PAIR_EDITORIAL_REVIEW_v3.9.csv').open(encoding='utf-8') as f:cls.baseline=list(csv.DictReader(f))
    def test_exact_sample_pending_coverage(self):
        expected={frozenset((r['fighter_a'],r['fighter_b'])) for r in self.baseline if int(r['observed_npc_occurrences_in_384_test_inputs'])>0 and r['proposal_type']!='established_exact_pair'}
        actual={frozenset(r['pair'].split('|')) for r in self.rows}
        self.assertEqual(expected,actual)
        self.assertEqual(len(self.rows),14)
    def test_statuses_and_counterplay(self):
        for r in self.rows:
            self.assertEqual(r['decision_status'],'editorial_hypothesis_not_approved')
            for field in ('conditional_win_mechanism','credible_counterplay','required_scene_evidence','downstream_continuity_check'):
                self.assertGreater(len(r[field]),50)
    def test_draft_winners_match_provenance(self):
        baseline={frozenset((r['fighter_a'],r['fighter_b'])):r for r in self.baseline}
        for r in self.rows:
            self.assertEqual(r['draft_winner'],baseline[frozenset(r['pair'].split('|'))]['proposed_winner'])
            self.assertEqual(r['sample_occurrences'],baseline[frozenset(r['pair'].split('|'))]['observed_npc_occurrences_in_384_test_inputs'])
if __name__ == '__main__':unittest.main()
