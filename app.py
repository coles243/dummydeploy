import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path in {"/", "/health"}:
			body = json.dumps({"status": "ok"}).encode()
			self.send_response(200)
			self.send_header("Content-Type", "application/json")
			self.send_header("Content-Length", str(len(body)))
			self.end_headers()
			self.wfile.write(body)
			return

		self.send_error(404, "Not Found")

	def log_message(self, format_string, *args):
		print(f"{self.client_address[0]} - {format_string % args}")


def main():
	port = int(os.environ.get("PORT", "8080"))
	server = ThreadingHTTPServer(("0.0.0.0", port), RequestHandler)
	print(f"Serving HTTP on port {port}")
	server.serve_forever()


if __name__ == "__main__":
	main()
