# CaseList local project context

Read `SPEC.md` (version 1.2), then `README.md`. The specification is the authoritative product and acceptance contract; this file summarizes the local handoff.

## Product and demo

CaseList helps a counselor inspect a provisional college list against synthetic applicant outcomes and correct a student fact. The supported domain is Computer Science, unweighted GPA on a 4.0 scale, US_demo curriculum, 2026 cycle and regular decision. Categories follow the deterministic `demo_v1` policy; they are not validated admission probabilities.

The frozen `synthetic_v1` dataset contains 60 applicants, 140 applications and six fictional colleges. Avery Chen's baseline categories in C01–C06 order are Reach, Target, Needs review, Likely, Needs review, Needs review. Correcting rigor from 1 to 2 changes C03 to Likely. Sparse C05 and unresolved C06 stay under review.

## Implementation map

- `core.py`: profile validation, eligibility, similarity ranking, category policy and exact structured claim checks.
- `server.py`: localhost HTTP server, state and comparison endpoints, explicit blocking of unsupported live processing.
- `static/index.html`: profile entry, comparison, evidence inspection and correction workflow.
- `data/`: frozen fixtures, sample and prepared Prism reference documents.
- `integrations.py`: connectivity helpers and readiness reporting; mandatory live controls are unfinished.
- `tests/test_core.py`: six tests for canonical/corrected results, input limits, outcome-independent retrieval, deduplication, unseen inputs and fabricated claims.
- `docs/PRISM_SETUP.md`: sponsor interface questions and required positive/negative examples.

## Local commands

Open `caselist.code-workspace` in VS Code. Run `python3 server.py` and visit http://127.0.0.1:8765. Run checks with `python3 -m unittest discover -s tests -v`. No third-party packages are required for the local preview.

Keep credentials in ignored `.env`, using `.env.example` for variable names. Never commit credentials or real student records.

## Remaining dependencies

Live Nicrron extraction/explanations and Prism Guardrail, Knowledge Base, Evaluator and trace verification remain pending. Obtain sponsor-supported interfaces before implementing mandatory controls; local comparison and connectivity tests do not satisfy the live release gate. Preserve actual results and visibly report failed or pending checks.

The spec also requires a compact delivery record, clean-start verification, demo video, accessible GitHub repository and all eight Devpost fields. This setup creates a local repository only. Public submission requires subsequent user authorization under the spec.
