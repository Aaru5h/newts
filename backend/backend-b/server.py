from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

BACKEND_ID = os.environ["BACKEND_ID"]
PORT = int(os.environ["PORT"])
ETAG = f'"phase1-backend-{BACKEND_ID}-v1"'

class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def send_json(self, status, data):
        body = json.dumps(data).encode()

        if self.headers.get("If-None-Match") == ETAG:
            self.send_response(304)
            self.send_header("ETag", ETAG)
            self.send_header("Cache-Control", "max-age=60")
            self.end_headers()
            return

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Backend", BACKEND_ID)
        self.send_header("Cache-Control", "max-age=60")
        self.send_header("ETag", ETAG)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.send_json(200, {
                "message": f"Backend {BACKEND_ID} is running"
            })
        elif self.path == "/api/status":
            self.send_json(200, {
                "backend": BACKEND_ID,
                "status": "ok"
            })
        else:
            self.send_json(404, {"error": "Not found"})

    def log_message(self, format, *args):
        print(f"[Backend {BACKEND_ID}] {format % args}")

print(f"Backend {BACKEND_ID} listening on port {PORT}")
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
