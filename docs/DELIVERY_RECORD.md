# CaseList delivery record — October 10, 2026

Specification 1.3; council_v1; frozen synthetic_v1; demo_v1.

## Verified live results

- Baseline run `9a9bc8d3-093e-4d71-a4d1-f0c5a1bd7edc`: six expected categories; Council source validation passed, six KB queries passed, Guardrail allowed, classified-output Evaluator PASS 95.0/100. Trace `d8f0783a-576b-41c0-b13c-7b8de69ad04c`.
- Correction run `17cc1e70-74ce-4c7a-bcec-12d9599ac0a2`: rigor 2 makes Harbor Likely; all live checks passed. Evaluator trace `6304d9c2-bb24-492b-9891-1e0e859ab1d2`.
- Injection control `45ede45a-2e2f-420d-8c01-e624e4bbbfde`: real PRISM block before inference. Custom regex augments the default detector; coverage is limited to demonstrated phrases.
- Deliberately wrong sparse-data category: FAIL 15.0/100; trace `7ab90eb8-039d-43d1-af77-9687ee56c09b`; result `c763ebbc-5156-40e9-8cf2-dc37e7af3588`.
- Eleven automated tests pass. Browser extraction and Council rendering were exercised.

## Implementation

Nicrron routes Haiku 4.5 and GPT-4o mini through independent opinions, anonymous peer reviews and chairman synthesis. No OpenRouter dependency or copied Council implementation. Code preserves policy categories, verifies exact citations and restricts chairman prose to essay experiences. PRISM checks classified output in a compact shared-reference payload; it does not judge the full Council prose. Missing or failed checks produce review status. Jobs are cancellable with a 90-second limit.

Replay evidence is in `data/demo_runs.json`, explicitly labeled Recorded run. Raw synthetic prompts/responses remain in ignored `runs/`. Secrets remain in ignored `.env`. The app is local at http://127.0.0.1:8765.

## Submission state

The existing Devpost draft is now CaseList. Overview, pitch, story, Python tag and repository URL were saved. Draft: https://devpost.com/submit-to/31652-get-hired-hack-columbia-startup-lab/manage/submissions/1229455-caselist/additional-info/edit

A public demo-video URL is required. The repository is private by user preference; judge access is unverified. Final Devpost submission and public application deployment are not complete. No claims of real admissions validation.
