"""Create fixed synthetic teaching cases. Outcomes are designed, not predictions."""
import json
from pathlib import Path
from core import CONTEXT

ROOT = Path(__file__).parent
SAMPLE = {**CONTEXT, "name": "Avery Chen", "gpa": 3.7, "rigor": 1,
          "activity_tags": ["robotics", "peer_tutoring"],
          "activities": "I lead our robotics club and tutor classmates in introductory programming.",
          "essay": "When our robot failed before the showcase, I helped the team test each sensor. Teaching a classmate to debug later showed me that I enjoy making complicated ideas understandable."}


def create():
    names = ["Northbridge College", "Cedar Valley University", "Harbor Institute", "Willow State College", "Summit Arts and Sciences", "Maple Coast University"]
    colleges = [{"college_id": f"C{i+1:02}", "name": name, "fictional": True} for i, name in enumerate(names)]
    outcomes = [["admitted"] + ["rejected"] * 7,
                ["admitted"] * 4 + ["rejected"] * 4,
                ["admitted"] * 7 + ["rejected"],
                ["admitted"] * 6 + ["rejected"] * 2,
                ["admitted"] * 2 + ["rejected"] * 2,
                ["admitted"] * 2 + ["rejected"] * 5 + ["waitlisted"]]
    applicants, applications = [], []
    for ci, group in enumerate(outcomes):
        for offset, outcome in enumerate(group):
            ident = f"A{len(applicants)+1:03}"
            applicants.append({**CONTEXT, "applicant_id": ident, "name": f"Synthetic applicant {ident}",
                               "gpa": round(3.5 + .02 * offset, 2), "rigor": 2 if ci == 2 else 1,
                               "activity_tags": ["robotics", "peer_tutoring"],
                               "activities": "Participated in robotics and tutored peers in programming.",
                               "essay": "I learned to explain debugging steps while helping another student repair a robotics project."})
            applications.append({"application_id": f"APP{len(applications)+1:03}", "applicant_id": ident,
                                 "college_id": f"C{ci+1:02}", "cycle": 2026, "round": "regular", "outcome": outcome})
    # Dissimilar cases keep the cohort threshold visible; their outcomes do not control ranking.
    while len(applicants) < 60:
        ident = f"A{len(applicants)+1:03}"
        applicants.append({**CONTEXT, "applicant_id": ident, "name": f"Synthetic applicant {ident}",
                           "gpa": 2.0, "rigor": 0, "activity_tags": ["music"],
                           "activities": "Played in the school orchestra.", "essay": "Practicing music helped me work patiently through difficult passages."})
        for college in colleges:
            applications.append({"application_id": f"APP{len(applications)+1:03}", "applicant_id": ident,
                                 "college_id": college["college_id"], "cycle": 2026, "round": "regular", "outcome": "rejected"})
    dataset = {"version": "synthetic_v1", "synthetic": True, "colleges": colleges, "applicants": applicants, "applications": applications}
    data = ROOT / "data"
    data.mkdir(exist_ok=True)
    (data / "dataset.json").write_text(json.dumps(dataset, indent=2) + "\n")
    (data / "sample.json").write_text(json.dumps(SAMPLE, indent=2) + "\n")
    # Upload-ready references; these files are not a claim of a completed KB integration.
    kb = data / "prism_kb"
    kb.mkdir(exist_ok=True)
    by_id = {p["applicant_id"]: p for p in applicants}
    for college in colleges:
        lines = [f"# {college['name']} | {college['college_id']}", "SYNTHETIC DEMONSTRATION DATA. Dataset synthetic_v1. Not real admissions outcomes.", ""]
        for app in applications:
            if app["college_id"] == college["college_id"]:
                person = by_id[app["applicant_id"]]
                lines.extend([f"## {app['application_id']} | {person['applicant_id']}",
                              f"College: {app['college_id']}; cycle: {app['cycle']}; round: regular; outcome: {app['outcome']}.",
                              f"Major: Computer Science. Unweighted GPA: {person['gpa']}/4.0. Rigor level: {person['rigor']}.",
                              f"Activities: {person['activities']}", f"Essay: {person['essay']}", ""])
        (kb / f"{college['college_id']}.md").write_text("\n".join(lines))
    print(f"Created {len(applicants)} synthetic applicants and {len(applications)} applications.")


if __name__ == "__main__":
    create()
