import unittest
from tournament_validator import simulate, GROUPS, DEFAULT_KNOCKOUT_WINNERS
from npc_pair_proposals import PROPOSED_PAIR_WINNERS

SCORES = {'GA1':(10,90),'GA2':(75,20),'GA3':(20,80)}

class ScoreTieBreakTests(unittest.TestCase):
    def test_score_totals_replace_provisional_seed(self):
        result = simulate('Ari',(True,False),(True,True,True),group_match_scores=SCORES, use_proposed_npc=True)
        rank = result['group_standings']['A']
        self.assertEqual(rank['ranked'],['Ari','Selene','Crystal'])
        self.assertEqual(rank['ranking_method'],'group_total_score')
        self.assertEqual(result['audit']['unapproved_cycle_seed_groups'],[])
    def test_missing_or_equal_scores_not_finalized(self):
        with self.assertRaisesRegex(ValueError,'scores missing or tied'):
            simulate('Ari',(True,False),(True,True,True),require_authored=True)
        tied = {'GA1':(10,20),'GA2':(20,10),'GA3':(10,20)}
        with self.assertRaisesRegex(ValueError,'scores missing or tied'):
            simulate('Ari',(True,False),(True,True,True),group_match_scores=tied,require_authored=True)
    def test_invalid_scores_rejected(self):
        for data in ({'ZZ1':(1,2)},{'GA1':(-1,2)},{'GA1':(float('nan'),3)},{'GA1':(True,1)}):
            with self.assertRaises(ValueError):
                simulate('Ari',(False,True),(True,True,True),group_match_scores=data)
    def test_proposals_exhaustively_cover_pairs(self):
        all_fighters = {x for group in GROUPS.values() for x in group}
        from itertools import combinations
        self.assertEqual(set(PROPOSED_PAIR_WINNERS),{frozenset(x) for x in combinations(sorted(all_fighters),2)})
        self.assertTrue(all(w in pair for pair,w in PROPOSED_PAIR_WINNERS.items()))
    def test_proposals_never_overwrite_default_or_player(self):
        r = simulate('Ari',(False,True),(True,True,True),use_proposed_npc=True)
        self.assertEqual(r['champion'],'Ari')
        self.assertEqual(r['audit']['proposed_npc_match_ids'],[])
    def test_strict_rejects_unapproved_proposals(self):
        with self.assertRaisesRegex(ValueError,'Missing approved NPC result'):
            simulate('Ari',(True,True),(True,True,True),use_proposed_npc=True,require_authored=True)

if __name__=='__main__': unittest.main()
