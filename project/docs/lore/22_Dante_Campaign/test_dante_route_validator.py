import unittest
import itertools
from dataclasses import replace
from dante_route_validator import DanteChoices, simulate_dante, interpret
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '07_Tournament_Model'))
from tournament_validator import simulate

class DanteRouteTests(unittest.TestCase):
    def test_default_canonical_group_and_qf(self):
        r=simulate_dante(True,False,(False,))
        self.assertEqual(r['group_rank'],2)
        self.assertEqual(r['quarterfinal_id'],'Q3')
        self.assertEqual(r['quarterfinal_opponent'],'Steffan')
        self.assertEqual(r['eliminated_at'],'Q3')
        self.assertEqual(r['official_champion'],'Ari')
        self.assertFalse(r['final_played'])

    def test_all_32_outcomes(self):
        for b in itertools.product((False,True), repeat=5):
            r=simulate_dante(b[0],b[1],b[2:])
            self.assertEqual(r['qualified'],r['quarterfinal_id'] is not None)
            self.assertEqual(r['semifinal_played'],r['semifinal_opponent'] is not None)
            self.assertEqual(r['final_played'],r['final_opponent'] is not None)
            self.assertTrue(all(m['winner']!=m['loser'] for m in r['tournament']['matches']))
            self.assertIn('DV5.2_CONFRONT_STEFFAN_DAY11',r['scenes'])
            self.assertIn('DV5.3_NOVA_RESCUE_DAY12',r['scenes'])
            self.assertIn('DV6.2_NOVA_VETO_AND_DESTRUCTION_DAY13',r['scenes'])
            self.assertFalse(r['day13_e5_known'])
            self.assertTrue(r['day30_e5_authenticated'])
            self.assertFalse(r['nova_default_survives'])

    def test_group_win_both_top_rank(self):
        r=simulate_dante(True,True,(False,))
        self.assertEqual((r['group_rank'],r['quarterfinal_id']), (1,'Q4'))

    def test_losses_eliminated(self):
        r=simulate_dante(False,False)
        self.assertFalse(r['qualified'])
        self.assertEqual(r['eliminated_at'],'GROUP_STAGE')
        self.assertIn('DV4.2_ELIMINATION',r['scenes'])

    def test_circular_win_angel_loss_jeanpaul(self):
        r=simulate_dante(False,True,(False,))
        self.assertTrue(r['group_circular'])
        self.assertEqual(r['group_rank'],2)
        self.assertEqual(r['quarterfinal_id'],'Q3')

    def test_player_can_be_champion(self):
        r=simulate_dante(True,True,(True,True,True))
        self.assertTrue(r['dante_champion'])
        self.assertEqual(r['official_champion'],'Dante')

    def test_standings_adapter(self):
        r=simulate_dante(True,False,(False,))
        s=simulate('Dante',(False,True),(False,))
        self.assertEqual(r['tournament']['matches'],s['matches'])

    def test_tone_variants_preserve_tournament(self):
        base=simulate_dante(True,False,(True,False))['tournament']['matches']
        for conf in ('merciless','clear','vulnerable'):
            for rev in ('needle','withdraw','threaten_public_scene'):
                ch=DanteChoices(confrontation=conf,revenge_response=rev)
                r=simulate_dante(True,False,(True,False),ch)
                self.assertEqual(base,r['tournament']['matches'])
                self.assertTrue(r['confrontation_inevitable'])

    def test_lyra_reunion_not_an_instant_reward(self):
        base=DanteChoices(relationship_intent='lyra',lyra_available=True,
            lyra_independently_reciprocates=True,lyra_independent_repair=True,
            future_interval_elapsed=True)
        self.assertEqual(simulate_dante(True,False,(False,),base)['relationship_ending'],'lyra_future_proposal')
        for field in ('lyra_available','lyra_independently_reciprocates','lyra_independent_repair','future_interval_elapsed'):
            self.assertFalse(simulate_dante(True,False,(False,),replace(base,**{field:False}))['romance_achieved'])
        self.assertFalse(simulate_dante(True,False,(False,),replace(base,lyra_response='lash_out'))['romance_achieved'])
        self.assertFalse(simulate_dante(True,False,(False,),replace(base,revenge_response='threaten_public_scene'))['romance_achieved'])

    def test_steffan_requires_reciprocity_and_accountability(self):
        base=DanteChoices(relationship_intent='steffan',dante_independently_wants_steffan=True,
            respect_response='curiosity',day11_contact='listen',later_approach='explore',
            steffan_available=True,steffan_independently_recognizes_attraction=True,
            steffan_independently_reciprocates=True,steffan_treated_lyra_accountably=True,
            future_interval_elapsed=True)
        self.assertEqual(simulate_dante(True,False,(False,),base)['relationship_ending'],'steffan_future_proposal')
        for field in ('dante_independently_wants_steffan','steffan_available',
                      'steffan_independently_recognizes_attraction','steffan_independently_reciprocates',
                      'steffan_treated_lyra_accountably','future_interval_elapsed'):
            self.assertFalse(simulate_dante(True,False,(False,),replace(base,**{field:False}))['romance_achieved'])
        self.assertFalse(simulate_dante(True,False,(False,),replace(base,steffan_coercive_control_recorded=True))['romance_achieved'])
        self.assertFalse(simulate_dante(True,False,(False,),replace(base,confrontation='merciless'))['romance_achieved'])
        for field, bad in (('respect_response','professional'),('day11_contact','boundary'),('later_approach','none')):
            self.assertFalse(simulate_dante(True,False,(False,),replace(base, **{field:bad}))['romance_achieved'])

    def test_default_dante_is_nonromantic_even_with_steffan_interest(self):
        default=simulate_dante(True,False,(False,))
        self.assertTrue(default['dante_default_nonromantic'])
        self.assertFalse(default['dante_steffan_romance_path_developed'])
        self.assertEqual(default['relationship_ending'],'solo_rebuild')
        self.assertIn('DV2.3_PROFESSIONAL_DEFAULT',default['scenes'])
        self.assertIn('DV5.2_BOUNDARY_DEFAULT',default['scenes'])
        # Even if an external NPC is reciprocal, no unchosen Dante romance.
        ch=DanteChoices(relationship_intent='steffan',dante_independently_wants_steffan=True,
            steffan_available=True,steffan_independently_recognizes_attraction=True,
            steffan_independently_reciprocates=True,steffan_treated_lyra_accountably=True,
            future_interval_elapsed=True)
        self.assertEqual(simulate_dante(True,False,(False,),ch)['relationship_ending'],'relationship_not_available')

    def test_curiosity_and_listening_do_not_force_romance(self):
        ch=DanteChoices(respect_response='curiosity',day11_contact='listen',
            confrontation='vulnerable',later_approach='none')
        r=simulate_dante(True,False,(False,),ch)
        self.assertIn('DV2.3_CURIOSITY',r['scenes'])
        self.assertIn('DV5.2_LISTEN_OPTIONAL',r['scenes'])
        self.assertFalse(r['dante_steffan_romance_path_developed'])
        self.assertEqual(r['relationship_ending'],'solo_rebuild')

    def test_mari_optional_romance(self):
        ch=DanteChoices(relationship_intent='mari',mari_available=True,
            mari_independently_reciprocates=True,professional_conflict_resolved=True,
            future_interval_elapsed=True)
        self.assertEqual(simulate_dante(True,False,(False,),ch)['relationship_ending'],'mari_future_proposal')
        self.assertFalse(simulate_dante(True,False,(False,),replace(ch,professional_conflict_resolved=False))['romance_achieved'])

    def test_vindictive_endpoint(self):
        ch=DanteChoices(confrontation='merciless',revenge_response='threaten_public_scene')
        r=simulate_dante(True,False,(False,),ch)
        self.assertEqual(r['relationship_ending'],'vindictive_isolation')
        self.assertIn('DV5.2b_PUBLIC_FALLOUT_NONDEFAULT',r['scenes'])

    def test_exact_timeline(self):
        t=simulate_dante(False,False)['timeline']
        self.assertEqual(t['DAY11_CONFRONTATION'],t['DAY11_VARGA'])
        self.assertLess(t['DAY11_VARGA'],t['DAY12_RESCUE'])
        self.assertLessEqual(t['DAY12_RESCUE'],t['DAY12_SF'])
        self.assertLess(t['DAY12_SF'],t['DAY13_FINAL'])
        self.assertLess(t['DAY13_FINAL'],t['DAY30_E5'])

    def test_invalid_input(self):
        with self.assertRaises(ValueError): simulate_dante(1,False)
        with self.assertRaises(ValueError): simulate_dante(True,False,choices=replace(DanteChoices(),relationship_intent='both'))
        with self.assertRaises(ValueError): interpret(DanteChoices(),simulate('Steffan',(True,True),(False,)))

if __name__=='__main__': unittest.main()
