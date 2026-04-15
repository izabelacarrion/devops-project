import os
import json
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = "1.0.0"
HOSTNAME = socket.gethostname()


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, payload, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_GET(self):
        if self.path == "/health":
            self._send_json({"status": "ok"})

        elif self.path == "/ready":
            self._send_json({"ready": True})

        elif self.path == "/info":
            self._send_json({
                "status": "ok",
                "version": APP_VERSION,
                "environment": APP_ENV,
                "hostname": HOSTNAME
            })

        else:
            self._send_json({"error": "not found"}, 404)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    server.serve_forever()