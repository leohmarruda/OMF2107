import itertools
import unittest
from unittest.mock import patch
from tournament_validator import simulate, generate_group_tie_draw, GROUPS

SCORES={'GA1':(5,5),'GA2':(5,5),'GA3':(5,5)}

class RandomThreeWayTieTests(unittest.TestCase):
    def test_six_possible_orders_and_uniform_shuffle_api(self):
        seen=set()
        for perm in itertools.permutations(GROUPS['A']):
            with patch('tournament_validator.secrets.SystemRandom') as rng:
                def arrange(xs, perm=perm): xs[:]=perm
                rng.return_value.shuffle.side_effect=arrange
                seen.add(generate_group_tie_draw('A'))
        self.assertEqual(len(seen),6)

    def test_recorded_draw_sets_standings_and_is_replayable(self):
        draw=['Selene','Crystal','Ari']
        kwargs=dict(group_match_scores=SCORES,tie_draws={'A':draw})
        one=simulate('Crystal',(True,False),(False,),**kwargs)
        two=simulate('Crystal',(True,False),(False,),**kwargs)
        self.assertEqual(one, two)
        self.assertEqual(one['group_standings']['A']['ranked'],draw)
        self.assertEqual(one['group_standings']['A']['ranking_method'],'recorded_uniform_random_draw')
        self.assertEqual(one['recorded_random_tie_draws'],{'A':draw})
        self.assertNotIn('A',one['audit']['unapproved_cycle_seed_groups'])

    def test_strict_mode_requires_recorded_draw(self):
        with self.assertRaisesRegex(ValueError,'three-way tied'):
            simulate('Crystal',(True,False),(False,),group_match_scores=SCORES,require_authored=True)

    def test_rejects_invalid_records(self):
        for record in ({'A':['Crystal','Crystal','Ari']},{'Z':['Ari','Selene','Crystal']},
                       {'A':['Crystal','Ari','Ren']},{'A':['Ari','Crystal']}):
            with self.assertRaises(ValueError):
                simulate('Crystal',(True,False),(False,),tie_draws=record)

    def test_draw_not_used_without_three_way_tie(self):
        scores={'GA1':(8,3),'GA2':(7,4),'GA3':(6,5)}
        r=simulate('Crystal',(True,False),(False,),group_match_scores=scores,
                   tie_draws={'A':['Selene','Ari','Crystal']})
        self.assertEqual(r['recorded_random_tie_draws'],{})

    def test_legacy_seed_only_when_no_recorded_draw(self):
        r=simulate('Crystal',(True,False),(False,),group_match_scores=SCORES)
        self.assertIn('A',r['audit']['unapproved_cycle_seed_groups'])
        self.assertEqual(r['recorded_random_tie_draws'],{})

if __name__=='__main__': unittest.main()
