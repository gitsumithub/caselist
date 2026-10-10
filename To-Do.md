# CaseList remaining work

Use SPEC.md v1.5 and docs/SPEC_TRACEABILITY.md as the acceptance references. This list records work, not implied approval to publish.

## Before the 4:30 PM ET submission deadline

- [ ] Rehearse the simplified workflow: Build college shortlist → confirm experiences → inspect results. Verify the one-click GPA/coursework update and source-edit re-confirmation in the browser.
- [ ] Refresh the video to show the latest single-profile interface and button labels. The existing local video predates this last simplification.
- [ ] Publish the demo to Loom and make the video playable for judges. Check the link without owner credentials.
- [ ] Put the playable video URL into the Devpost draft and reconcile its story with the actual synthetic-data scope and sponsor behavior.
- [ ] Arrange judge access to the private GitHub repository; judge GitHub usernames are still needed. Keep the repository private as requested.
- [ ] Review all eight submission fields and both links against SPEC.md. Obtain the user's final submission authorization, then submit and verify persistence.

## Review and validation

- [ ] Review PRISM's separate fair_lending/requires_review analysis with the sponsor; retain the flag until resolved.
- [ ] Verify account-level one-workspace/team and project-naming requirements; trace agent_name=caselist has been verified.
- [ ] Test usability with someone unfamiliar with the app.
- [ ] For production, obtain a permissioned historical applicant/outcome dataset and evaluate recommendation accuracy. Synthetic fixtures do not validate predictions.

## Completed

- [x] SPEC.md v1.5 identified; requirement evidence matrix saved.
- [x] 16 automated tests passed, including bounded malformed-output repair.
- [x] Fresh live spec 1.5 Council/KB/Evaluator checks passed; PRISM persisted spec/build identity.
- [x] Input-injection and deliberately wrong-output controls exercised.
- [x] Distinct synthetic profiles, randomized name pairings and separately sourced college program references.
- [x] Single editable profile; one main build action; demo and technical controls collapsed.
