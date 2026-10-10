import json, unittest
from pathlib import Path
from council import run_council
from core import build_list
from release import SPEC_VERSION
ROOT=Path(__file__).resolve().parents[1]
class ReleaseChecks(unittest.TestCase):
 def exercise(self, repair_good):
  p=json.loads((ROOT/'data/sample.json').read_text());d=json.loads((ROOT/'data/dataset.json').read_text());r=build_list(p,d);claims=[]
  for c in r['colleges']:
   x=c['cases'][0];claims.append(dict(college_id=c['college_id'],category=c['category'],application_id=x['application_id'],outcome=x['outcome'],quote=x['essay'][:100],student_quote=p['essay'][:100],explanation='These quotations describe practical problem solving.',limitation='Synthetic decisions do not establish an admission cause.'))
  good=json.dumps({'colleges':claims,'summary':'Compare observed experiences; decisions are illustrative.'});calls=[]
  def call(messages,model,purpose):
   calls.append(purpose)
   content=json.dumps({'ranking':['A','B'],'reasons':['Exact source comparison'],'concerns':[]}) if purpose=='council_review' else good
   if purpose=='council_chairman' or purpose=='council_repair' and not repair_good: content=good+'\nUnexpected extra text'
   return {'content':content,'model':model,'trace_id':purpose}
  return run_council(p,r,call),calls
 def test_malformed_chairman_has_one_repair(self):
  result,calls=self.exercise(True)
  self.assertEqual(result['status'],'passed');self.assertEqual(calls.count('council_repair'),1)
 def test_malformed_repair_never_passes(self):
  result,calls=self.exercise(False)
  self.assertEqual(result['status'],'incomplete');self.assertIsNone(result['synthesis']);self.assertEqual(calls.count('council_repair'),1)
 def test_spec_identity_and_independent_fixture_expectations(self):
  self.assertIn('Specification version: '+SPEC_VERSION+'.',(ROOT/'SPEC.md').read_text())
  d=json.loads((ROOT/'data/dataset.json').read_text());p=json.loads((ROOT/'data/sample.json').read_text());expected=json.loads((ROOT/'data/expected_results.json').read_text())
  result=build_list(p,d);self.assertEqual(result['spec_version'],SPEC_VERSION);self.assertEqual([c['category'] for c in result['colleges']],expected['baseline'])
  self.assertEqual([c['category'] for c in build_list({**p,'rigor':2},d)['colleges']],expected['rigor_2'])
if __name__=='__main__':unittest.main()
