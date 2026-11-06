import csv, unittest
from pathlib import Path
from tournament_validator import DEFAULT_KNOCKOUT_WINNERS
from npc_pair_reachability import reachability

class TestNpcApprovalLedger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        p=Path(__file__).with_name('NPC_OUTCOME_APPROVAL_LEDGER_v4.3.csv')
        cls.rows=list(csv.DictReader(p.open(encoding='utf-8')))
    def test_exactly_reachable_pairs(self):
        self.assertEqual({frozenset((r['fighter_a'],r['fighter_b'])) for r in self.rows},set(reachability()))
        self.assertEqual(len(self.rows),66)
    def test_canon_pinned_and_pending_not_approved(self):
        self.assertEqual(sum(bool(r['established_winner']) for r in self.rows),7)
        self.assertEqual(sum(r['status']=='PENDING_AUTHOR_APPROVAL' for r in self.rows),59)
        for r in self.rows:
            pair=frozenset((r['fighter_a'],r['fighter_b']))
            self.assertEqual(r['established_winner'], DEFAULT_KNOCKOUT_WINNERS.get(pair,''))
            if r['status']=='PENDING_AUTHOR_APPROVAL':
                self.assertEqual(r['approval_decision'],'')
                self.assertEqual(r['approved_by'],'')
                self.assertEqual(r['approval_date'],'')
            self.assertIn(r['proposed_winner'],pair)
    def test_all_stages(self):
        self.assertEqual({stage for r in self.rows for stage in r['possible_rounds'].split('/')},{'QF','SF','Final'})
    def test_dossiers_not_authority(self):
        for r in self.rows:
            if r['proposal_origin']=='ranking_exception':
                self.assertEqual(r['priority'],'P0')
