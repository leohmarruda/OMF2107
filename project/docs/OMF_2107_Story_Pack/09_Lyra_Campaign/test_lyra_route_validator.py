import itertools
import unittest
from lyra_route_validator import LyraChoices, choose_ending, interpret, simulate_lyra
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate


class LyraTest(unittest.TestCase):
    def test_default_cinematic_history(self):
        r = simulate_lyra((False,True), (True,True,False))
        self.assertEqual((r['lyra_group_rank'],r['qf_opponent'],r['sf_opponent'],r['final_opponent']),
                         (2,'Angel','Steffan','Ari'))
        self.assertEqual(r['official_champion'],'Ari')
        self.assertEqual(r['relationship_after_L5'],None)
        self.assertEqual(r['possible_main_endings'],('solo',))

    def test_lyra_wins_all_games_and_fights(self):
        r = simulate_lyra((True,True), (True,True,True))
        self.assertEqual(r['lyra_group_rank'],1)
        self.assertEqual(r['qf_opponent'],'Dante')
        self.assertTrue(r['lyra_champion'])
        self.assertNotIn('L6.2_final_broadcast',r['core_scenes'])

    def test_early_elimination_has_full_story(self):
        r = simulate_lyra((False,False), ())
        self.assertFalse(r['qualified'])
        self.assertIn('L4.2_eliminated_group_stage',r['core_scenes'])
        self.assertIn('L5.4_independent_safety_audit',r['core_scenes'])
        self.assertIn('L6.5_nova_boss',r['core_scenes'])
        self.assertEqual(r['qf_opponent'],None)
        self.assertFalse(r['nova_is_official_match'])

    def test_qualified_but_loss_in_qf(self):
        r = simulate_lyra((False,True), (False,))
        self.assertTrue(r['qualified'])
        self.assertIsNone(r['sf_opponent'])
        self.assertIn('L5.4_independent_safety_audit',r['core_scenes'])
        self.assertNotIn('L6.2_final_match',r['core_scenes'])

    def test_all_tournament_inputs_have_consistent_plot_and_no_draws(self):
        # 4 two-group result vectors x 8 future KO input vectors = 32 scenarios.
        for grp in itertools.product([False, True], repeat=2):
            for ko in itertools.product([False, True], repeat=3):
                t = simulate('Lyra', grp, ko)
                r = interpret(LyraChoices(),t)
                self.assertEqual(r['qualified'],t['selected_pilot_advances_from_group'])
                self.assertEqual(r['lyra_champion'],t['player_champion'])
                self.assertEqual(r['official_champion'],t['champion'])
                self.assertIn('L6.5_nova_boss',r['core_scenes'])
                self.assertEqual(len(r['core_clues']),8)
                self.assertTrue(all(m['winner'] != m['loser'] for m in t['matches']))
                self.assertEqual('L6.2_final_match' in r['core_scenes'],
                                 'FINAL' in t['player_match_ids'])

    def test_neural_choice_no_fighting_effect(self):
        r = [simulate_lyra((False,True),(True,True,False),LyraChoices(neural=n))
             for n in ('decline','monitor_only','enhanced')]
        self.assertEqual(len({x['neural_clue_variant'] for x in r}),3)
        for x in r[1:]:
            self.assertEqual(x['official_champion'],r[0]['official_champion'])
            self.assertEqual(x['qf_opponent'],r[0]['qf_opponent'])
            self.assertEqual(x['core_clues'],r[0]['core_clues'])

    def test_dante_steady_route_rejects_other_lovers(self):
        r = simulate_lyra((False,True),(True,True,False), LyraChoices(relationship='stay_dante',
                    alex_mutual_interest=True,alex_adult_verified=True,
                    alex_assignment_finished=True,alex_recused_from_future_lyra_coverage=True,
                    alex_editorial_independence=True))
        self.assertEqual(r['possible_main_endings'],('dante',))
        with self.assertRaises(ValueError): choose_ending(r,'alex')

    def test_clean_breakup_and_breach_both_require_repair(self):
        for rel in ('steffan_clean','steffan_breach','single'):
            r = simulate_lyra((False,True),(True,True,False),LyraChoices(relationship=rel,
                 dante_mutual_recommit=True,dante_accountability_repaired=False,long_repair_interval=True))
            self.assertNotIn('dante',r['possible_main_endings'])

    def test_steffan_reconciliation_is_not_immediate(self):
        base=dict(relationship='steffan_breach',future_steffan=True,steffan_mutual_recommit=True)
        r = simulate_lyra((False,True),(True,True,False),LyraChoices(**base))
        self.assertNotIn('steffan',r['possible_main_endings'])
        r2 = simulate_lyra((False,True),(True,True,False),LyraChoices(**base,long_repair_interval=True))
        self.assertIn('steffan',r2['possible_main_endings'])
        self.assertEqual(choose_ending(r2,'steffan'),'L6.7_steffan')

    def test_alex_age_recusal_mutuality_editorial_all_required(self):
        vals=dict(alex_mutual_interest=True,alex_adult_verified=True,
             alex_assignment_finished=True,alex_recused_from_future_lyra_coverage=True,
             alex_editorial_independence=True)
        self.assertIn('alex',simulate_lyra((False,True),(True,True,False),LyraChoices(**vals))['possible_main_endings'])
        for flag in vals:
            altered=dict(vals); altered[flag]=False
            self.assertNotIn('alex',simulate_lyra((False,True),(True,True,False),LyraChoices(**altered))['possible_main_endings'])

    def test_eligibility_does_not_force_romance(self):
        vals=dict(alex_mutual_interest=True,alex_adult_verified=True,
             alex_assignment_finished=True,alex_recused_from_future_lyra_coverage=True,
             alex_editorial_independence=True)
        r = simulate_lyra((False,True),(True,True,False),LyraChoices(**vals))
        self.assertIn('solo',r['possible_main_endings'])
        self.assertEqual(choose_ending(r,'solo'),'L6.7_solo')

    def test_invalid_old_partner_gates(self):
        with self.assertRaises(ValueError):
            simulate_lyra((False,True),(True,True,False),LyraChoices(relationship='stay_dante',future_steffan=True))
        with self.assertRaises(ValueError):
            simulate_lyra((False,True),(True,True,False),LyraChoices(relationship='single',dante_amicable_separation=True))

    def test_partner_choices_leave_same_bracket(self):
        results=[simulate_lyra((False,True),(True,True,False),LyraChoices(relationship=x)) for x in
             ('stay_dante','steffan_clean','steffan_breach','single')]
        for r in results[1:]:
            for key in ('lyra_group_rank','qf_opponent','sf_opponent','final_opponent','official_champion','core_clues'):
                self.assertEqual(r[key],results[0][key])

if __name__ == '__main__': unittest.main()
