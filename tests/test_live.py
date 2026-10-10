import copy,json,unittest
from pathlib import Path
from unittest.mock import patch
from core import build_list
from council import validate_explanations
from live import Journey, validate_extraction, validate_kb_chunk, SponsorError
ROOT=Path(__file__).resolve().parents[1]
class LiveSafetyTests(unittest.TestCase):
 def setUp(self):
  self.p=json.loads((ROOT/'data/sample.json').read_text());self.r=build_list(self.p,json.loads((ROOT/'data/dataset.json').read_text()))
 def test_invented_extraction_rejected(self):
  v={'experiences':[{'label':'award','source':'essay','quote':'Won an award'}],'activity_tags':[]}
  self.assertTrue(validate_extraction(v,self.p))
 def test_wrong_kb_document_rejected(self):
  case=self.r['colleges'][0]['cases'][0]
  self.assertIsNone(validate_kb_chunk({'doc_id':'wrong','content':'plausible'},case,'C01','right'))
 def test_guardrail_fails_closed(self):
  j=Journey({'id':'test','cancelled':False,'session_id':'test','revision':1})
  with patch('live.request',return_value={'evaluated':False,'blocked':False}):
   with self.assertRaises(SponsorError):j.guard(self.p)
 def test_cancelled_journey_rejects_results(self):
  j=Journey({'cancelled':True})
  with self.assertRaises(SponsorError):j.remaining()
 def test_council_cannot_change_policy(self):
  claims=[]
  for c in self.r['colleges']:
   case=c['cases'][0];claims.append({'college_id':c['college_id'],'category':c['category'],'application_id':case['application_id'],'outcome':case['outcome'],'quote':case['essay'],'student_quote':self.p['essay'][:60],'explanation':'Both mention debugging.','limitation':'Synthetic records do not establish causality.'})
  self.assertEqual(validate_explanations({'colleges':claims},self.p,self.r),[])
  claims[0]['explanation']='The GPA is below the median.'
  self.assertTrue(validate_explanations({'colleges':claims},self.p,self.r))
  claims[0]['category']='Likely';self.assertTrue(validate_explanations({'colleges':claims},self.p,self.r))
