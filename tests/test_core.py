import copy
import json
from pathlib import Path
import unittest
from core import build_list, validate_claims

ROOT = Path(__file__).resolve().parents[1]


class PolicyTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "data/dataset.json").read_text())
        self.profile = json.loads((ROOT / "data/sample.json").read_text())

    def test_canonical_and_correction(self):
        result = build_list(self.profile, self.data)
        self.assertEqual([c["category"] for c in result["colleges"]], ["Reach", "Target", "Needs review", "Likely", "Needs review", "Needs review"])
        self.profile["rigor"] = 2
        updated = build_list(self.profile, self.data)
        self.assertEqual(updated["colleges"][2]["category"], "Likely")

    def test_missing_and_unsupported_inputs(self):
        for field, value in [("gpa", None), ("gpa", float("nan")), ("major", "History"), ("rigor", None), ("gpa_scale", "weighted_5")]:
            with self.subTest(field=field, value=value):
                self.assertTrue(build_list({**self.profile, field: value}, self.data)["errors"])

    def test_outcomes_do_not_change_retrieval(self):
        before = build_list(self.profile, self.data)
        for app in self.data["applications"]:
            app["outcome"] = "admitted"
        after = build_list(self.profile, self.data)
        self.assertEqual([[c["applicant_id"] for c in col["cases"]] for col in before["colleges"]], [[c["applicant_id"] for c in col["cases"]] for col in after["colleges"]])

    def test_duplicates_not_counted_twice(self):
        self.data["applications"] += copy.deepcopy(self.data["applications"])
        result = build_list(self.profile, self.data)
        self.assertEqual(result["colleges"][4]["n"], 4)

    def test_unseen_profile_and_sparse_results(self):
        self.profile.update(name="Different synthetic person", gpa=3.11, activity_tags=["music"])
        result = build_list(self.profile, self.data)
        self.assertFalse(result["errors"])
        self.assertFalse(result["has_likely"])

    def test_fabricated_claim_is_rejected(self):
        result = build_list(self.profile, self.data)
        case = result["colleges"][0]["cases"][0]
        good = {"college_id": "C01", "category": "Reach", "application_id": case["application_id"], "outcome": case["outcome"], "quote": case["essay"]}
        self.assertEqual(validate_claims([good], result["colleges"]), [])
        for changed in ({"quote": "Invented award"}, {"category": "Likely"}, {"outcome": "unknown"}):
            self.assertTrue(validate_claims([{**good, **changed}], result["colleges"]))


if __name__ == "__main__":
    unittest.main()
