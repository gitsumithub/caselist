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


## Synthetic v2 release, October 10

Replaced identical applicant prose with 60 unique essays and activity descriptions, named scenario students, coursework and explicit generated-outcome provenance. Added six official institution program references, contrasted admitted/rejected scenarios and exposed matching factors. Simplified run status for nontechnical users. SPEC version 1.4 records the remaining real-outcome validation gap. Thirteen automated tests pass, including diversity/provenance checks. Revised live baseline: Council passed, all six KB checks passed, attached Evaluator PASS 95/100; trace ff7c2529-7522-4736-a4e6-973b7cd833da, result 4fcea421-31b9-4ae9-bb25-0f780a3e0dd4. Coursework correction verification is recorded in data/demo_runs.json when complete.

Correction retry passed all checks; source quoting was tightened to each college’s cited case after an initial failed source check. Both saved synthetic_v2 runs now have live_sponsors_verified=true. New-version injection was blocked before model inference. Negative classified-output control failed at 15/100.

All 60 scenario display surnames are distinct. Display names do not enter model packets or policy matching. PRISM reference revision removes name labels and grounds stable application IDs, profiles and outcomes; saved-run KB receipts were refreshed against these documents.

Added a visible student overview above results and verified that correcting rigor updates it immediately. Randomized first/surname pairings reproducibly for all 60 comparison profiles; verified that applicant evidence and outcome fields did not change. Updated saved-run display labels and captured the revised demonstration.

Spec 1.5 audit: 16 tests passed; bounded malformed-chairman repair added and tested. Fresh live run 4d316fd9-c0c0-4a14-b348-3593f307bb0c passed Council, KB and attached Evaluator at 95/100. PRISM readback confirmed spec/build identity. Full requirement mapping and open platform-analysis/submission issues: docs/SPEC_TRACEABILITY.md.
