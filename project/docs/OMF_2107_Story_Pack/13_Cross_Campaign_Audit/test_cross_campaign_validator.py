import unittest,itertools
from pathlib import Path
from cross_campaign_validator import (simulate_screen,chronology_check,resolve_ending,
    normalized_pairs, RelationshipConflict,DEFAULT_SCREEN_WINS, DEFAULT_KNOCKOUT_WINS)

class CrossCampaignAudit(unittest.TestCase):
    def test_default_outcomes_reproduce_same_world(self):
        for p,wins in DEFAULT_SCREEN_WINS.items():
            with self.subTest(pilot=p):
                t,r=simulate_screen(p,*wins,DEFAULT_KNOCKOUT_WINS[p])
                self.assertEqual(t['champion'],'Ari')
                self.assertFalse(t['circular_groups'])
                chronology_check(p,r)
                self.assertEqual(len(t['matches']),19)

    def test_all_160_binary_screen_input_combinations(self):
        count=0
        for p in DEFAULT_SCREEN_WINS:
            for group in itertools.product((False,True),repeat=2):
                for ko in itertools.product((False,True),repeat=3):
                    t,r=simulate_screen(p,*group,ko)
                    self.assertEqual(t['selected_pilot_advances_from_group'],
                                     t['player_elimination_match']!='GROUP_STAGE')
                    self.assertEqual(t['champion'],t['matches'][-1]['winner'])
                    self.assertTrue(all(m['winner']!=m['loser'] for m in t['matches']))
                    chronology_check(p,r)
                    if r is not None:
                        clues=r.get('core_clues',r.get('all_essential_clues',()))
                        self.assertTrue(len(clues)>=7)
                        scenes=r.get('core_scenes',r.get('main_scenes',()))
                        self.assertTrue(any('nova' in x.lower() and ('boss' in x.lower() or 'special' in x.lower()) for x in scenes))
                        self.assertTrue(any(x.startswith(('L6.3','M6.2','R6.2','A6.2')) for x in scenes))
                    count+=1
        self.assertEqual(count,160)

    def test_lyra_screen_input_is_milano_then_steffan(self):
        t,r=simulate_screen('Lyra',True,False,(False,))
        matches={m['id']:m for m in t['matches']}
        self.assertEqual(matches['GC3']['winner'],'Lyra') # vs Milano
        self.assertEqual(matches['GC1']['winner'],'Steffan') # vs Steffan
        self.assertEqual(r['lyra_group_rank'],2)

    def test_ari_screen_input_is_selene_then_crystal(self):
        t,_=simulate_screen('Ari',True,False,(False,))
        matches={m['id']:m for m in t['matches']}
        self.assertEqual(matches['GA3']['winner'],'Ari') # vs Selene
        self.assertEqual(matches['GA1']['winner'],'Crystal')

    def test_cross_pilot_relationship_conflicts(self):
        r={'romance_endings_available':('ren','crystal','leena','single','friendship')}
        # Ren/Tessa and Crystal/Raven must be addressed in independent scenes.
        for intended,existing in [('ren',[('Ren','Tessa')]),
                                  ('crystal',[('Crystal','Raven')]),
                                  ('leena',[('Ari','Leena')])]:
            with self.subTest(pair=intended), self.assertRaises(RelationshipConflict):
                resolve_ending('Angel',r,intended,existing)
        # A character cannot gain two simultaneous exclusive partners.
        with self.assertRaises(RelationshipConflict):
            normalized_pairs([('Ari','Mara'),('Ari','Leena')])

    def test_verified_separation_is_explicit_and_not_a_toggle(self):
        r={'romance_endings_available':('ren','single','friendship')}
        before=[('Ren','Tessa')]
        changed=resolve_ending('Angel',r,'ren',before,verified_separations=[('Ren','Tessa')])
        self.assertIn(frozenset(('Angel','Ren')),changed)
        self.assertNotIn(frozenset(('Ren','Tessa')),changed)
        with self.assertRaises(RelationshipConflict):
            resolve_ending('Angel',r,'ren',before,verified_separations=[('Crystal','Raven')])

    def test_romance_not_automatically_unlocked_by_desire(self):
        r={'romance_endings_available':('friendship','single')}
        with self.assertRaises(RelationshipConflict):
            resolve_ending('Angel',r,'ren')
        self.assertEqual(resolve_ending('Angel',r,'friendship',[('Ren','Tessa')]),
                         normalized_pairs([('Ren','Tessa')]))

    def test_corrected_angel_chapter_days(self):
        root=Path(__file__).resolve().parents[1]
        text=(root/'12_Angel_Campaign/Angel_Playable_Screenplay_v0.1.md').read_text(encoding='utf-8')
        for header in ('Days 3–4. Question','Day 5. Question','Days 8–10. Question',
                       'Days 11–12. Question','Day 13. Question'):
            self.assertIn(header,text)
        self.assertNotIn('*Day 6. Question:',text)

if __name__=='__main__': unittest.main()
