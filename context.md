# CaseList — project reference

A short fallback for the project owner in VS Code. This is not a mandatory agent context file or a running transcript. Update it only when the project’s purpose, scope or authoritative references change.

**Purpose:** Help a counselor build and inspect a provisional college shortlist from a high-school student’s grades, activities and draft essay.

**Current scope:** Computer Science; unweighted 4.0 GPA; 2026 regular decision. Applicant profiles and outcomes are synthetic. College program facts have separate official sources. Admission accuracy is not validated.

**Workflow:** Edit one profile → build shortlist → confirm extracted experiences → inspect college results and supporting evidence.

**Integrations:** Nicrron provides extraction and LLM Council explanations. PRISM provides input checks, Knowledge Base retrieval, output evaluation and traces. Code controls matching and categories.

## Where to check

- [SPEC.md](SPEC.md): requirements; active version 1.5.
- [To-Do.md](To-Do.md): current work, completed work and remaining actions.
- [docs/SPEC_TRACEABILITY.md](docs/SPEC_TRACEABILITY.md): tests, live receipts and unresolved validation gaps.
- [README.md](README.md): run and setup instructions.
- [docs/DEMO_SCRIPT.txt](docs/DEMO_SCRIPT.txt): demo walkthrough.

**Local app:** http://127.0.0.1:8765/ · **VS Code workspace:** caselist.code-workspace

**Boundaries:** Keep credentials out of Git. Keep the repository private as requested. Final Devpost submission requires the owner's authorization.
