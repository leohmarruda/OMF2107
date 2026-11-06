import unittest,csv,re,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]; D=R/'27_Performance_Audio_Registry'
class TestPerformanceAudioRegistry(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.registry=json.loads((D/'registry.json').read_text())
  cls.revisions=list(csv.DictReader((D/'script_revisions.csv').open()))
  cls.dialogue=list(csv.DictReader((D/'dialogue_cues.csv').open()))
  cls.music=list(csv.DictReader((D/'scene_music_cues.csv').open()))
 def test_covers_all_campaigns_and_18_scripts(self):
  self.assertEqual(len(self.revisions),18)
  self.assertEqual(len(set(r['campaign'] for r in self.revisions)),13)
 def test_no_content_changed(self):
  for r in self.revisions:
   text=(R/r['new']).read_text();old=(R/r['old']).read_text()
   text=re.sub(r'^<!-- ACTIVE performance-annotated version[^\n]+-->\n','',text)
   text=re.sub(r'^\*\*\[MUSIC: [^\n]*\]\*\*\n','',text,flags=re.M)
   text=re.sub(r'^\*\*\[PERF: [^\n]*\]\*\*\n','',text,flags=re.M)
   text=re.sub(r' \[PERF: [^\]\n]*\]','',text)
   self.assertEqual(text,old,r['new'])
 def test_expression_codes_closed_vocabulary(self):
  codes={v['expression_code'] for v in self.registry['expressions'].values()}
  for r in self.dialogue:
   if r['tone']!='neutral':
    self.assertEqual(self.registry['expressions'][r['tone']]['expression_code'],r['expression'])
    self.assertIn(r['expression'],codes)
 def test_music_codes_known_and_backgrounds_preserved(self):
  self.assertEqual(len(self.music),449)
  for r in self.music:
   self.assertIn(r['music'],self.registry['music_stems'])
   self.assertTrue(r['bg'].startswith('BG-'))
 def test_no_script_has_unknown_music_or_expression(self):
  for r in self.revisions:
   txt=(R/r['new']).read_text()
   self.assertEqual(txt.count('[MUSIC:'),int(r['music_cues']))
   self.assertEqual(txt.count('[PERF:'),int(r['expressive_cues']))
 def test_sprite_family_lookup_complete(self):
  lookup=self.registry['expression_to_sprite_family']; fam=self.registry['sprite_families']
  for r in self.dialogue:
   if r['tone']!='neutral':
    self.assertIn(r['expression'],lookup)
    self.assertIn(lookup[r['expression']],fam)
 def test_dialogue_ids_globally_unique(self):
  ids=[r['utterance_id'] for r in self.dialogue]
  self.assertEqual(len(ids),len(set(ids)))
 def test_current_release_refs_exist(self):
  release=(R/'00_README/CURRENT_RELEASE.md').read_text()
  for r in self.revisions:
   self.assertIn(Path(r['new']).name,release)
if __name__=='__main__':unittest.main()
