"""Mara campaign v0.1 route tests, stdlib unittest."""
import dataclasses
from itertools import product
import unittest
from mara_route_validator import MaraChoices, choose_ending, simulate_mara


class MaraRouteTests(unittest.TestCase):
    def test_01_default_bracket(self):
        r = simulate_mara(True,True,(False,))
        self.assertEqual(r['mara_group_rank'],1)
        self.assertEqual(r['qf_id'],'Q2')
        self.assertEqual(r['qf_opponent'],'Ari')
        self.assertEqual(r['elimination'],'Q2')
        self.assertEqual(r['official_champion'],'Ari')
        self.assertFalse(r['mara_champion'])
        self.assertEqual(r['group_match_order_on_screen'],('GB2','GB1'))

    def test_02_b2_opponent_is_actual_a1(self):
        r = simulate_mara(True,False,(True,False))
        self.assertEqual(r['mara_group_rank'],2)
        self.assertEqual(r['qf_id'],'Q1')
        self.assertEqual(r['qf_opponent'],'Crystal')
        self.assertIsNotNone(r['sf_opponent'])

    def test_03_group_elimination_continues(self):
        r = simulate_mara(False,False,())
        self.assertEqual(r['mara_group_rank'],3)
        self.assertIsNone(r['qf_id'])
        self.assertIn('M4.1b_independent_audit',r['main_scenes'])
        self.assertIn('M6.3_special_nova_boss',r['main_scenes'])
        self.assertEqual(r['elimination'],'GROUP_STAGE')

    def test_04_possible_mara_champion(self):
        r = simulate_mara(True,True,(True,True,True))
        self.assertTrue(r['mara_champion'])
        self.assertEqual(r['official_champion'],'Mara')
        self.assertTrue(r['prize_eligible'])
        self.assertEqual(r['prize_received'],'not_assumed_until_settlement')

    def test_05_final_loss_respected(self):
        r = simulate_mara(True,True,(True,True,False))
        self.assertEqual(r['elimination'],'FINAL')
        self.assertFalse(r['mara_champion'])
        self.assertIsNotNone(r['final_opponent'])
        self.assertEqual(r['prize_eligible'],False)

    def test_06_all_32_input_patterns(self):
        # Two group results + up to three knockout outcomes; extra outcomes
        # are ignored on early elimination just as in the original engine.
        for rav,ren,q,s,f in product((False,True),repeat=5):
            with self.subTest(raven=rav,ren=ren,knockout=(q,s,f)):
                r = simulate_mara(rav,ren,(q,s,f))
                self.assertIn('M6.3_special_nova_boss',r['main_scenes'])
                self.assertEqual(len(r['core_clues']),8)
                self.assertIsNotNone(r['official_champion'])
                self.assertEqual(r['prize_eligible'],r['mara_champion'])
                self.assertFalse(r['nova_is_official_match'])

    def test_07_guards_plug_unverified_age(self):
        r=simulate_mara(True,True,(False,),MaraChoices(relationship_intent='plug',plug_mutual_interest=True,plug_professional_conflict_cleared=True))
        self.assertNotIn('plug',r['possible_main_endings'])

    def test_08_guards_plug_professional_boundary(self):
        c=MaraChoices(relationship_intent='plug',plug_mutual_interest=True,plug_adult_verified=True)
        self.assertNotIn('plug',simulate_mara(True,True,(False,),c)['possible_main_endings'])

    def test_09_plug_mutual_and_cleared(self):
        c=MaraChoices(relationship_intent='plug',plug_mutual_interest=True,plug_adult_verified=True,plug_professional_conflict_cleared=True)
        r=simulate_mara(True,True,(False,),c)
        self.assertIn('plug',r['possible_main_endings'])
        self.assertNotIn('ari',r['possible_main_endings'])
        self.assertNotIn('raven',r['possible_main_endings'])
        self.assertEqual(choose_ending(r,'plug'),'M6.5_plug')

    def test_10_raven_requires_crystal_separation_and_accountability(self):
        baseline=MaraChoices(relationship_intent='raven',raven_mutual_interest=True)
        for c in (baseline,dataclasses.replace(baseline,raven_crystal_commitment_cleared=True),dataclasses.replace(baseline,raven_accountability_completed=True)):
            self.assertNotIn('raven',simulate_mara(True,True,(False,),c)['possible_main_endings'])
        c=dataclasses.replace(baseline,raven_crystal_commitment_cleared=True,raven_accountability_completed=True)
        self.assertIn('raven',simulate_mara(True,True,(False,),c)['possible_main_endings'])

    def test_11_ari_neural_concealment_needs_repair(self):
        c=MaraChoices(relationship_intent='ari',ari_mutual_interest=True,ari_concealed_nii=True)
        self.assertNotIn('ari',simulate_mara(True,True,(False,),c)['possible_main_endings'])
        c=dataclasses.replace(c,ari_repair_completed=True)
        self.assertIn('ari',simulate_mara(True,True,(False,),c)['possible_main_endings'])

    def test_12_ari_romance_requires_mutual_interest(self):
        c=MaraChoices(relationship_intent='ari',ari_mutual_interest=False)
        r=simulate_mara(True,True,(False,),c)
        self.assertNotIn('ari',r['possible_main_endings'])
        self.assertIn('friendship',r['possible_main_endings'])

    def test_13_public_sponsorship_requires_mother_consent(self):
        c=MaraChoices(financial_strategy='transparent_sponsor',mother_consented_to_publicity=False)
        self.assertFalse(simulate_mara(True,True,(False,),c)['publicity_permitted'])
        self.assertFalse(simulate_mara(True,True,(False,),c)['sponsor_consent_cleared'])
        self.assertEqual(simulate_mara(True,True,(False,),c)['financial_strategy_effective'],'itemized_plan')
        c=dataclasses.replace(c,mother_consented_to_publicity=True)
        self.assertTrue(simulate_mara(True,True,(False,),c)['sponsor_consent_cleared'])
        self.assertFalse(simulate_mara(True,True,(False,),c)['publicity_permitted'])
        c=dataclasses.replace(c,disclosure='public_with_consent')
        self.assertTrue(simulate_mara(True,True,(False,),c)['publicity_permitted'])

    def test_14_finances_never_magic(self):
        for champion in (True,False):
            for fs in ('itemized_plan','paid_work','transparent_sponsor'):
                c=MaraChoices(financial_strategy=fs)
                ko=(True,True,True) if champion else (False,)
                r=simulate_mara(True,True,ko,c)
                self.assertEqual(r['care_plan'],'independent_contingent_plan_always')
                self.assertEqual(r['prize_received'],'not_assumed_until_settlement')
                self.assertEqual(r['financial_strategy'],fs)

    def test_15_social_choices_cannot_change_matches(self):
        baseline=simulate_mara(True,True,(True,True,False))
        for intent in ('ari','plug','raven','solo'):
            for role in ('mechanical_audit','witness_network','worker_safety'):
                c=MaraChoices(relationship_intent=intent,investigation_role=role,financial_strategy='paid_work')
                r=simulate_mara(True,True,(True,True,False),c)
                for key in ('official_champion','qf_opponent','sf_opponent','final_opponent','elimination','mara_champion'):
                    self.assertEqual(r[key],baseline[key])

    def test_16_no_alternate_relationship_without_intent(self):
        c=MaraChoices(relationship_intent='solo',ari_mutual_interest=True,plug_mutual_interest=True,plug_adult_verified=True,plug_professional_conflict_cleared=True,raven_crystal_commitment_cleared=True,raven_accountability_completed=True,raven_mutual_interest=True)
        r=simulate_mara(True,True,(False,),c)
        self.assertEqual(set(r['possible_main_endings']),{'solo','friendship'})
        with self.assertRaises(ValueError): choose_ending(r,'ari')

if __name__=='__main__':unittest.main()
