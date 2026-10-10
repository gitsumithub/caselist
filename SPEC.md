# CaseList Counselor Copilot Build Specification

CaseList generates a provisional reach / target / likely college list from a student’s grades, activities and draft essay, supported by inspectable past applicant records. A counselor can examine conflicting outcomes, correct a profile fact and regenerate the list.

Track: NERD APPLY, The Counselor Copilot. Event: Get Hired Hack at Columbia Startup Lab, October 10, 2026. Specification version: 1.4. On October 10 the user explicitly authorized adding LLM Council through Nicrron and completing the live app and demo. Version 1.2 remains preserved in Git history. The live Council journey and sponsor control checks have passed on recorded synthetic runs; see docs/DELIVERY_RECORD.md. Public video and judge access remain submission requirements.

All student histories and outcomes in this prototype are synthetic, as explicitly authorized by the user on October 10. The prototype demonstrates traceable behavior against those records; it does not validate admissions predictions.

## Start here and first five minutes

Big idea: generate a college list whose evidence a counselor can inspect, challenge and correct. Each recommendation shows comparable applicants with different outcomes, material differences and evidence limits. One correction recomputes the list. Nicrron performs extraction and explanation; Prism checks input, grounds at least one displayed claim through its Knowledge Base, evaluates classified output and records the journey. This is the fixed acceptance scenario for build, demo and maintenance.

Start the 120-minute clock only when implementation is authorized. The first five minutes are blocker triage, not a promise to finish the integrations. Record each result as pending, passed or blocked, with evidence and an owner. All checks are currently pending.

| Minute | What to establish | Failure and response |
| --- | --- | --- |
| 0 to 1 | Working runtime, repository, named build/submission owner; Devpost editing and video-upload access | Resolve access before UI work. Confirm one team, one project and one track |
| 1 to 2 | Tiny live Nicrron call using the actual key; record accessible model, latency, finish state and usable JSON | Ask the Nicrron owner for the fastest reliable model and supported structured-output parameters; dashboard login is insufficient |
| 2 to 3 | Prism Builder access, correct project, ingest/read key and agent_name; one real trace visible | Resolve credit, key-scope or project mismatch with Prism support |
| 3 to 4 | Sponsor-confirmed path for an input Guardrail before Nicrron inference, Knowledge Base upload/query, and attaching/reading an Evaluator | Get working examples from the owners. Trace ingestion alone does not satisfy these requirements. Do not guess endpoints or assume proxy compatibility |
| 4 to 5 | One hand-worked eight-case cohort; synthetic-data and fictional-college scope explained to NERD APPLY | Confirm acceptable demonstration scope and obtain an unseen profile/edge case if available; keep heuristic categories explicitly provisional |

By minute 20, prove the smallest complete sponsor journey: benign input passes its Prism Guardrail, Nicrron returns usable content, a displayed claim cites an actual Prism Knowledge Base result, a classified output receives its attached Evaluator result, and the run is visible under the correct project and agent_name. Also exercise one injected input and one deliberately wrong classified output. If a required capability is unavailable, stop feature expansion and resolve it with the sponsor. Continue only independent fixture or submission preparation. Logos, local substitutes and recorded traces cannot replace these live requirements.

### Risks that change the build

| Risk | Why it could derail this prototype | Required control |
| --- | --- | --- |
| Sponsor integration incompatibility | Public Prism docs describe inline blocking through its proxy, but a Nicrron upstream and the required KB/Evaluator calls have not been verified | Obtain a sponsor-supported working path before UI work. An after-the-fact trace is not proof of prevention |
| No usable comparison cohort | Sixty applicants divided by major, college and context may leave fewer than eight eligible cases everywhere | Support one intended-major group for the two-hour demo; verify cohort coverage before UI work and leave unsupported inputs visibly unresolved |
| Fragile category rules | One waitlisted record can trigger blanket abstention; one changed record can cross an arbitrary threshold | Use the explicit unresolved-outcome rule below. Describe categories as demo heuristics and retain the selected records and counts |
| Plausible but invalid model output | Valid JSON can still contain fabricated grades, unsupported tags or incorrect citations | Validate the schema and exact source support; expose editable extraction and enforce category rules in code |
| Unsupported essay interpretation | A fluent explanation can imply personality or causes of admission that the records never establish | Use quoted experiences and interests only; keep interpretations qualified and separate from recorded facts |
| Misleading evaluation | A fixture set built to produce a desired list can appear to prove admission accuracy | Freeze records before testing; use separate hand-authored edge cases and report mechanical correctness separately from predictive validity |
| Stale results or duplicate calls | An interface rerun can mix edited facts with an old explanation or repeat paid inference | Explicit submit actions; input hash, profile revision and run ID; edits invalidate acceptance; no inference on every keystroke |
| Oversized request or network failure | Full essays for dozens of applicants can inflate latency and token use; event WiFi may fail | Send compact evidence packets, cap output, bound retries, record a successful live run before polishing |
| Submission access failure | A local app can work while the repository or video is inaccessible to judges | Verify GitHub permissions, recording/upload access and Devpost editing access early; test the final links without owner credentials |

