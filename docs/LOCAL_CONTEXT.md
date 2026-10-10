# CaseList local project context

Read `SPEC.md` (version 1.3), then `README.md`. The specification is the authoritative product and acceptance contract; this file summarizes the local handoff.

## Product and demo

CaseList helps a counselor inspect a provisional college list against synthetic applicant outcomes and correct a student fact. The supported domain is Computer Science, unweighted GPA on a 4.0 scale, US_demo curriculum, 2026 cycle and regular decision. Categories follow the deterministic `demo_v1` policy; they are not validated admission probabilities.

The frozen `synthetic_v2` dataset contains 60 applicants, 140 applications and six named colleges with official program references. Avery Chen's baseline categories in C01–C06 order are Reach, Target, Needs review, Likely, Needs review, Needs review. Correcting rigor from 1 to 2 changes C03 to Likely. Sparse C05 and unresolved C06 stay under review.

## Implementation map

- `core.py`: profile validation, eligibility, similarity ranking, category policy and exact structured claim checks.
- `server.py`: localhost HTTP server, state, comparison, live jobs, cancellation and recorded playback endpoints.
- `static/index.html`: profile entry, comparison, evidence inspection and correction workflow.
- `data/`: frozen fixtures, sample and prepared Prism reference documents.
- `integrations.py`: Nicrron calls, connectivity helpers and configuration reporting.
- `tests/test_core.py`: six tests for canonical/corrected results, input limits, outcome-independent retrieval, deduplication, unseen inputs and fabricated claims.
- `docs/PRISM_SETUP.md`: verified sponsor contracts and positive/negative controls.

## Local commands

Open `caselist.code-workspace` in VS Code. Run `python3 server.py` and visit http://127.0.0.1:8765. Run checks with `python3 -m unittest discover -s tests -v`. No third-party packages are required for the local preview.

Keep credentials in ignored `.env`, using `.env.example` for variable names. Never commit credentials or real student records.

## Remaining submission dependencies

The video is built locally. Loom upload awaits sign-in. Judge access to the private repository and final Devpost submission remain outstanding. Public submission requires subsequent user authorization under the spec.

## Live Council release

Nicrron extraction and two-model Council are implemented in live.py/council.py. PRISM Guardrail, Knowledge Base and classified-output Evaluator have verified recorded controls. Read docs/DELIVERY_RECORD.md for IDs and limits. Recorded demonstration is labeled historical and can be opened in the app. docs/demo/CaseList-demo.mp4 is a three-minute narrated screenshot walkthrough; docs/DEMO_SCRIPT.txt supports a live rehearsal. Devpost overview and story are saved; required video link, private repository judge access and final submission remain pending.


October 10 revision: synthetic_v2 contains 60 distinct authored applicant essays and activity descriptions, 140 scenario application outcomes, coursework, contrasting admitted/non-admitted examples, and six separately sourced official college program references. Applicant decisions are designed policy fixtures, not reported decisions by the named colleges. Real-outcome validation remains a production requirement. Use docs/DEMO_SCRIPT.txt for the revised recording; previous video screenshots describe an older release.
