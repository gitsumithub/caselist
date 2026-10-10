"""Verified wire contracts only. Mandatory Prism controls remain explicitly blocked."""
import json
import os
import time
import urllib.request
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).parent


def load_env():
    path = ROOT / ".env"
    if path.exists():
        for raw in path.read_text().splitlines():
            raw = raw.strip()
            if not raw or raw.startswith("#") or "=" not in raw:
                continue
            name, value = raw.split("=", 1)
            if name.strip().isidentifier():
                os.environ.setdefault(name.strip(), value.strip().strip("\"'"))


def readiness():
    load_env()
    return [
        {"name": "Nicrron inference", "status": "Configured, untested" if os.getenv("NICRRON_API_KEY") and os.getenv("NICRRON_MODEL") else "Needs key and model", "detail": "Extraction and explanation must use actual Nicrron responses."},
        {"name": "Prism traces", "status": "Configured, untested" if os.getenv("PRISMTRACE_API_KEY") and os.getenv("PRISMTRACE_PROJECT_ID") else "Needs key and project", "detail": "Verified HTTP contract implemented; live delivery has not been tested."},
        {"name": "Input Guardrail", "status": "Blocked", "detail": "Need sponsor-confirmed pre-inference check compatible with Nicrron."},
        {"name": "Knowledge Base", "status": "Blocked", "detail": "Upload-ready synthetic references exist. Actual upload and query contract need confirmation."},
        {"name": "Output Evaluator", "status": "Blocked", "detail": "Rubric is in docs/PRISM_SETUP.md. Attachment and verdict readback need confirmation."},
    ]


def _post(url, payload, headers, timeout):
    body = json.dumps(payload, allow_nan=False).encode()
    request = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json", **headers}, method="POST")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def nicrron_chat(messages):
    load_env()
    key, model = os.getenv("NICRRON_API_KEY"), os.getenv("NICRRON_MODEL")
    if not key or not model:
        raise RuntimeError("Configure NICRRON_API_KEY and an accessible NICRRON_MODEL in .env.")
    started = time.monotonic()
    response = _post("https://api.nicrron.ai/v1/chat/completions", {"model": model, "messages": messages}, {"Authorization": f"Bearer {key}"}, 25)
    choice = response.get("choices", [{}])[0]
    content = choice.get("message", {}).get("content")
    if choice.get("finish_reason") != "stop" or not isinstance(content, str) or not content.strip():
        raise RuntimeError("Nicrron response is incomplete or has no text content.")
    return {"content": content, "model": response.get("model", model), "latency_ms": round((time.monotonic() - started) * 1000), "usage": response.get("usage", {})}


def prism_trace(messages, reply, session_id):
    load_env()
    key, project = os.getenv("PRISMTRACE_API_KEY"), os.getenv("PRISMTRACE_PROJECT_ID")
    if not key or not project:
        raise RuntimeError("Configure Prism project and ingest/read key in .env.")
    # Fixed official destination protects credentials from accidental host misconfiguration.
    host = os.getenv("PRISMTRACE_HOST", "https://prism.blockconvey.com").rstrip("/")
    if host != "https://prism.blockconvey.com":
        raise RuntimeError("Only the verified official Prism host is configured in this starter.")
    return _post(host + "/api/traces", {
        "trace_id": str(uuid4()), "project_id": project, "session_id": session_id,
        "agent_name": os.getenv("PRISM_AGENT_NAME", "caselist"), "agent_id": "caselist",
        "model": reply["model"], "input_messages": messages, "output_message": reply["content"],
        "latency_ms": reply["latency_ms"], "metadata": {"purpose": "connectivity_smoke_test", "not_full_release_gate": True}
    }, {"X-PRISMtrace-Key": key}, 5)


def require_live_controls():
    # Intentionally no fake successful control result or guessed vendor endpoints.
    raise RuntimeError("Live student processing is blocked until Prism Guardrail, Knowledge Base and Evaluator contracts are connected and tested. Local comparison is available.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", help="Send a harmless fixed connectivity request to Nicrron and trace it in Prism.")
    args = parser.parse_args()
    if args.smoke:
        messages = [{"role": "user", "content": "Reply with the single word connected."}]
        reply = nicrron_chat(messages)
        trace = prism_trace(messages, reply, "caselist-smoke-" + str(uuid4()))
        print(json.dumps({"model": reply["model"], "latency_ms": reply["latency_ms"], "trace_id": trace.get("id"), "full_gate_passed": False}))
    else:
        print(json.dumps(readiness(), indent=2))
