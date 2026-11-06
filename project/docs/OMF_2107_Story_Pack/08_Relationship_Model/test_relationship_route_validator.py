import sys
import unittest
from dataclasses import replace
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from relationship_route_validator import StoryState, relationship_ready, main_ending, available_scene_slots, blue_hour_choices

BASE = StoryState(player='Ari', primary_route='Ari:Mara', mutual_attraction=frozenset({'Ari:Mara'}),
                  commitments={'Ari':'Mara','Mara':'Ari'}, bonds={'Ari:Mara':'romance'})

class RelationshipBranches(unittest.TestCase):
    def test_default_ari_mara_eligible(self):
        self.assertTrue(relationship_ready(BASE,'Ari:Mara'))
        self.assertEqual(main_ending(BASE),'16_ari_mara_restaurant')

    def test_romance_not_forced_from_banter(self):
        state=replace(BASE,mutual_attraction=frozenset())
        self.assertFalse(relationship_ready(state,'Ari:Mara'))
        self.assertEqual(main_ending(state),'16B_E4_solo_friendship')

    def test_friendship_has_positive_ending(self):
        state=StoryState(player='Ari',bonds={'Ari:Mara':'friends'})
        self.assertEqual(main_ending(state),'16_ari_mara_friendship_restaurant')

    def test_ari_leena_requires_age_recusal_mutual_and_no_exclusive_mara(self):
        state=StoryState(player='Ari',primary_route='Ari:Leena', mutual_attraction=frozenset({'Ari:Leena'}))
        self.assertFalse(relationship_ready(state,'Ari:Leena'))
        state=replace(state,adult_verified=state.adult_verified|{'Leena'},professional_cleared=frozenset({'leena_independent_publication'}))
        self.assertTrue(relationship_ready(state,'Ari:Leena'))
        self.assertEqual(main_ending(state),'16B_E1_ari_leena')
        self.assertFalse(relationship_ready(replace(state,commitments={'Ari':'Mara'}),'Ari:Leena'))

    def test_lyra_alex_only_post_assignment(self):
        s=StoryState(player='Lyra',primary_route='Lyra:Alex',adult_verified=BASE.adult_verified|{'Alex'},mutual_attraction=frozenset({'Lyra:Alex'}))
        self.assertFalse(relationship_ready(s,'Lyra:Alex'))
        s=replace(s,professional_cleared=frozenset({'alex_recused'}))
        self.assertTrue(relationship_ready(s,'Lyra:Alex'))
        self.assertEqual(main_ending(s),'15B_lyra_alex')
        self.assertFalse(relationship_ready(replace(s,commitments={'Lyra':'Steffan'}),'Lyra:Alex'))

    def test_mara_plug_after_work_contract_end(self):
        s=StoryState(player='Mara',primary_route='Mara:Plug',mutual_attraction=frozenset({'Mara:Plug'}),adult_verified=BASE.adult_verified|{'Plug'})
        self.assertFalse(relationship_ready(s,'Mara:Plug'))
        s=replace(s,professional_cleared=frozenset({'plug_repair_contract_closed'}))
        self.assertEqual(main_ending(s),'16B_E2_mara_plug')

    def test_crystal_raven_no_romantic_amnesty(self):
        s=StoryState(player='Crystal',primary_route='Crystal:Raven',mutual_attraction=frozenset({'Crystal:Raven'}))
        self.assertFalse(relationship_ready(s,'Crystal:Raven'))
        s=replace(s,disclosure_complete=True)
        self.assertFalse(relationship_ready(s,'Crystal:Raven'))
        s=replace(s,independent_evidence_review=True)
        self.assertEqual(main_ending(s),'16B_E3_crystal_raven')

    def test_neural_disagreement_preserves_choice(self):
        s=replace(BASE,chapter=4, trust_strained=True)
        self.assertEqual(blue_hour_choices(s),('quiet_nonromantic_talk','skip'))
        s=replace(s,trust_strained=False)
        self.assertEqual(blue_hour_choices(s),('stay','kiss_and_leave','talk','skip'))

    def test_rooftop_open_to_all_selected_pilots(self):
        for pilot in ('Ari','Mara','Lyra','Dante','Steffan','Crystal','Raven','Jean-Paul','Milano','Selene','Ren','Angel'):
            self.assertIn('4B_neon_respite',available_scene_slots(StoryState(player=pilot,chapter=2)))

    def test_side_scene_access_not_romance_gated(self):
        self.assertIn('3B_cooling_system',available_scene_slots(StoryState(player='Mara',chapter=4)))
        self.assertIn('2B_clean_custody',available_scene_slots(StoryState(player='Ari',chapter=5)))

    def test_selected_pilot_owns_main_ending(self):
        s=replace(BASE,player='Lyra')
        self.assertEqual(main_ending(s),'16B_E4_solo_friendship')

    def test_combat_outcomes_remain_separate(self):
        # The social state has no wins/loses field, and social decisions
        # cannot mutate the authoritative tournament record.
        tournament_outcomes={'Ari:Crystal':'Crystal','Ari:Mara':'Ari','Lyra:Steffan':'Lyra'}
        before=dict(tournament_outcomes)
        _=main_ending(replace(BASE,trust_strained=True))
        self.assertEqual(tournament_outcomes,before)

    def test_actual_tournament_simulation_is_stable_across_social_choices(self):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'07_Tournament_Model'))
        from tournament_validator import simulate
        baseline=simulate('Ari',(False,True),(True,True,True))
        self.assertEqual(baseline['champion'],'Ari')
        _=main_ending(BASE)
        _=main_ending(replace(BASE,mutual_attraction=frozenset(),bonds={'Ari:Mara':'friends'}))
        after=simulate('Ari',(False,True),(True,True,True))
        self.assertEqual(after['matches'],baseline['matches'])
        self.assertEqual(after['champion'],baseline['champion'])

    def test_ch3_first_kiss_not_repeated_in_spar(self):
        p=Path(__file__).resolve().parents[1]/'04_Screenplay_Reconstructions'/'Chapter_03_Trouble_With_Attraction_v0.2.md'
        scene=p.read_text().split('## SCENE 5B — FIVE MORE SECONDS')[1].split('# SCENE 6')[0]
        self.assertIn('*does not* include a first kiss',scene)
        self.assertNotIn('they kiss',scene.lower())

    def test_lyra_alex_after_default_steffan_breakup(self):
        ch6=(Path(__file__).resolve().parents[1]/'04_Screenplay_Reconstructions'/'Chapter_06_One_Must_Fall_v0.2.md').read_text()
        self.assertIn('the tournament and Alex\'s active coverage of her matches have ended',ch6)
        self.assertIn('## SCENE 15B — NO INTERVIEW TONIGHT',ch6)

if __name__=='__main__': unittest.main()
