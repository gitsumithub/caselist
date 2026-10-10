import json, unittest
from pathlib import Path
from core import build_list
ROOT=Path(__file__).resolve().parents[1]
class ScenarioIntegrityTests(unittest.TestCase):
 def test_distinct_profiles_and_explicit_provenance(self):
  d=json.loads((ROOT/'data/dataset.json').read_text())
  self.assertEqual(len({p['name'].split()[-1] for p in d['applicants']}),60)
  self.assertEqual(len({p['essay'] for p in d['applicants']}),60)
  self.assertEqual(len({p['activities'] for p in d['applicants']}),60)
  self.assertTrue(all(p['synthetic'] and p['courses'] and 'not historical' in p['provenance'] for p in d['applicants']))
  self.assertTrue(all('scenario' in a['provenance'] for a in d['applications']))
 def test_official_facts_separate_from_outcomes(self):
  d=json.loads((ROOT/'data/dataset.json').read_text());p=json.loads((ROOT/'data/sample.json').read_text())
  result=build_list(p,d)
  self.assertTrue(all(not c['fictional'] and c['reference']['url'].startswith('https://') and 'not this college' in c['outcome_scope'] for c in result['colleges']))
  self.assertTrue(all(c['contrast']['admitted']['essay']!=c['contrast']['other']['essay'] for c in result['colleges']))
if __name__=='__main__':unittest.main()
