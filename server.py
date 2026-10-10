"""Local-only CaseList development server. Live workflow uses configured sponsor credentials."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from uuid import uuid4
import argparse
import hashlib
import json
import math
from core import build_list
from integrations import readiness
from live import submit, get_job, cancel

ROOT = Path(__file__).parent
DATASET = json.loads((ROOT / "data/dataset.json").read_text())
SAMPLE = json.loads((ROOT / "data/sample.json").read_text())


class Handler(BaseHTTPRequestHandler):
    def send_json(self, value, status=200):
        content = json.dumps(value, allow_nan=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        if self.path.startswith('/api/jobs/'):
            job = get_job(self.path.rsplit('/', 1)[-1])
            return self.send_json(job or {'error': 'Unknown run'}, 200 if job else 404)
        if self.path == "/api/demo":
            return self.send_json(json.loads((ROOT / "data/demo_runs.json").read_text()))
        if self.path == "/health":
            return self.send_json({"ok": True, "mode": "local_and_live_council", "live_sponsors_verified": False})
        if self.path == "/api/state":
            return self.send_json({"sample": SAMPLE, "integrations": readiness(), "dataset": {"version": DATASET["version"], "applicants": len(DATASET["applicants"]), "applications": len(DATASET["applications"]), "colleges": len(DATASET["colleges"])}})
        if self.path in ("/", "/index.html"):
            content = (ROOT / "static/index.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            return self.wfile.write(content)
        self.send_json({"error": "Not found"}, 404)

    def do_POST(self):
        origin = self.headers.get("Origin")
        host = self.headers.get("Host")
        if origin and origin != f"http://{host}":
            return self.send_json({"error": "Use the local app origin."}, 403)
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 64000:
                return self.send_json({"error": "Request must be between 1 and 64,000 bytes."}, 413)
            payload = json.loads(self.rfile.read(length), parse_constant=lambda v: (_ for _ in ()).throw(ValueError("Non-finite JSON")))
            if not isinstance(payload, dict):
                raise ValueError("Expected a profile object.")
            if self.path == '/api/cancel':
                cancel(str(payload.get('job_id', '')))
                return self.send_json({'cancelled': True})
            if self.path in ('/api/extract', '/api/live'):
                profile = payload.get('profile')
                if not isinstance(profile, dict):
                    return self.send_json({'error': 'Provide a profile object.'}, 400)
                revision = payload.get('revision', 1)
                if type(revision) is not int or not 1 <= revision <= 10000:
                    return self.send_json({'error': 'Invalid profile revision.'}, 400)
                session_id = payload.get('session_id')
                if session_id is not None and (not isinstance(session_id, str) or len(session_id) > 100):
                    return self.send_json({'error': 'Invalid session ID.'}, 400)
                job = submit('extract' if self.path == '/api/extract' else 'generate', profile, DATASET,
                    extraction_id=payload.get('extraction_id'), session_id=session_id, revision=revision)
                return self.send_json(job, 202)
            if self.path != "/api/compare":
                return self.send_json({"error": "Not found"}, 404)
            result = build_list(payload, DATASET)
            result.update(run_id=str(uuid4()), input_hash=hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest(),
                          mode="local_comparison", live_sponsors_verified=False)
            self.send_json(result, 422 if result["errors"] else 200)
        except (ValueError, TypeError, KeyError, OverflowError):
            self.send_json({"error": "Invalid profile. Check field types and numeric values."}, 400)

    def log_message(self, fmt, *args):
        # Log paths/status only; never profile contents or secrets.
        print(fmt % args, flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    print(f"CaseList: http://127.0.0.1:{args.port} (local app with live Nicrron Council and Prism checks)", flush=True)
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
