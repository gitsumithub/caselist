# Verified PRISM contracts

This replaces the initial pending-contract notes. Contracts were checked against the authenticated service OpenAPI and exercised on October 10, 2026.

- Host: `https://prism-api-prod.up.railway.app`, authenticated using `X-PRISMtrace-Key` from local `.env`.
- Input: `POST /api/guardrails/evaluate`; require `evaluated: true`; honor `blocked` before Nicrron inference. A custom_regex block rule augments the default detector for the demonstrated override phrases.
- KB: multipart `POST /api/knowledge-base/documents` and `POST /api/knowledge-base/search`. Validate returned document ID, synthetic_v1 name and exact application block. Configured IDs are in `data/prism_config.json`.
- Traces: `POST /api/traces`, always `agent_name=caselist` with session/run/revision and purpose metadata.
- Evaluator: create/update `/api/evaluators`, attach a task via `/api/eval-tasks`, filter `policy/demo_v1`, then run the matching user/run task and read persisted `/api/eval-results`. Accept only the matching trace/task/evaluator verdict at threshold 80.

The bounded evaluator payload checks classifications and canonical citation references. Full essay prose is source-validated locally and anonymously reviewed by the Council. Repeated synthetic essay language is a documented fixture limitation. Neither evaluator scores nor Council agreement validate admissions predictions.

Run `setup_prism.py` to reuse or provision the reference documents, custom Guardrail and classified-output evaluator. IDs are configuration, not credentials. Changing project requires a fresh project-specific configuration and live verification.

See `docs/DELIVERY_RECORD.md` for passing and deliberately failing trace IDs. Never replace a failed verdict with a local success label.
