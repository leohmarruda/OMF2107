#!/usr/bin/env python3
import itertools
import unittest
from dataclasses import replace
from crystal_route_validator import CrystalChoices, simulate_crystal_screen, CORE_CLUES

class CrystalTests(unittest.TestCase):
    def test_v14_no_romance_if_raven_exploited_crystal(self):
        valid = CrystalChoices(relationship_intent='raven', chooses_private_ds=True,
            raven_reciprocates=True, raven_free=True, crystal_free=True,
            raven_disclosure_verified=True, limits_agreed=True,
            crystal_active_consent=True, raven_active_consent=True,
            raven_coercion_recorded=True)
        r = simulate_crystal_screen(True, True, (True, False), valid)
        self.assertTrue(r['involuntary_pull_to_raven'])
        self.assertTrue(r['raven_coercion_recorded'])
        self.assertFalse(r['consensual_private_ds'])
        self.assertIn('C5.3_INFORMED_NO_INTIMACY', r['scene_ids'])

    def test_v14_recorded_exploitation_never_gates_evidence(self):
        c=CrystalChoices(raven_coercion_recorded=True,relationship_intent='single')
        r=simulate_crystal_screen(False,False,choices=c)
        self.assertTrue(r['independent_shuttle_inquiry'])
        self.assertIn('nova_conditional_executive_veto', r['core_clues'])

    def test_default(self):
        r = simulate_crystal_screen(True, True, (True, False, False))
        self.assertEqual(r['group_rank'], 1)
        self.assertEqual(r['qf_id'], 'Q1')
        self.assertEqual(r['qf_opponent'], 'Ren')
        self.assertEqual(r['sf_opponent'], 'Ari')
        self.assertFalse(r['final_reached'])
        self.assertEqual(r['champion'], 'Ari')

    def test_32_binary_input_cases(self):
        for bits in itertools.product((False, True), repeat=5):
            r = simulate_crystal_screen(bits[0], bits[1], bits[2:])
            t = r['tournament']
            self.assertEqual(r['qualified'], r['group_rank'] <= 2)
            self.assertEqual(r['crystal_champion'], t['champion'] == 'Crystal')
            self.assertEqual(r['official_trophy'], r['crystal_champion'])
            self.assertEqual(len(t['matches']), 19)
            self.assertEqual(r['nova_encounter'], 'SPECIAL_NOVA_AFTER_ACTUAL_FINAL')
            self.assertTrue(all(m['winner'] != m['loser'] for m in t['matches']))

    def test_group_screen_adapter(self):
        # Only loss to Selene, victory over Ari: 1-1-1, provisional Crystal seed first.
        r = simulate_crystal_screen(False, True, (False, False, False))
        self.assertEqual(r['group_rank'], 1)
        self.assertIn('A', r['tournament']['circular_groups'])
        m = {m['id']:m['winner'] for m in r['tournament']['matches']}
        self.assertEqual((m['GA1'], m['GA2']), ('Crystal', 'Selene'))
        self.assertEqual(r['group_match_order'], ('GA2', 'GA1'))

    def test_early_elimination_no_fake_qf(self):
        r = simulate_crystal_screen(False, False, (False, False, False))
        self.assertEqual(r['group_rank'], 3)
        self.assertIsNone(r['qf_id'])
        self.assertFalse(r['sf_reached'])
        self.assertFalse(r['final_reached'])
        self.assertIn('C4.1_NO_QF', r['scene_ids'])
        self.assertIn('C6.1_SPECTATE', r['scene_ids'])

    def test_can_be_champion(self):
        r = simulate_crystal_screen(True, True, (True, True, True))
        self.assertTrue(r['crystal_champion'])
        self.assertTrue(r['final_reached'])
        self.assertEqual(r['final_opponent'], 'Lyra')
        self.assertIn('C6.1_FINAL', r['scene_ids'])

    def test_instinct_not_consent(self):
        r = simulate_crystal_screen(True, True, (True, False), CrystalChoices(relationship_intent='raven'))
        self.assertTrue(r['involuntary_pull_to_raven'])
        self.assertEqual(r['relationship_ending'], 'raven_unresolved')
        self.assertFalse(r['consensual_private_ds'])
        self.assertIn('C5.3_INFORMED_NO_INTIMACY', r['scene_ids'])

    def test_full_raven_gates(self):
        valid = CrystalChoices(relationship_intent='raven', chooses_private_ds=True,
            raven_reciprocates=True, raven_free=True, crystal_free=True,
            raven_disclosure_verified=True, limits_agreed=True,
            crystal_active_consent=True, raven_active_consent=True)
        r = simulate_crystal_screen(True, True, (True, False), valid)
        self.assertEqual(r['relationship_ending'], 'raven_consensual_ds')
        self.assertTrue(r['consensual_private_ds'])
        for field in ('chooses_private_ds', 'raven_reciprocates', 'raven_free', 'crystal_free',
                      'raven_disclosure_verified', 'limits_agreed', 'crystal_active_consent', 'raven_active_consent'):
            r = simulate_crystal_screen(True, True, (True, False), replace(valid, **{field: False}))
            self.assertEqual(r['relationship_ending'], 'raven_unresolved', field)
            self.assertFalse(r['consensual_private_ds'])

    def test_angel_requires_separation_and_mutuality(self):
        valid = CrystalChoices(relationship_intent='angel', angel_adult_verified=True,
            angel_reciprocates=True, angel_free=True, crystal_free=True,
            raven_relationship_cleared=True)
        self.assertEqual(simulate_crystal_screen(True, True, (True, False), valid)['relationship_ending'], 'angel_romance')
        for field in ('angel_adult_verified', 'angel_reciprocates', 'angel_free', 'crystal_free', 'raven_relationship_cleared'):
            r = simulate_crystal_screen(True, True, (True, False), replace(valid, **{field: False}))
            self.assertEqual(r['relationship_ending'], 'angel_friendship_only', field)

    def test_clues_and_independent_inquiry_across_tournament_and_romance(self):
        variants = [CrystalChoices(), CrystalChoices(relationship_intent='friendship'),
                    CrystalChoices(relationship_intent='raven'), CrystalChoices(relationship_intent='angel')]
        for bits in itertools.product((False, True), repeat=5):
            for opts in variants:
                r = simulate_crystal_screen(bits[0], bits[1], bits[2:], opts)
                self.assertEqual(r['core_clues'], CORE_CLUES)
                self.assertTrue(r['independent_shuttle_inquiry'])
                self.assertTrue(r['involuntary_pull_to_raven'])

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            simulate_crystal_screen(True, True, (), CrystalChoices(relationship_intent='both'))
        with self.assertRaises(ValueError):
            simulate_crystal_screen(1, False, (False, False))
        with self.assertRaises(ValueError):
            simulate_crystal_screen(True, True, (), CrystalChoices(reform_policy='automatic_absolution'))

    def test_public_ending_independent_of_romance(self):
        for strategy in ('conditional_council', 'outside_watchdog', 'public_witness'):
            r = simulate_crystal_screen(True, True, (True, False), CrystalChoices(reform_policy=strategy))
            self.assertEqual(r['reform_policy'], strategy)
            self.assertFalse(r['romance_committed'])

    def test_semifinal_day_before_rescue(self):
        r = simulate_crystal_screen(True, True, (True, True, False))
        self.assertEqual(r['timeline']['S_AB'], 11)
        self.assertEqual(r['timeline']['RESCUE'], 12)
        self.assertEqual(r['timeline']['FINAL'], 13)
        self.assertTrue(r['final_reached'])
        self.assertFalse(r['official_trophy'])

if __name__ == '__main__':
    unittest.main()
