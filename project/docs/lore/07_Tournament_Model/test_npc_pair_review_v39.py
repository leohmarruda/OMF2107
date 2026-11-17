import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from npc_pair_review import build_review, UPSET_QUESTIONS
from npc_pair_proposals import PROPOSED_PAIR_WINNERS
from tournament_validator import DEFAULT_KNOCKOUT_WINNERS, GROUPS

class NPCPairReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = build_review()

    def test_exact_complete_pair_coverage(self):
        roster = {name for fighters in GROUPS.values() for name in fighters}
        self.assertEqual(len(roster),12)
        self.assertEqual(len(self.rows),66)
        self.assertEqual({frozenset((r['fighter_a'],r['fighter_b'])) for r in self.rows},set(PROPOSED_PAIR_WINNERS))

    def test_default_canon_is_never_rewritten(self):
        for pair,winner in DEFAULT_KNOCKOUT_WINNERS.items():
            self.assertEqual(PROPOSED_PAIR_WINNERS[pair],winner)
        for row in self.rows:
            if row['proposal_type'] == 'established_exact_pair':
                self.assertEqual(row['approval_status'],'canonical_default_only')
            else:
                self.assertEqual(row['approval_status'],'pending_individual_approval')
                self.assertEqual(row['editorial_rationale'],'NOT YET SUBSTANTIATED')

    def test_priority_derivation_flagged(self):
        self.assertEqual(sum(r['proposal_type']=='ranking_inherited' for r in self.rows),51)
        self.assertEqual(sum(r['proposal_type']=='ranking_exception' for r in self.rows),8)
        self.assertEqual(sum(r['proposal_type']=='established_exact_pair' for r in self.rows),7)
        self.assertEqual(len(UPSET_QUESTIONS),8)

    def test_sampling_is_not_certified_reachability(self):
        self.assertTrue(all('not exhaustive' in r['observation_scope'] for r in self.rows))
        self.assertEqual(sum(bool(r['observed_npc_occurrences_in_384_test_inputs']) for r in self.rows),21)

if __name__=='__main__':
    unittest.main()
