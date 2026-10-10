"""Deterministic comparison policy. No network calls or admissions predictions."""
from collections import Counter
from statistics import median
import math

POLICY_VERSION = "demo_v1"
CONTEXT = {"gpa_scale": "unweighted_4", "curriculum": "US_demo", "major": "Computer Science", "cycle": 2026, "round": "regular"}


def validate_profile(profile):
    errors = []
    for name, expected in CONTEXT.items():
        if profile.get(name) != expected:
            errors.append(f"{name}: this demo requires {expected}; received {profile.get(name)!r}.")
    gpa = profile.get("gpa")
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)) or not math.isfinite(gpa) or not 0 <= gpa <= 4:
        errors.append("Enter an unweighted GPA from 0 to 4. No conversion is assumed.")
    if type(profile.get("rigor")) is not int or profile["rigor"] not in (0, 1, 2):
        errors.append("Confirm course rigor: 0 standard, 1 some advanced, or 2 extensive advanced coursework.")
    tags = profile.get("activity_tags")
    if not isinstance(tags, list) or any(not isinstance(x, str) or len(x) > 80 for x in tags):
        errors.append("Activity tags must be a list of short, confirmed descriptions.")
    for name in ("essay", "activities"):
        if not isinstance(profile.get(name), str) or not profile[name].strip():
            errors.append(f"Provide {name}; missing evidence is not inferred.")
    if sum(len(str(profile.get(k, ""))) for k in ("essay", "activities")) > 12000:
        errors.append("The combined essay and activities must be at most 12,000 characters.")
    return errors


def similarity(student, applicant):
    gpa = max(0, 1 - abs(student["gpa"] - applicant["gpa"]))
    rigor = 1 - abs(student["rigor"] - applicant["rigor"]) / 2
    left, right = set(student["activity_tags"]), set(applicant["activity_tags"])
    overlap = len(left & right) / len(left | right) if left | right else 0
    return round(.5 * gpa + .3 * rigor + .2 * overlap, 8)


def retrieve(student, college_id, dataset):
    applicants = {x["applicant_id"]: x for x in dataset["applicants"]}
    selected, seen = [], set()
    for application in dataset["applications"]:
        if application["college_id"] != college_id or application["applicant_id"] in seen:
            continue
        person = applicants.get(application["applicant_id"])
        if person is None or any(person.get(k) != student.get(k) for k in ("gpa_scale", "curriculum", "major")):
            continue
        if any(application.get(k) != student.get(k) for k in ("cycle", "round")):
            continue
        if application["outcome"] not in ("admitted", "rejected", "waitlisted"):
            continue
        score = similarity(student, person)
        if score < .65:
            continue
        seen.add(person["applicant_id"])
        selected.append({**person, **application, "similarity": score,
                         "gpa_difference": round(student["gpa"] - person["gpa"], 2),
                         "rigor_difference": student["rigor"] - person["rigor"]})
    return sorted(selected, key=lambda x: (-x["similarity"], x["applicant_id"]))[:8]


def classify(student, cases):
    counts = {k: sum(c["outcome"] == k for c in cases) for k in ("admitted", "rejected", "waitlisted")}
    a, w = counts["admitted"], counts["waitlisted"]
    result = {"counts": counts, "n": len(cases), "category": "Needs review", "policy_version": POLICY_VERSION}
    if len(cases) < 8:
        result["reason"] = f"Only {len(cases)} comparable cases meet the threshold; the demo policy requires eight."
    elif a + w <= 2:
        result.update(category="Reach", reason="At most two of eight cases were admitted or have unresolved waitlists.")
    elif a >= 3 and a + w <= 5:
        result.update(category="Target", reason="Three to five of eight cases remain admitted under every waitlist resolution.")
    elif 6 <= a <= 8:
        admitted = [c for c in cases if c["outcome"] == "admitted"]
        gpa_median, rigor_median = median(c["gpa"] for c in admitted), median(c["rigor"] for c in admitted)
        result.update(admitted_gpa_median=gpa_median, admitted_rigor_median=rigor_median)
        if student["gpa"] < gpa_median or student["rigor"] < rigor_median:
            result["reason"] = f"Favorable counts, but the student's GPA or rigor is below the admitted-case medians ({gpa_median:g}, level {rigor_median:g})."
        elif w:
            result["reason"] = "An unresolved waitlist prevents a Likely assessment under this demo policy."
        else:
            result.update(category="Likely", reason="Six or more of eight were admitted; both academic median checks pass. This is a provisional demo category.")
    else:
        result["reason"] = "Unresolved waitlists can cross a category boundary. Keep this college under review."
    return result


def build_list(profile, dataset):
    errors = validate_profile(profile)
    if errors:
        return {"errors": errors, "colleges": [], "policy_version": POLICY_VERSION}
    colleges = []
    for college in dataset["colleges"]:
        cases = retrieve(profile, college["college_id"], dataset)
        admitted = next((c for c in cases if c["outcome"] == "admitted"), None)
        other = next((c for c in cases if c["outcome"] != "admitted"), None)
        colleges.append({**college, **classify(profile, cases), "cases": cases,
                         "contrast": {"admitted": admitted, "other": other}})
    return {"errors": [], "colleges": colleges, "policy_version": POLICY_VERSION,
            "dataset_version": dataset["version"], "has_likely": any(c["category"] == "Likely" for c in colleges),
            "category_counts": dict(Counter(c["category"] for c in colleges))}


def validate_claims(claims, colleges):
    """Check structured model claims against the exact retrieved evidence."""
    errors = []
    by_college = {c["college_id"]: c for c in colleges}
    for claim in claims:
        college = by_college.get(claim.get("college_id"))
        if not college:
            errors.append("Unknown college ID")
            continue
        if claim.get("category") != college["category"]:
            errors.append("Category differs from policy")
        case = next((c for c in college["cases"] if c["application_id"] == claim.get("application_id")), None)
        if not case or case["outcome"] != claim.get("outcome"):
            errors.append("Unknown application or changed outcome")
            continue
        quote = claim.get("quote", "")
        if not isinstance(quote, str) or not quote.strip() or not any(quote in case[k] for k in ("essay", "activities")):
            errors.append("Unsupported quotation")
    return errors
