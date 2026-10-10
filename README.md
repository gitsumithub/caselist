# CaseList local starter

Open `caselist.code-workspace` in VS Code. Read `SPEC.md` first.

Run from the integrated terminal (Python 3.10+; no packages required):

```sh
python3 server.py
```

Open http://127.0.0.1:8765. Load Avery, build the comparison, inspect the evidence, then change rigor from 1 to 2 and rebuild. Run tests with `python3 -m unittest discover -s tests -v`.

## Current scope

Working local comparison, deterministic provisional categories, exact source records, editable profile, stale-result invalidation and a correction summary. All records and colleges are fictional. Manual profile entry is explicit; this starter does not claim live AI extraction or sponsor verification.

Nicrron and Prism are **not yet verified**. Put credentials in a local `.env` using `.env.example`. Never paste keys into chat or commit them. Get the three missing Prism control examples from the sponsor; see `docs/PRISM_SETUP.md`. The app deliberately blocks live student processing until those controls are implemented. `python3 integrations.py --smoke` is only a harmless model/trace connectivity test and cannot pass the full release gate.

## Recorded changes from the initial plan

- Package downloads failed in the current build session. Python's built-in server and a plain HTML interface replace Streamlit. The project runs without dependencies.
- Frozen synthetic_v1 contains 60 applicants, **140** applications and six colleges. This replaces the approximate 180-record planning target while preserving all six expected demo cases.
- Sponsor access is unresolved. Local work is a development preview; the hackathon submission is not complete.

## Files

- `SPEC.md`: product, controls, tests, judging and all eight submission requirements.
- `core.py`: eligibility, similarity, categories and exact claim validation.
- `data/`: synthetic records and upload-ready Prism reference documents.
- `server.py`, `static/index.html`: local app.
- `integrations.py`: verified Nicrron request and Prism trace contracts; explicit pending controls.
- `docs/PRISM_SETUP.md`: sponsor questions and acceptance examples.

No GitHub project, deployment, video or Devpost submission has been created. This repository is local.
