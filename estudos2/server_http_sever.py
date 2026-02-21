from http.server import BaseHTTPRequestHandler, HTTPServer


class MeuHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello Renato!")


server = HTTPServer(("localhost", 8000), MeuHandler)
print("Rodando em http://localhost:8000")

server.serve_forever()
