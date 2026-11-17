import itertools
import unittest
from dataclasses import replace
from ren_route_validator import CORE_CLUES, RenChoices, simulate_ren, interpret, choose_ending
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate

class RenRouteTests(unittest.TestCase):
    def test_default_path(self):
        r = simulate_ren(True,False)
        self.assertEqual(r['ren_group_rank'],2)
        self.assertEqual(r['qf_id'],'Q1')
        self.assertEqual(r['qf_opponent'],'Crystal')
        self.assertEqual(r['player_elimination_match'],'Q1')
        self.assertEqual(r['official_champion'],'Ari')

    def test_group_order_conversion(self):
        r = simulate_ren(True,False)
        t = simulate('Ren',(False,True),(False,False,False))
        self.assertEqual(r['official_champion'],t['champion'])
        self.assertEqual(r['group_match_order_on_screen'],('GB3','GB1'))

    def test_loses_both_no_knockout(self):
        r = simulate_ren(False,False)
        self.assertEqual(r['ren_group_rank'],3)
        self.assertIsNone(r['qf_id'])
        self.assertIn('R4.1b_bench_evidence',r['main_scenes'])
        self.assertIn('R6.3_special_nova',r['main_scenes'])

    def test_wins_both_first_group(self):
        r = simulate_ren(True,True)
        self.assertEqual(r['ren_group_rank'],1)
        self.assertEqual(r['qf_id'],'Q2')

    def test_all_32_input_patterns(self):
        for bits in itertools.product((False,True), repeat=5):
            r=simulate_ren(bits[0],bits[1],bits[2:])
            self.assertIn(r['ren_group_rank'],(1,2,3))
            self.assertEqual(len(r['all_essential_clues']),8)
            self.assertEqual(r['played_final'],r['final_opponent'] is not None)
            self.assertIn('R6.3_special_nova',r['main_scenes'])

    def test_champion_requires_actual_final_win(self):
        r=simulate_ren(True,True,(True,True,True))
        self.assertTrue(r['ren_champion'])
        self.assertEqual(r['official_champion'],'Ren')
        self.assertEqual(r['final_opponent'],'Lyra')

    def test_loss_cannot_be_trophy(self):
        r=simulate_ren(True,True,(True,True,False))
        self.assertFalse(r['ren_champion'])
        self.assertNotEqual(r['official_champion'],'Ren')

    def test_research_does_not_change_fights(self):
        results=[simulate_ren(True,True,(True,False,True), replace(RenChoices(),research_path=p)) for p in ('withdraw','audited','persist_safeguarded')]
        for r in results[1:]:
            self.assertEqual(r['qf_opponent'],results[0]['qf_opponent'])
            self.assertEqual(r['official_champion'],results[0]['official_champion'])

    def test_romance_does_not_change_fights(self):
        one=simulate_ren(True,True,(True,True,True),RenChoices(relationship_intent='angel'))
        two=simulate_ren(True,True,(True,True,True),RenChoices(relationship_intent='tessa'))
        self.assertEqual(one['official_champion'],two['official_champion'])

    def test_angel_requires_reciprocity(self):
        c=RenChoices(relationship_intent='angel',private_interface_isolated=True,angel_current_commitment_cleared=True)
        self.assertNotIn('angel',simulate_ren(True,False,choices=c)['romance_endings_available'])
        self.assertIn('angel',simulate_ren(True,False,choices=replace(c,angel_reciprocates=True))['romance_endings_available'])

    def test_angel_needs_no_other_commitment(self):
        c=RenChoices(relationship_intent='angel',private_interface_isolated=True,angel_reciprocates=True)
        self.assertNotIn('angel',simulate_ren(True,False,choices=c)['romance_endings_available'])

    def test_tessa_requires_mutuality(self):
        c=RenChoices(relationship_intent='tessa',private_interface_isolated=True)
        self.assertNotIn('tessa',simulate_ren(False,True,choices=c)['romance_endings_available'])
        self.assertIn('tessa',simulate_ren(False,True,choices=replace(c,tessa_reciprocates=True))['romance_endings_available'])

    def test_intimacy_requires_capacity(self):
        c=RenChoices(relationship_intent='tessa',private_interface_isolated=True,tessa_reciprocates=True,consent_capacity_clear=False)
        self.assertNotIn('tessa',simulate_ren(True,True,choices=c)['romance_endings_available'])

    def test_intimacy_requires_disconnect(self):
        c=RenChoices(relationship_intent='angel',angel_reciprocates=True,angel_current_commitment_cleared=True)
        self.assertNotIn('angel',simulate_ren(True,True,choices=c)['romance_endings_available'])

    def test_no_concurrent_romance(self):
        c=RenChoices(relationship_intent='angel',angel_reciprocates=True,tessa_reciprocates=True,angel_current_commitment_cleared=True,private_interface_isolated=True)
        r=simulate_ren(True,True,choices=c)
        self.assertIn('angel',r['romance_endings_available'])
        self.assertNotIn('tessa',r['romance_endings_available'])

    def test_nonromantic_always_available(self):
        for c in (RenChoices(relationship_intent='single'), RenChoices(relationship_intent='friendship'), RenChoices(relationship_intent='tessa')):
            self.assertTrue({'single','friendship'} <= set(simulate_ren(False,False,choices=c)['romance_endings_available']))

    def test_missing_repair_blocks_research_review(self):
        c=RenChoices(symptom_disclosure='concealed',research_path='persist_safeguarded')
        self.assertFalse(simulate_ren(True,False,choices=c)['research_resumption_may_be_reviewed'])
        self.assertTrue(simulate_ren(True,False,choices=replace(c,corrected_disclosure=True))['research_resumption_may_be_reviewed'])

    def test_withdraw_remains_research_end(self):
        c=RenChoices(research_path='withdraw')
        self.assertFalse(simulate_ren(True,True,choices=c)['research_resumption_may_be_reviewed'])

    def test_no_auto_research(self):
        for p in ('withdraw','audited','persist_safeguarded'):
            r=simulate_ren(True,False,choices=RenChoices(research_path=p))
            self.assertFalse(r['research_resumption_is_automatic'])
            self.assertFalse(r['symptoms_magically_cured'])

    def test_clues_on_all_paths(self):
        for p in ('withdraw','audited','persist_safeguarded'):
            for wins in itertools.product((False,True),repeat=2):
                r=simulate_ren(*wins,choices=RenChoices(research_path=p))
                self.assertEqual(set(r['all_essential_clues']),set(CORE_CLUES))

    def test_evidence_roles_distinct(self):
        roles={simulate_ren(True,False,choices=RenChoices(evidence_method=m))['evidence_contribution'] for m in ('offline_record','witness_protocol','hardware_isolation')}
        self.assertEqual(len(roles),3)

    def test_cannot_choose_unavailable_romance(self):
        r=simulate_ren(True,False)
        with self.assertRaises(ValueError):choose_ending(r,'angel')
        self.assertEqual(choose_ending(r,'single'),'single')

    def test_bad_values_rejected(self):
        with self.assertRaises(ValueError):simulate_ren(True,False,choices=replace(RenChoices(),research_path='magic'))
        with self.assertRaises(ValueError):simulate_ren(True,1)

    def test_other_pilot_rejected(self):
        with self.assertRaises(ValueError):interpret(RenChoices(),simulate('Mara',(True,True),(False,False,False)))

if __name__=='__main__':unittest.main()