The supported fixture domain is Computer Science, one curriculum context, one application round and one cycle. This is a disclosed demo boundary; unsupported values return a named limitation. Display the context beside the profile. Do not infer a real student's curriculum, cycle or round from an essay. A narrow domain improves two-hour feasibility but may limit judging utility; validate that tradeoff with NERD APPLY. Any edit invalidates prior result and validation status.

## Product and practical use

The counselor is preparing a student advising session. The student supplies a profile and an essay, and needs a first college list. The counselor needs to understand why each college appears, where the evidence disagrees and what information is missing.

The core outcome is a generated list with source-backed reasons. The distinctive interaction is reviewing comparable applicants with different admission outcomes before accepting a recommendation. A list summary also identifies when no college has adequate support for a provisional likely category.

Success means the counselor can generate a list, inspect the records behind one recommendation and correct one fact without a walkthrough. “Needs review” is a valid result when the evidence cannot support a category.

## Nonnegotiable release gates

Release readiness requires all three gates below. Every item is pending until its evidence is verified. The judging checks are our internal readiness tests against the organizer’s rubric; passing them does not guarantee a judge’s score.

### Gate 1 Working prototype and required integrations

| Requirement | Pass evidence |
| --- | --- |
| Built during the event | Implementation within the October 10, 11:15 AM to 4:30 PM ET hacking window; repository history and dependency disclosure |
| Working NERD APPLY prototype | Grades, activities and a draft essay produce a provisional college list with retrieved applicant outcomes |
| Visible uncertainty | Missing inputs, sparse matches, conflicting evidence and failed checks produce named clarification or review states |
| NicrronNinoo | Fresh live Nicrron responses actually drive extraction and explanations |
| Prism input Guardrail | Configured on student input; benign case passes and injected instructions trigger the intended action, with a retained result |
| Prism output Evaluator | Attached to classified college output; correct and deliberately incorrect results are checked against the saved rubric and references |
| Prism Knowledge Base | Reference records are uploaded, queried and used to ground at least one visible claim; returned evidence and its document ID are inspectable |
| Prism trace and organization rules | One organization per team; project named after team; agent_name on every SDK call; shared session/revision identifiers and visible live traces |
| Checkable output | Source records, IDs, counts, policy, validation results and sponsor evidence can be inspected by the judge |

### Gate 2 Complete Devpost submission

All eight items must be present in the Devpost project page and checked against the implemented product.

- [ ] Project name and one-line description: CaseList, with a concise description matching the delivered behavior.

- [ ] Track: NERD APPLY, The Counselor Copilot.

- [ ] What was built and why: the actual profile-to-list workflow, counselor need and demonstrated distinction.

- [ ] Accuracy and uncertainty: evidence references, validation, review conditions, test results and synthetic-data limitations.

- [ ] Tools and technologies: explicitly name NicrronNinoo and Block Convey Prism, describe their actual roles, and list the supporting stack.

- [ ] Team member names and roles: every member and their actual contribution; no invented contributors.

- [ ] Video demo link: a playable recording showing the complete workflow, an uncertainty case and both live sponsor integrations.

- [ ] GitHub repository link: accessible source, fixtures, policy, tests, README and setup instructions; no credentials committed.

Before authorized submission, verify the prepared fields and both links. After submission, reopen the Devpost page and confirm that all eight items persisted and both links work for a judge without owner credentials. Distinguish “submission ready” from “submitted.”

### Gate 3 Evidence against all four judging criteria

| Criterion | Organizer’s question | Internal pass evidence |
| --- | --- | --- |
| Technical Execution 5 | Does it actually work, and does it get the right answer? | Live end-to-end run; expected cases and categories match hand-authored fixtures; counts are correct; correction reruns successfully; unseen valid and invalid inputs tested; measured results recorded |
| Trust and Explainability 5 | Can a user see why the AI said what it said? Does it flag what it does not know instead of bluffing? | Clickable or expandable source records; faithful quotes and outcomes; missing and sparse evidence visibly handled; no fabricated certainty; live Guardrail, Knowledge Base and Evaluator evidence |
| Design 5 | Could a counselor, pharmacist or investor use this tomorrow without a walkthrough? | For this track, an unfamiliar reviewer can load a student, generate a list, inspect evidence and correct a fact without verbal instruction |
| Uniqueness of Idea 5 | Did you find a sharper angle on the problem? | Demo juxtaposes comparable applicants with different outcomes, identifies the limit of the inference, and shows how a counselor correction changes the evidence and list |

Each criterion carries 5 points, for 20 points total. Prepare visible evidence for all four; do not compensate for a missing required integration or submission item by claiming a strong judging score.

