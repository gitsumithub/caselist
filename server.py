"""Local-only CaseList development server. Python standard library; no install."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from uuid import uuid4
import argparse
import hashlib
import json
import math
from core import build_list
from integrations import readiness, require_live_controls

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
        if self.path == "/health":
            return self.send_json({"ok": True, "mode": "local_comparison", "live_sponsors_verified": False})
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
            if self.path == "/api/live":
                try:
                    require_live_controls()
                except RuntimeError as error:
                    return self.send_json({"error": str(error)}, 503)
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
    print(f"CaseList: http://127.0.0.1:{args.port} (local comparison; live sponsor checks pending)", flush=True)
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
