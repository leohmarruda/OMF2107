"""Static, deterministic guards for active scripts; not a qualitative narrative review."""
import re, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ACTIVE={
 'Lyra':'09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.4.md',
 'Mara':'10_Mara_Campaign/Mara_Playable_Screenplay_v0.2.md',
 'Ren':'11_Ren_Campaign/Ren_Playable_Screenplay_v0.2.md',
 'Angel':'12_Angel_Campaign/Angel_Playable_Screenplay_v0.2.md',
 'Crystal':'15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.6.md',
 'Raven':'16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.5.md',
 'Jean-Paul':'20_Jean_Paul_Campaign/Jean_Paul_Playable_Screenplay_v0.1.md',
 'Steffan':'21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.3.md',
 'Dante':'22_Dante_Campaign/Dante_Playable_Screenplay_v0.3.md',
 'Selene':'23_Selene_Campaign/Selene_Playable_Screenplay_v0.1.md',
 'Milano':'24_Milano_Campaign/Milano_Playable_Screenplay_v0.1.md',
}

class ActiveScreenplayStructure(unittest.TestCase):
 def test_all_twelve_active_script_sets_are_present(self):
  self.assertEqual(len(ACTIVE)+1,12) # Ari has six chapter files
  for pilot,path in ACTIVE.items(): self.assertTrue((ROOT/path).is_file(),pilot)
  chapters=['01_Anniversary','02_Champions_Shadow','03_Trouble_With_Attraction','04_No_Holding_Back','05_Fractures','06_One_Must_Fall']
  for x in chapters:
   vers='v0.4' if x.startswith('06_') else 'v0.3'
   self.assertTrue((ROOT/f'04_Screenplay_Reconstructions/Chapter_{x}_{vers}.md').is_file(),x)

 def test_no_duplicate_heading_scene_ids_in_active_scripts(self):
  # Only leading, structured scene labels count; incidental refs inside headings do not.
  pat=re.compile(r'^#{2,4}\s+((?:L|M|R|A|C|RV|JP-C|ST|DV|SV|MA)\d+(?:\.\d+[A-Za-z]?|-[A-Za-z0-9]+)+)\s+[—:-]')
  for pilot,path in ACTIVE.items():
   ids=[]
   for line in (ROOT/path).read_text().splitlines():
    m=pat.match(line)
    if m: ids.append(m.group(1))
   self.assertEqual(len(ids),len(set(ids)),f'{pilot}: duplicate scene IDs {ids}')

 def test_dante_day2_training_before_day5_and_dante_default_nonromantic(self):
  d=(ROOT/ACTIVE['Dante']).read_text()
  self.assertEqual(d.count('### DV2.3 — A precise opponent'),1)
  self.assertEqual(d.count('### DV2.2b — The audience'),1)
  self.assertLess(d.index('### DV2.3 — A precise opponent'),d.index('# CHAPTER 3'))
  self.assertIn('default is still nonromantic',d)
  self.assertIn('CHOICE DV2-C3',d)

 def test_shared_world_timing_and_content_sources_exist(self):
  self.assertIn('Day 30',(ROOT/'02_Story_Bibles/Devroe_Shuttle_Case_Canon_v1.7.md').read_text())
  self.assertIn('Day 12',(ROOT/'19_Kreissack_Arc/POV_Integration_Spec_v1.9.md').read_text())
  self.assertIn('DEFAULT_GROUP_WINNERS',(ROOT/'07_Tournament_Model/tournament_validator.py').read_text())
  self.assertIn('NPC_KNOCKOUT_PRIORITY',(ROOT/'07_Tournament_Model/tournament_validator.py').read_text())

if __name__=='__main__': unittest.main()
