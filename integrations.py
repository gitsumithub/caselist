"""Verified wire contracts only. Mandatory Prism controls remain explicitly blocked."""
import json
import os
import ssl
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
    configured = bool(os.getenv('PRISMTRACE_API_KEY') and os.getenv('NICRRON_API_KEY'))
    return [{'name': name, 'status': 'Configured; verified per run' if configured else 'Needs credentials',
        'detail': 'Inspect this run’s evidence panel for actual checks and verdicts.'}
        for name in ('Nicrron Council', 'Prism traces', 'Input Guardrail', 'Knowledge Base', 'Output Evaluator')]



def _post(url, payload, headers, timeout):
    body = json.dumps(payload, allow_nan=False).encode()
    request = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json", **headers}, method="POST")
    context = ssl.create_default_context()
    # Some macOS Python distributions omit the system CA bundle.
    # Add trusted system certificates while retaining TLS verification.
    system_ca = Path('/etc/ssl/cert.pem')
    if system_ca.is_file():
        context.load_verify_locations(cafile=str(system_ca))
    with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
        return json.load(response)


def nicrron_chat(messages, model=None, timeout=25, json_output=False):
    load_env()
    key, model = os.getenv("NICRRON_API_KEY"), model or os.getenv("NICRRON_MODEL")
    if not key or not model:
        raise RuntimeError("Configure NICRRON_API_KEY and an accessible NICRRON_MODEL in .env.")
    started = time.monotonic()
    payload = {"model": model, "messages": messages, "max_tokens": 2000, "temperature": 0}
    if json_output:
        payload['response_format'] = {'type': 'json_object'}
    response = _post("https://api.nicrron.ai/v1/chat/completions", payload, {"Authorization": f"Bearer {key}"}, timeout)
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
    if host not in ("https://prism.blockconvey.com", "https://prism-api-prod.up.railway.app"):
        raise RuntimeError("Only the verified official Prism host is configured in this starter.")
    return _post(host + "/api/traces", {
        "trace_id": str(uuid4()), "project_id": project, "session_id": session_id,
        "agent_name": os.getenv("PRISM_AGENT_NAME", "caselist"), "agent_id": "caselist",
        "model": reply["model"], "input_messages": messages, "output_message": reply["content"],
        "latency_ms": reply["latency_ms"], "metadata": {"purpose": "connectivity_smoke_test", "not_full_release_gate": True}
    }, {"X-PRISMtrace-Key": key}, 5)


def prism_handshake():
    """Use the exact setup-doctor contract supplied by Prism onboarding."""
    load_env()
    key, project = os.getenv("PRISMTRACE_API_KEY"), os.getenv("PRISMTRACE_PROJECT_ID")
    if not key or not project:
        raise RuntimeError("Set PRISMTRACE_API_KEY and PRISMTRACE_PROJECT_ID in the local .env first.")
    response = _post(
        "https://prism-api-prod.up.railway.app/api/setup-doctor/handshake",
        {"project_id": project, "send_test_trace": True},
        {"X-PRISMtrace-Key": key}, 15)
    # Do not display an echoed credential even if the server returns one.
    return json.loads(json.dumps(response).replace(key, "[REDACTED]"))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", help="Send a harmless fixed connectivity request to Nicrron and trace it in Prism.")
    parser.add_argument("--prism-handshake", action="store_true", help="Verify Prism onboarding credentials and send its synthetic setup trace.")
    args = parser.parse_args()
    if args.prism_handshake:
        print(json.dumps(prism_handshake(), indent=2))
    elif args.smoke:
        messages = [{"role": "user", "content": "Reply with the single word connected."}]
        reply = nicrron_chat(messages)
        trace = prism_trace(messages, reply, "caselist-smoke-" + str(uuid4()))
        print(json.dumps({"model": reply["model"], "latency_ms": reply["latency_ms"], "trace_id": trace.get("id"), "full_gate_passed": False}))
    else:
        print(json.dumps(readiness(), indent=2))
