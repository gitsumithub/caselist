# CaseList project context

Start with SPEC.md version 1.5, then docs/SPEC_TRACEABILITY.md. SPEC.md defines the product and acceptance requirements; the audit distinguishes verified behavior from open release gates.

CaseList is a counselor copilot for a high-school student applying to college. One editable profile contains grades, coursework preparation, activities and a draft essay. Build college shortlist starts guarded Nicrron extraction, the counselor confirms source quotations, and the app generates a provisional college list with inspectable applicant evidence. GPA/coursework-only updates reuse confirmed extraction; source edits require confirmation again.

## Scope and data

Supported context: Computer Science, unweighted 4.0 GPA, US demonstration curriculum, 2026 regular decision. synthetic_v2 contains 60 authored applicants and 140 scenario application decisions across six named colleges. College program references come from separately linked official sources. Applicant outcomes are not historical decisions or validated admission predictions. Names are display labels and never affect matching.

Policy demo_v1 computes categories and counts. Council council_v1 uses Claude Haiku 4.5 and GPT-4o mini through Nicrron for independent opinions, anonymous reviews and chairman synthesis. Code validates quotations and preserves policy categories. Malformed chairman output has at most one repair.

PRISM checks input before inference, retrieves versioned KB records, evaluates classified output using rubric_v2 and stores traces. New results/traces include spec version, build commit, dataset/policy/Council versions and working-tree status. Recorded replay is historical evidence, not a fresh run.

## Verified status — October 10, 3:24 PM ET

16 automated tests passed. Fresh spec 1.5 run passed Council, all six KB checks and the attached Evaluator at 95/100. Actual PRISM readback confirmed spec/build identity. Injection was blocked before inference; a deliberately incorrect sparse-cohort category failed at 15/100. Exact receipts and coverage limitations are in docs/SPEC_TRACEABILITY.md.

PRISM separately flagged a trace for automated review under fair_lending; that analysis remains unresolved and is distinct from the policy Evaluator PASS. Real admissions accuracy is unvalidated. See To-Do.md for remaining demo/submission work.

## Development

Open caselist.code-workspace in VS Code. Run `.venv/bin/python server.py`; app: http://127.0.0.1:8765/. Tests: `.venv/bin/python -m unittest discover -s tests -v`.

core.py: matching/policy; live.py: guarded sponsor journey; council.py: model review; release.py: spec/build identity; static/index.html: interface; data/: fixtures and recorded runs; tests/: verification; docs/: audit, sponsor contracts and demo script.

Credentials stay in ignored .env. Do not commit keys or real student records. Repository gitsumithub/caselist remains private. Consult To-Do.md before claiming submission readiness.
