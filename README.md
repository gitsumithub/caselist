# CaseList

A counselor workspace using synthetic applicant records, deterministic provisional categories, a two-model Nicrron LLM Council, and live PRISM controls. Read [SPEC.md](SPEC.md) for scope and acceptance requirements.

Run locally:

```sh
python3 -m venv .venv
.venv/bin/pip install 'prismtrace-sdk>=0.5.1' httpx
# Copy .env.example to .env and configure your existing credentials.
.venv/bin/python setup_prism.py
.venv/bin/python server.py
```

Open http://127.0.0.1:8765. Load sample, extract experiences, review exact quotations, and confirm facts to build with Council. Change rigor from 1 to 2 and rebuild to inspect the correction. Local comparison remains available separately.

The Council calls `anthropic/claude-haiku-4-5` and `openai/gpt-4o-mini` through Nicrron. Independent opinions receive anonymous peer review; Haiku synthesizes explanations. This implementation is inspired by Karpathy’s LLM Council. Categories are assigned by `core.py`, never by model voting. Exact citations are checked against canonical records.

PRISM evaluates input before inference, grounds outcome claims using six uploaded reference documents, captures model stages, and evaluates the classified output. Missing, failed or timed-out checks leave categories under review. Each run is bounded to 90 seconds and can be cancelled. Credentials stay in ignored `.env`; raw synthetic run evidence stays in ignored `runs/`.

```sh
python3 -m unittest discover -s tests -v
```

All colleges and records are fictional. Categories are provisional demonstration labels, not validated admission predictions. Live check status applies only to its recorded run. See `docs/DELIVERY_RECORD.md` for verified results and remaining submission tasks.

The three-minute narrated screenshot walkthrough is `docs/demo/CaseList-demo.mp4` locally (ignored by Git). To rebuild after updating captured screenshots, install `imageio-ffmpeg` and run `.venv/bin/python scripts/build_demo.py` on macOS. The live rehearsal script is `docs/DEMO_SCRIPT.txt`.
