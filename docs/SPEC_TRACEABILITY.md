# CaseList specification traceability audit
Checked: 2026-10-10T15:22:31.163945-04:00
Active specification: SPEC.md version 1.5; SHA-256 `5592f98b048094f28c28f61e688be65a394fbb1a53277d84dcbe734b30079226`.
Dataset synthetic_v2; deterministic policy demo_v1; Council council_v1; evaluator rubric_v2.
Automated verification: 16 unittest checks passed. These prove mechanics, not admission accuracy.

| Requirement | Implementation and evidence | Status |
|---|---|---|
| Profile → provisional college list | core.build_list; test_canonical_and_correction; independent data/expected_results.json | PASS |
| Unseen and unsupported profiles | test_unseen_profile_and_sparse_results; test_missing_and_unsupported_inputs | PASS within supported context |
| Distinct synthetic records; provenance | test_distinct_profiles_and_explicit_provenance; test_official_facts_separate_from_outcomes | PASS |
| Outcome-independent retrieval and deduplication | test_outcomes_do_not_change_retrieval; test_duplicates_not_counted_twice | PASS |
| Source-supported extraction and final quotations | test_invented_extraction_rejected; test_fabricated_claim_is_rejected; test_council_cannot_change_policy | PASS local validation; semantic explanation quality needs human review |
| Bounded chairman format repair | test_malformed_chairman_has_one_repair; test_malformed_repair_never_passes | PASS; fresh live retry also passed |
| Guardrail before inference | test_guardrail_fails_closed; synthetic_v2 injection control blocked with model_called=false | PASS for exercised attack; broader injection robustness unvalidated |
| Actual KB claim and version checking | test_wrong_kb_document_rejected; six saved baseline/correction queries with actual document/chunk IDs in data/demo_runs.json | PASS on saved runs; not a new run |
| Attached Evaluator positive and negative controls | Saved synthetic_v2 baseline/correction PASS 95/100; wrong sparse-cohort category FAIL 15/100 | PASS on saved runs |
| Correction and stale-state handling | Baseline/rigor_2 independent expectations; browser checked edit invalidation and two-step extraction → confirmation; GPA/coursework-only reuse implemented | Mechanical PASS; one-click reuse browser validation pending |
| Cancellation and unavailable mandatory checks | test_cancelled_journey_rejects_results; test_guardrail_fails_closed; latest malformed Council run preserved Needs review | PASS for tested paths; no full network fault-injection suite |
| Spec identity on every new trace | release.py adds spec version, code commit and dirty-state metadata to live.Journey.trace and results | PASS: read back from PRISM with spec_version 1.5, tested build commit and working_tree_modified=false |
| Trace project/agent/session | Actual trace IDs and session/revision retained in runs; project ID stored in data/prism_config.json; agent_name caselist | API evidence available; one-org/team-name account compliance not independently reverified |
| Simpler usable interface | Single editable profile; main build button; technical/demo controls collapsed; browser extraction and confirmation checked | Implemented; unfamiliar-user usability study not performed |
| Reasoning grounded in real outcomes | Applicant outcomes are explicitly authored, as authorized by user | NOT EMPIRICALLY VALIDATED; no historical outcome dataset |
| Complete submission and judge-accessible links | Private GitHub source; local demo video; Devpost draft | OPEN: Loom publication, judge access and final submission |

## Live evidence receipts
- Saved synthetic_v2 baseline: trace `ff7c2529-7522-4736-a4e6-973b7cd833da`, evaluator result `4fcea421-31b9-4ae9-bb25-0f780a3e0dd4`, PASS 95.0/100; Council passed and KB passed.
- Saved synthetic_v2 corrected: trace `7eaaa399-8122-414d-ac85-8adafbc7ffaa`, evaluator result `e8792834-d6c2-4895-8040-da2d19f52511`, PASS 95.0/100; Council passed and KB passed.
- Negative control: trace `01d71d6a-ba16-428a-ae5c-7e3a11e2107d`, result `4f15eeaf-3386-4a8e-aa03-6d357e3523d9`, FAIL 15.0/100.
- Latest UI run at 15:19:57 ET: c1d855ce-b634-4763-aa1f-7dee9fa390f4; Council malformed JSON, overall incomplete. Classified-output trace 955a7b49-aced-446d-aaf1-2a4ced8dab3d passed 95/100 but does not certify Council or overall readiness. The failure prompted the bounded repair fix.

## Release conclusion
The implementation is a tested synthetic demonstration. Fresh live retry passed the required controls. Full release gates remain open for submission links/access checks, account-compliance review and the acknowledged real-outcome validation limitation. No test or Council agreement certifies admission predictions.

## Fresh spec 1.5 live verification

Tested code commit: `b857f9dd1fe7e79b9cfeb538e1be3040fd68af9b`; working tree clean at run start. Run `4d316fd9-c0c0-4a14-b348-3593f307bb0c`. Council passed; all six KB claims passed; attached Evaluator PASS 95.0/100. Evaluator trace `2aa67bad-e1da-4188-9c8e-d41252735d19`, result `01288e4f-f12d-4c8d-a6cc-a227516725b0`. The classified-output trace was read back from PRISM: spec version 1.5, dataset synthetic_v2, policy demo_v1, Council council_v1, code commit, session/revision, and agent_name caselist persisted.

Separate PRISM automated analysis marked the trace requires_review=true with regulatory_category=fair_lending. This is separate from the attached policy Evaluator PASS, appears to classify this admissions scenario under an unrelated financial domain, and has not been resolved or cleared. It is retained as a platform-analysis review item, not concealed by the required-control pass.
