import itertools
import unittest
from dataclasses import replace
from angel_route_validator import (
    CORE_CLUES, AngelChoices, choose_ending, interpret, simulate_angel
)
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate


class AngelRouteTests(unittest.TestCase):
    def eligible(self, partner):
        return AngelChoices(
            relationship_intent=partner, angel_adult_verified=True,
            partner_adult_verified=True, partner_reciprocates=True,
            partner_free=True, ren_capacity_clear=True,
            ren_private_interface_isolated=True, ren_tessa_commitment_cleared=True,
            crystal_raven_commitment_cleared=True,
            leena_recused=True, leena_ari_commitment_cleared=True,
        )

    def test_default_path(self):
        r = simulate_angel(True, True)
        self.assertEqual(r['angel_group_rank'], 1)
        self.assertEqual(r['qf_id'], 'Q4')
        self.assertEqual(r['qf_opponent'], 'Lyra')
        self.assertEqual(r['official_champion'], 'Ari')
        self.assertEqual(r['player_elimination_match'], 'Q4')

    def test_match_order_translation(self):
        r = simulate_angel(False, True)
        ref = simulate('Angel', (True, False), (False, False, False))
        self.assertEqual(r['official_champion'], ref['champion'])
        self.assertEqual(r['angel_group_rank'], ref['group_standings']['D']['ranked'].index('Angel') + 1)
        self.assertEqual(r['group_match_order_on_screen'], ('GD2', 'GD1'))

    def test_two_losses_no_knockout(self):
        r = simulate_angel(False, False)
        self.assertEqual(r['angel_group_rank'], 3)
        self.assertIsNone(r['qf_id'])
        self.assertIn('A4.1b_qualified_fighters_broadcast', r['main_scenes'])
        self.assertIn('A6.3_separate_nova_boss', r['main_scenes'])

    def test_both_wins_q4(self):
        self.assertEqual(simulate_angel(True, True)['qf_id'], 'Q4')

    def test_qualifies_second_q3(self):
        r = simulate_angel(True, False)
        self.assertEqual(r['angel_group_rank'], 2)
        self.assertEqual(r['qf_id'], 'Q3')
        self.assertEqual(r['qf_opponent'], 'Steffan')

    def test_32_patterns(self):
        for bits in itertools.product((False, True), repeat=5):
            r = simulate_angel(bits[0], bits[1], bits[2:])
            self.assertIn(r['angel_group_rank'], (1,2,3))
            self.assertEqual(len(r['all_essential_clues']), 8)
            self.assertEqual(r['played_final'], r['final_opponent'] is not None)
            self.assertIn('A6.3_separate_nova_boss', r['main_scenes'])
            self.assertFalse(r['nova_is_official_match'])

    def test_championship_requires_real_final_win(self):
        r = simulate_angel(True, True, (True, True, True))
        self.assertTrue(r['angel_champion'])
        self.assertEqual(r['official_champion'], 'Angel')

    def test_loss_in_final_no_championship(self):
        r = simulate_angel(True, True, (True, True, False))
        self.assertFalse(r['angel_champion'])
        self.assertNotEqual(r['official_champion'], 'Angel')

    def test_tournament_invariant_under_all_identity_choices(self):
        records = [simulate_angel(True, True, (True, False, True),
                    replace(AngelChoices(), identity_policy=p)) for p in ('masked','controlled','public')]
        self.assertEqual(len({r['official_champion'] for r in records}),1)
        self.assertEqual(len({r['qf_opponent'] for r in records}),1)

    def test_tournament_invariant_under_archive_and_romance(self):
        base = simulate_angel(True, True, (True, True, True))
        for p in ('escrow','redacted_release','private_verify'):
            for s in ('ren','crystal','leena','single'):
                r = simulate_angel(True, True, (True,True,True),
                                    replace(AngelChoices(), archive_disposition=p, relationship_intent=s))
                self.assertEqual(base['official_champion'], r['official_champion'])
                self.assertEqual(base['qf_id'], r['qf_id'])

    def test_no_romance_without_explicit_adult_check(self):
        for p in ('ren','crystal','leena'):
            c = replace(self.eligible(p), angel_adult_verified=False)
            self.assertNotIn(p, simulate_angel(True, False, choices=c)['romance_endings_available'])
            c = replace(self.eligible(p), partner_adult_verified=False)
            self.assertNotIn(p, simulate_angel(True, False, choices=c)['romance_endings_available'])

    def test_mutuality_required(self):
        for p in ('ren','crystal','leena'):
            c = replace(self.eligible(p), partner_reciprocates=False)
            self.assertNotIn(p, simulate_angel(True, False, choices=c)['romance_endings_available'])
            c = replace(self.eligible(p), partner_free=False)
            self.assertNotIn(p, simulate_angel(True, False, choices=c)['romance_endings_available'])

    def test_ren_capacity_and_disconnection(self):
        for key in ('ren_capacity_clear','ren_private_interface_isolated','ren_tessa_commitment_cleared'):
            c = replace(self.eligible('ren'), **{key:False})
            self.assertNotIn('ren', simulate_angel(True, True, choices=c)['romance_endings_available'])
        self.assertIn('ren', simulate_angel(True, True, choices=self.eligible('ren'))['romance_endings_available'])

    def test_crystal_requires_raven_resolution(self):
        c = replace(self.eligible('crystal'), crystal_raven_commitment_cleared=False)
        self.assertNotIn('crystal', simulate_angel(True,True,choices=c)['romance_endings_available'])
        self.assertIn('crystal', simulate_angel(True,True,choices=self.eligible('crystal'))['romance_endings_available'])

    def test_leena_requires_recusal_and_ari_resolution(self):
        for key in ('leena_recused', 'leena_ari_commitment_cleared'):
            c = replace(self.eligible('leena'), **{key:False})
            self.assertNotIn('leena', simulate_angel(True,False,choices=c)['romance_endings_available'])
        self.assertIn('leena', simulate_angel(True,False,choices=self.eligible('leena'))['romance_endings_available'])

    def test_romances_exclusive(self):
        c = self.eligible('ren')
        r = simulate_angel(True,True, choices=c)
        self.assertIn('ren', r['romance_endings_available'])
        self.assertNotIn('crystal', r['romance_endings_available'])
        self.assertNotIn('leena', r['romance_endings_available'])

    def test_friendship_and_single_always_available(self):
        for p in ('ren','crystal','leena','friendship','single'):
            r = simulate_angel(False,False,choices=AngelChoices(relationship_intent=p))
            self.assertTrue({'single','friendship'} <= set(r['romance_endings_available']))

    def test_clues_persist_across_routes(self):
        for witness, archive, release in itertools.product(
                ('forensic','human','physical'), ('escrow','redacted_release','private_verify'),
                ('audited_public','protected_hearing','limited_proof')):
            r = simulate_angel(False,False, choices=AngelChoices(
                witness_method=witness, archive_disposition=archive, release_policy=release))
            self.assertEqual(set(r['all_essential_clues']), set(CORE_CLUES))
            self.assertFalse(r['dangerous_full_nova_blueprint_published'])

    def test_evidence_contributions_distinct(self):
        roles={simulate_angel(True,False,choices=AngelChoices(witness_method=p))['evidence_contribution'] for p in ('forensic','human','physical')}
        self.assertEqual(len(roles),3)

    def test_anonymity_can_maintain_independent_proof(self):
        r = simulate_angel(False,False,choices=AngelChoices(identity_policy='masked',release_policy='protected_hearing'))
        self.assertEqual(len(r['all_essential_clues']),8)
        self.assertFalse(r['privacy_is_always_forfeited'])

    def test_invalid_romance_ending_rejected(self):
        r = simulate_angel(True,False)
        with self.assertRaises(ValueError): choose_ending(r,'ren')
        self.assertEqual(choose_ending(r,'single'),'single')

    def test_invalid_choice_rejected(self):
        for key, value in (('identity_policy','automatic'),('archive_disposition','delete'),
                           ('witness_method','magic'),('release_policy','none'),('relationship_intent','all')):
            with self.assertRaises(ValueError):
                simulate_angel(True,False,choices=replace(AngelChoices(),**{key:value}))

    def test_invalid_group_bools_rejected(self):
        with self.assertRaises(ValueError): simulate_angel(1,True)
        with self.assertRaises(ValueError): simulate_angel(False,'yes')

    def test_other_pilot_rejected(self):
        with self.assertRaises(ValueError):interpret(AngelChoices(),simulate('Ren',(True,False),(False,False,False)))

if __name__ == '__main__':
    unittest.main()