The [event Resources](https://get-hired-hack-nyc.devpost.com/resources) require all three Prism controls in addition to trace visibility. The [Nicrron sponsor guide](https://docs.google.com/document/d/1W0XuREG2ElwFoJaJXowSM60A390iHthG/edit) presents API, Builder and Code as alternative build paths; this project selects the API. Arena is optional model exploration, not proof of runtime integration.

The [Rules](https://get-hired-hack-nyc.devpost.com/rules) allow teams of 1 to 4, one team/project/track per participant, libraries/templates and AI coding tools. Product decisions remain the team's. Submissions and the required video are due October 10 at 4:30 PM ET; demos run 4:30 to 6:00 PM ET. Late submissions are not judged. Submission permits sharing the project/profile with participating hiring companies. The public [Discussions](https://get-hired-hack-nyc.devpost.com/forum_topics) and [Updates](https://get-hired-hack-nyc.devpost.com/updates) were checked on October 10 and contained no topics or announcements at that check.

## User journey

1. Open the app and load the synthetic sample or paste a new student profile and draft essay.

2. Select “Build college list.” The configured Prism input Guardrail runs first. On a pass, Nicrron extracts facts and exact supporting excerpts. A block or unavailable check produces a clear input-review state.

3. Review the extracted facts. Correct any error or missing academic field and continue.

4. The application retrieves comparable applicants, computes provisional categories, queries Prism's Knowledge Base for supporting records and asks Nicrron to explain the evidence. It validates claims locally and attaches the configured Prism Evaluator to the classified output.

5. Inspect the list. Each card shows its category or review state, outcome counts and main limitation. Pending or failed verification is visible; a pending Evaluator is never displayed as passed.

6. Select “Review evidence.” See the nearest admitted case and nearest rejected or waitlisted case from the retrieved cohort, when present, alongside all retrieved records.

7. Correct one student fact and select “Update list.” Recompute results and highlight changed categories, evidence cohorts and reasons.

8. Open the technical evidence view when demonstrating the sponsors: inspect the matching Guardrail result, Knowledge Base citation, Evaluator verdict and Nicrron traces. An advising-note export is optional after all release gates pass.

The app must not invent an opposite-outcome example when the retrieved cohort contains none. Show “No such outcome in the retrieved cases.” Differences between applicants describe observations, not causes of admissions decisions.

## Minimum interface

Use one usable Python standard-library HTTP server with a plain HTML interface application with an input step and a results step. This keeps the two-hour build focused on behavior.

| Surface | Required content and actions |
| --- | --- |
| Input | Profile and essay fields, synthetic sample button, Build college list |
| Profile review | Editable GPA, scale, rigor, major and supported tags; exact excerpts; fixed context; Continue |
| List | Six college cards grouped by provisional category plus Needs review; counts and short reasons |
| Evidence | Source records and IDs, academic differences, activity/essay excerpts, recorded outcomes, KB-backed reference |
| Review actions | Edit profile, Update list and a short change summary |
| List check | Explicit message when evidence cannot support likely options; never force categories |
| Technical view | Run/revision/model IDs; Guardrail, KB, Evaluator and trace evidence; separate from the counselor's main workflow |

Visible disclosure: “Synthetic demonstration data. Categories are provisional and are not validated admission predictions.” Labels use text as well as color. A Likely label is never presented as a guarantee.

## Agent and application responsibilities

Implement one bounded workflow: guard input, extract profile, review facts, retrieve cases, classify, query Knowledge Base, Council explanation/review/synthesis, validate, evaluate and return. Use explicit application functions. Council orchestration is now authorized; a separate agent framework is unnecessary. Use actual Prism interfaces verified against its live OpenAPI contract or installed SDK.

### LLM Council amendment, version council_v1

Implement the three-stage pattern inspired by https://github.com/karpathy/llm-council as native CaseList functions rather than replacing the app with the upstream chat UI. Two explicitly named, live-tested models are council members: `anthropic/claude-haiku-4-5` and `openai/gpt-4o-mini`, both called only through `https://api.nicrron.ai/v1`. Independent evidence explanations run concurrently. In stage two, the same members review and rank anonymously labeled proposals against the canonical packet. In stage three, a chairman synthesizes an explanation; preserve disagreements, limitations and source citations. Record model identities after anonymized review and show opinions, rankings, synthesis and actual trace IDs in an inspectable Council view.

The Council must not assign or override categories, create admissions probabilities, invent source facts, or count agreement as predictive validation. Application code computes categories and exact counts. Validate every final cited application/outcome/quote against the selected canonical records and every student quotation against the confirmed profile. If a required member or review fails, mark the Council incomplete and retain verified deterministic evidence instead of claiming consensus. One schema-repair attempt may be used within the overall deadline; preserve failed responses.

Nicrron extracts experiences and interests with exact supporting quotations; academic fields and curriculum/cycle/round remain counselor-confirmed. Human review is explicit before list generation. The complete automated workflow retains the 90-second budget, excluding human review. Council calls use bounded per-call timeouts and a verified 2,000-token cap. No calls occur on keystrokes. Record council_v1, prompt and configured/actual models with each run. Session and revision IDs connect extraction, Council and classified-output checks.

Prism's verified `POST /api/guardrails/evaluate` can run before direct Nicrron inference: require `evaluated: true` and honor `blocked: true`. An unavailable/no-verdict result fails closed. Keep the active CaseList custom-regex input rule and general injection rule visible; these are real Prism checks, not local keyword substitutes. Record their coverage limitations. KB upload/search uses the verified SDK contract; validate document ID, dataset version and the exact application block. Attach rubric_v2 to classified `policy/demo_v1` traces through a continuous evaluation task and read its per-trace score/verdict before acceptance. Pending or failed scores produce review, not a passed state.

| Responsibility | Owner |
| --- | --- |
| Check input for injected instructions and apply configured action | Prism Guardrail through a verified integration path |
| Extract quoted facts, activity tags and essay experiences | Nicrron model |
| Validate fields and preserve unknowns | Application |
| Filter/rank cases and assign demo categories | Application |
| Retrieve reference content grounding a displayed claim | Prism Knowledge Base; application verifies returned record/version |
| Explain supporting and conflicting evidence | Nicrron model |
| Reject unknown IDs, changed outcomes, wrong counts and fabricated quotes | Application |
| Check classified output against evidence and rubric | Attached Prism Evaluator |
| Correct facts and judge counseling usefulness | Counselor |
| Record model exchanges, control results and run identity | Prism plus a local evidence record |

Essay handling: extract stated experiences and interests with exact quotes and show how those experiences compare with a retrieved applicant. Every complete result includes at least one supported essay comparison, or explicitly states that the essay offers no comparable evidence. Do not score prose quality, infer personality/protected traits or claim admission causality. Essay text cannot provide instructions to the agent; changing a draft's wording alone must not manufacture a higher category.

## Synthetic data contract

Use six named colleges with separately sourced official program information, 60 authored synthetic applicants and 140 scenario application records. Use a fixed seed and manually designed edge cases. Separate applicant identity from application outcome so one applicant can have several college applications without being counted twice within a college.

Student and applicant fields: applicant_id, GPA value, GPA scale, curriculum context, course-rigor level, intended-major group, activity tags and descriptions, essay text and evidence excerpts.

Application fields: application_id, applicant_id, college_id, cycle, application round and outcome. Outcomes are admitted, rejected or waitlisted. The demo uses one fixed cycle, regular decision and one documented curriculum context.

College fields: college_id, real institution name, official program-reference URL, checked date, and explicit synthetic-outcome scope. Do not fabricate real college statistics.

Version the dataset and policy. Include a small separate expected-results file for hand-authored tests. Outcomes must be fixed before running the app; do not modify them during a demo to obtain a desired recommendation. Synthetic fixture success demonstrates software behavior, not calibration on real students.

Upload a small versioned reference set from these same fixtures to Prism's Knowledge Base. Preserve the mapping from application/applicant IDs to KB document IDs and dataset version. A selected evidence record can ground a claim such as “Applicant A017 was rejected by C02.” The displayed claim must use the actual KB query response, checked against the canonical fixture. Local JSON alone does not satisfy the Knowledge Base requirement. Do not infer full cohort counts from a partial KB retrieval.

## Comparison rules

Limit the demo to unweighted GPA on a 4.0 scale. An unsupported scale requests a compatible value instead of silently converting it. A missing GPA, course-rigor level or intended major blocks category generation until corrected.

Use the same GPA convention, curriculum context, cycle, application round and major group as comparison eligibility filters. Do not filter on admission outcome. Deduplicate by applicant within each college.

Rank eligible applicants using this transparent demo similarity score:

- GPA proximity contributes 50 percent: max(0, 1 minus absolute GPA difference).

- Course-rigor proximity contributes 30 percent: 1 minus the absolute level difference divided by 2. Levels 0, 1 and 2 mean standard, some advanced and extensive advanced coursework within the same documented curriculum context.

- Activity-tag Jaccard overlap contributes 20 percent. An empty tag union contributes zero and is shown as missing comparison evidence.

Retrieve the top eight scoring at least 0.65, using applicant ID to break ties. Activity tags must be supported by profile excerpts. These weights and thresholds are demo configuration, not validated admissions factors. Course-rigor levels are visible and counselor-correctable; missing levels remain unknown.

Display actual GPA and course-rigor differences, not just the aggregate score. Essay evidence informs the explanation but does not silently change this ranking.

## Provisional category policy

Store policy version demo_v1 in configuration and apply it in code. Apply the review checks first.

| Condition | Result |
| --- | --- |
| Required academic or major fields missing, incompatible scale or unsupported major group | Needs clarification or a named unsupported-input state |
| Fewer than eight eligible retrieved cases above threshold | Needs review due to sparse comparisons |
| Eight cases, with admitted count A and unresolved waitlisted count W | Evaluate the complete range from A to A plus W; do not count a waitlist as a rejection |
| A plus W is at most 2 | Provisional Reach, with unresolved outcomes disclosed |
| A is at least 3 and A plus W is at most 5 | Provisional Target, with unresolved outcomes disclosed |
| W is zero, A is 6 to 8, and student GPA and rigor are each at least the admitted-case median | Provisional Likely |
| A is 6 to 8 but an academic comparison gate fails | Needs review due to a material mismatch |
| All remaining combinations | Needs review because unresolved outcomes can change the category or prevent a Likely assessment |

These are explicit heuristic bands for a synthetic demonstration. The sample size and counts alone do not establish personal admission likelihood. The academic gate and review conditions prevent a favorable cohort count from automatically producing Likely. Do not display percentage chances, confidence percentages or invented institutional cutoffs. NERD APPLY has not endorsed these thresholds. The demonstration can establish traceability, policy consistency and usable review; real recommendation quality remains unvalidated.

Every category retains the retrieved IDs, counts, policy version and relevant comparison differences. The model can explain the assigned category but cannot change it. Never add artificial likely colleges merely to balance the list. No supported likely option is a review finding, not proof that the student lacks real-world options.

## Explanation and uncertainty contract

For each college, return a short explanation containing: evidence IDs, one grounded comparison, recorded outcome counts rendered by code, material differences and one limitation. Preserve facts separately from interpretation.

Where available, show one admitted and one non-admitted retrieved case with similar profiles. Explain that differing outcomes limit what a comparison can establish. Do not claim that a specific activity or essay caused acceptance.

Validation rejects unknown college or applicant IDs, outcome mismatches, fabricated quotations and categories that differ from the computed result. Check that cited fields and exact quotations match the referenced record; numerical claims are rendered from code. These checks do not certify every free-text inference. Keep generated language brief and visible beside the evidence.

On validation failure, retry once with the specific errors. If it still fails, display the verified structured evidence and a deterministic explanation marked “Generated explanation unavailable.” Preserve the failed response in the technical record.

If Nicrron fails before extraction, preserve input and show retry. If the input Guardrail is unavailable, stop before inference. If KB retrieval fails or contradicts the fixture, withhold that claim and mark evidence verification incomplete. If the Evaluator is pending, unavailable or fails, keep the classification in a visible review state and retain its reasons. These mandatory checks cannot silently fall back to local substitutes. A trace-ingestion-only failure may preserve already verified structured results, but must show delivery failure and fails the sponsor release gate. Recorded playback is labeled and never counted as a new live pass.

## Sponsor integration and technical design

Default stack: Python, Python standard-library HTTP server with a plain HTML interface, OpenAI-compatible client, Pydantic, local JSON fixtures and pytest for core checks, plus sponsor-verified Prism interfaces. The event recommends prismtrace-sdk>=0.5.1; pin the version that passes the smoke test. Use explicit submit buttons, session state, input hash, profile revision and run ID. No custom database or vector infrastructure is required; Prism's Knowledge Base is mandatory.

The sponsor guide specifies Nicrron's OpenAI-compatible endpoint, https://api.nicrron.ai/v1. Use NICRRON_API_KEY and an accessible model verified in the account; do not treat illustrative model IDs in docs as proof of availability. The live journey uses one extraction call, two independent Council opinions, two anonymous reviews and one chairman call; extraction/chairman may each have one schema repair. Test structured-output support and record the actual model. The guide offers COLUMBIA26 for $250 credit plus the standard $10 signup credit, shared across API/Builder/Code. Existing-account balances must be checked rather than assumed. Arena is optional.

Prism integration has four required parts: input Guardrail, output Evaluator, Knowledge Base grounding and trace visibility. The event instructions specify one organization/workspace per team, project named after the team and agent_name on every SDK call. Use a custom key with ingest/read access, or the onboarding key described by the event; confirm any additional operation scopes with Prism. The event coupon PROOFOFWORK offers Builder access, 200 credits and five seats for 30 days. No account configuration is assumed completed.

The public [Prism docs](https://blockconvey.com/docs) describe HTTP tracing and proxy enforcement. Authenticated service OpenAPI and the SDK established the direct pre-inference Guardrail and KB/Evaluator operations; verified contracts are recorded in docs/PRISM_SETUP.md. Trace ingestion is not a replacement for those controls. Maintain the exercised contract for each required operation, including result retrieval, error shape and latency. Do not invent SDK methods or route inference away from Nicrron merely to make tracing work.

Proposed input policy: block an essay instruction that asks the system to ignore evidence or assign “Likely” universally; allow an ordinary essay. Apply the verified result before inference. If the available integration only flags after the call, disclose that limitation and resolve the prevention path with Prism before implementing this specification.

Proposed output rubric: check that category matches the saved policy, cited IDs/outcomes/quotes match provided evidence, sparse data causes review, and no guarantee or unsupported admission probability is stated. Attach this Evaluator to classified college output, retaining its configuration, input references, verdict and reasons. Exercise a known-correct output and a deliberately altered “Likely” output on sparse evidence. An Evaluator is an additional check, not proof of admissions accuracy.

For grounding, query uploaded synthetic reference records and show at least one claim with its returned KB document and excerpt. Use IDs/version checks to prevent a plausible answer about the wrong applicant. Keep deterministic local ranking independent of incomplete KB search results.

Preserve the shared session, run/revision IDs and agent_name across the journey. Save trace IDs, Guardrail result, KB query/evidence and Evaluator verdict. If an operation returns no stable ID, save its response and configuration reference without fabricating one.

Configure NICRRON_API_KEY, NICRRON_MODEL, PRISMTRACE_HOST, PRISMTRACE_PROJECT_ID and PRISMTRACE_API_KEY server-side. Add the actual Guardrail, KB and Evaluator configuration identifiers only after confirming their interfaces. Commit .env.example with names only; never expose secrets in source, responses, telemetry or recording.

First integration proof is the complete minute-20 sponsor journey, not merely an ingested trace. Before implementation, ask the owners for:

- Nicrron: one accessible low-latency model, a working JSON example, supported response limit and confirmation of credit access.

- Prism: the smallest working Nicrron-compatible input Guardrail, KB upload/query and classified-output Evaluator example, with agent_name and readback.

- Both: whether Prism's proxy supports Nicrron upstream, or what supported alternative enforces the input check while retaining Nicrron inference.

These preflight dependencies were resolved for the current workspace; the delivery record distinguishes actual live proofs from release requirements still pending.

Use a 25-second timeout per model attempt, at most one transient retry and one schema-repair attempt per logical model call. Bound the complete automated run to 90 seconds, including Guardrail, KB and Evaluator checks; human review time is excluded. If a sponsor check is asynchronous, display pending and use a supported bounded polling/readback path. Do not assume evaluation is immediate; Cancel and preserve the input when the deadline expires. Budget up to 5 seconds for each Prism ingest attempt. This release marks an ingest failure incomplete without automatically retrying; an explicit retry starts a new run. These are implementation limits, not promised response times. Cap input at 12,000 characters. Send only structured comparison facts and up to two relevant source excerpts of at most 250 characters per retrieved applicant; never include full historical essays. Start with a 2,000-token response cap and verify it on the chosen model, including any reasoning-token accounting. A response that stops because of the cap is incomplete and must not be accepted. Configure a tested response cap using the selected model’s verified supported parameter. Measure actual latency.

## Acceptance checks

| Check | Pass condition |
| --- | --- |
| Complete profile | Known fixture produces expected comparable cases and provisional categories |
| Unseen supported profile | A profile outside the rehearsed demo is parsed and processed without hardcoded identity or outcome |
| Unsupported or incomplete profile | Missing GPA/major/rigor, incompatible scale or major produces a named limitation; no invented conversion |
| Sparse and conflicting evidence | Correct counts, review conditions and admitted/non-admitted records |
| Essay use | Exact experience comparison or explicit lack of comparable essay evidence; no inferred character or admission cause |
| Unsupported generated claim | Unknown ID, altered outcome or fabricated quote is rejected |
| Counselor correction | Recomputes evidence/categories and clears stale verification |
| Guardrail positive/negative tests | Benign essay passes; injected instruction triggers the configured action before inference, with real Prism evidence |
| Knowledge Base grounding | A displayed claim is supported by a real KB response and correct record/version; missing or mismatched evidence is withheld |
| Evaluator positive/negative tests | Known-correct classification passes; deliberately wrong category or unsupported certainty is flagged with reasons |
| Live sponsor journey | Nicrron responses and all required Prism control results are inspectable under the correct project/agent/run |
| Failure behavior | Timeout or unavailable mandatory check is visible and never shown as passed |
| Usability | An unfamiliar reviewer can load, inspect evidence and update one fact without instruction |
| Submission | All eight fields are complete; repository and video open without owner credentials |

Keep hand-authored expectations independent of the implementation. Freeze the demo fixtures before testing, then test at least one unseen supported profile and one unsupported/missing-data profile. Judges may supply real-world cases; a supported case must run normally and an unsupported case must state its boundary. Fixture success, evaluator agreement and synthetically favorable outcomes do not establish real admissions accuracy.

## Judging plan

| Criterion | What the judge sees |
| --- | --- |
| Technical Execution 5 | Live profile-to-list execution, correct fixture counts, tested comparison rules and a working correction |
| Trust and Explainability 5 | Exact source records, conflicting outcomes, concrete review reasons and honest synthetic-data labeling |
| Design 5 | A readable advising workflow with clear next actions and technical details in a separate view |
| Uniqueness of Idea 5 | Comparable applicants with different outcomes shown together, followed by a correction that updates the list and reveals what changed |

Do not spend build time on unsupported claims of uniqueness, model leaderboards or decorative dashboards. Demonstrate the specific interaction.

## Two hour implementation plan

| Elapsed minutes | Deliverable |
| --- | --- |
| 0 to 5 | Blocker triage, account access and sponsor questions; identify submission owner |
| 5 to 20 | Smallest live Guardrail → Nicrron → KB-grounded claim → evaluated classification journey; trace/readback evidence |
| 20 to 40 | Fixed fixtures, eligibility/ranking/category functions and independent expected cases |
| 40 to 70 | Single Python standard-library HTTP server with a plain HTML interface workflow, evidence display, extraction review, correction and integration checks |
| 70 to 95 | Unseen inputs, positive/negative control tests, failures, usability and clean-start verification |
| 95 to 120 | Feature freeze; README, accessible repository, video recording/upload, all eight Devpost fields and delivery record |

If delayed, cut styling, Arena comparison, advising-note export and extra review controls. Preserve list generation, source evidence, uncertainty, one correction and every mandatory sponsor capability. The two-hour target depends on readily available sponsor APIs, working credentials and prompt help; it cannot be guaranteed before preflight. Record actual start, minute-20 checkpoint and finish target, keeping preparation and authorized submission before 4:30 PM ET. Keep the final 25 minutes for delivery. An unresolved mandatory integration is reported as blocked, never simulated.

Excluded: accounts, PDF/OCR ingestion, payments, web crawling, real admissions predictions, essay grading, financial-aid modeling, an autonomous scenario explorer, model training and custom vector databases. Council explanation review is the only newly authorized model orchestration.

## Demo and submission

## Canonical demo case

Lock one named synthetic student and one editable correction before UI work. Baseline: Avery Chen, unweighted GPA 3.70 on a 4.0 scale, the supported Computer Science major group, rigor level 1 and quoted activities and essay experiences. Correction: the counselor confirms rigor level 2 from additional coursework information. Record that correction as counselor-supplied evidence, not a quotation from the original input.

The following is an illustrative acceptance fixture to construct and verify before demonstration. College IDs are proposed fixture identifiers, not existing records.

| College | Baseline retrieved evidence | Expected baseline | Expected after correction |
| --- | --- | --- | --- |
| C01 | Eight eligible cases, one admitted and seven rejected | Reach | Reach |
| C02 | Eight cases, four admitted and four rejected | Target | Target |
| C03 | Eight cases, seven admitted and one rejected; GPA median check passes but admitted rigor median is 2 | Needs review due to rigor mismatch | Likely, if the same cohort remains eligible and both academic checks pass |
| C04 | Eight cases, six admitted and two rejected; both academic checks pass | Likely | Likely |
| C05 | Four eligible cases | Needs review due to sparse evidence | Needs review |
| C06 | Eight cases, two admitted, five rejected and one unresolved waitlist | Needs review because resolution can cross the Reach to Target boundary | Needs review |

Construct fixture features so these cohort and median expectations can be checked independently. If the policy yields different results, diagnose and revise the fixture or policy transparently before freezing the demo; never override application output for the presentation. Keep additional edge-case tests separate. This scenario proves mechanics under the stated policy, not admissions validity.

The success condition is a complete list with a visible disagreement, a specific unresolved case and a justified update after correction. Do not require every edit to change a category; changed evidence with an unchanged category is also a valid result.

Record a focused demo of approximately three minutes, adjusted if organizers specify a limit. Reuse an honestly labeled captured live run to avoid dead time, but also be ready to run the controls live for judges:

1. Load the synthetic student with grades, activities and an essay.

2. Generate the list and inspect a Target card with similar applicants who had different outcomes.

3. Open the sparse-evidence college and its Needs review explanation.

4. Correct course rigor and regenerate. Show the changed cases and any changed category without claiming a causal admission effect.

5. Show the actual Prism Knowledge Base reference and attached Evaluator verdict for the result; open the corresponding Nicrron traces. Run the injected-essay case and show its Guardrail outcome, then the deliberately wrong classification and its failed evaluation. Clearly distinguish test cases from the ordinary student journey.

Devpost project name: CaseList.
One-line description: A counselor copilot that builds a provisional college list and shows the past applicant outcomes that support or challenge each recommendation.
Track: NERD APPLY — The Counselor Copilot.

Submission must contain:

- What was built and why: student intake, outcome-based comparisons, generated categories and counselor review.

- Accuracy and uncertainty: deterministic checks, cited cases, abstention conditions and synthetic-data limits.

- Tools: NicrronNinoo through Nicrron, Block Convey Prism, Python, Python standard-library HTTP server with a plain HTML interface and supporting libraries.

- Team names and actual roles. Sumit Shekhar’s and any teammates’ contributions must reflect the work completed.

- A working video demo link.

- An accessible GitHub repository containing source, fixtures, policy, tests, README and .env.example.

- Run instructions, known limitations, measured check results and the policy version.

Do not claim unrun tests, completed integrations or team contributions before they exist. The two-hour definition of done requires all three release gates: a working prototype with both sponsors, all eight verified Devpost submission items, and visible evidence for each of the four judging criteria. Report submission ready separately from submitted. Local implementation is authorized. Public submission requires the user's subsequent authorization.

## Build demo and maintenance record

This Page and the workspace SPEC.md anchor implementation. Save this corrected version to SPEC.md before writing application code. The submitted commit and archived SPEC.md define what was built; later Page edits must be reconciled explicitly. Record the specification version and commit together. No feature, threshold or provider change is silent.

Maintain one compact delivery record in the repository. For each release gate, record owner, status, evidence path or URL, observed result and timestamp. A pending check stays pending. Record scope changes with reason and effect on the demo. Credentials never appear in this record.

| Phase | Anchors to preserve |
| --- | --- |
| Build | SPEC.md, decision policy, data schema, fixture version and hand-authored expected results |
| Demo | Named input and correction, expected outcomes, observed output, actual model ID, Prism session and trace IDs, Guardrail evidence, KB documents/query, Evaluator configuration and verdict, source commit and video |
| Handoff | README with clean-start commands, pinned working dependencies, .env.example, check results, known limitations and all eight Devpost fields |
| After the event | Tagged submitted version, reusable fixtures, recorded integration contracts, unresolved assumptions and next-validation plan |

The post-event goal is to determine whether a counselor finds the explanations and review actions useful. Conduct counselor review before claiming recommendation quality. A later real-data evaluation needs permitted historical records, documented outcome completeness, time-separated evaluation and checks for cohort bias; matching applicants and describing differences do not establish causality.

A replayable engineering result consists of the saved input, data and policy versions, model configuration and captured response. Model wording may change across new live calls; preserve the recorded run for exact historical inspection. Any offline playback must say “Recorded run” and never count as a fresh sponsor-integration pass.

Rerun core checks when the policy, fixtures, prompt, model or integration contract changes. Preserve the submitted version rather than silently replacing its demo or claims. Extending the product to real students, additional majors, GPA conventions or financial constraints is a new scoped release.



## Archived initial local handoff status October 10 2026

The user requested an immediate VS Code handoff around 12:23 PM ET. The local starter is implemented and six core tests pass. Package installation was blocked, so the interface uses no third-party dependencies. Sponsor credentials are absent and all live integration gates remain pending. The application labels its current behavior as local comparison preview. This local version 1.2 supersedes the Page version 1.1 for these implementation details. Start with README.md; the remaining integration contracts are recorded in docs/PRISM_SETUP.md. No submission, video or public repository exists yet.


## Council release verification October 10 2026

The implemented council_v1 is inspired by Karpathy’s three-stage Council; it is not an installation of the original OpenRouter app. All inference goes through Nicrron. Two independent opinions, two anonymous reviews, a Haiku chairman and at most one repair are recorded. Extraction is separately reviewed by the counselor. Code controls categories and validates exact application/outcome/essay references. Chairman prose is restricted to quoted essay experiences; academic policy reasons remain separate.

PRISM input evaluation runs before inference and fails closed. The default injection detector missed the required attack example, so an additional actual PRISM custom_regex block rule covers the demonstrated evidence-override phrases. This is narrow demonstrated coverage, not a general proof against prompt injection. Six synthetic reference documents were uploaded and their returned application blocks verified.

The attached Evaluator checks the compact classified output: all six IDs, category/count consistency, sparse-data abstention, waitlists and canonical citation references. The full essay prose is source-validated locally and reviewed by the Council; it is not included in the bounded classified-output evaluator payload. Shared quotation references prevent PRISM context truncation. The evaluator establishes fixture consistency only, never real admissions validity.

Verified baseline: Reach, Target, Needs review, Likely, Needs review, Needs review. Verified rigor-2 correction: Harbor becomes Likely. Positive classified output PASS 95; wrong four-case Likely output FAIL 15; injected instructions blocked before Nicrron. Eleven tests cover deterministic policy and key failure controls. Each run has session/revision/input hash and model-stage trace IDs. A recorded playback is explicitly labeled historical and does not perform fresh checks.

The app runs locally on 127.0.0.1:8765. The CaseList Devpost project overview and story are saved as a draft. This release does not claim public hosting, a submitted Devpost entry, or confirmed judge access to the private repository/video.

## Version 1.4 — credible synthetic demonstration

The user confirmed no organizer applicant dataset exists and authorized created synthetic data. synthetic_v2 preserves the demo_v1 policy fixtures so the examples remain inspectable, while replacing repeated applicant text with unique essays, activities, named scenario students and coursework consistent with rigor. Each outcome remains an authored fixture, not a reported decision by the named institution. Do not use fixture counts to describe real institutional admission rates or selectivity.

The UI shows an admitted scenario beside a rejected or waitlisted scenario, academic differences, shared tags and coursework. Retrieval weights are visible; essay meaning is reviewed separately by Council. Names do not enter matching. Official university program facts have separate links and verification dates. PRISM must query new versioned documents; old recorded passes cannot certify this release.

Original track requirement: reasoning grounded in real outcomes. Without permissioned historical outcomes, this prototype demonstrates the workflow using synthetic outcomes and does not satisfy empirical validation of that requirement. Obtaining and validating a permissioned outcome dataset remains the production step.

### Visible student context

A Student being reviewed card sits above the results on initial load, extraction and comparison views. It shows name, unweighted GPA, readable rigor level, major, activities, full draft essay and confirmed matching tags. Editing the profile updates the card immediately while invalidating stale results. Synthetic comparison students use independently shuffled first-name and surname lists with a fixed random seed; display labels never affect matching, quotations or outcome classifications.

UI terminology: distinguish a first-year college applicant from a current college student. Label GPA and coursework as high-school preparation, use descriptive coursework options without numeric codes, and explain advanced-course examples. Do not invent transcript courses or school opportunities. Policy values remain 0/1/2 internally.
