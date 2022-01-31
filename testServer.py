from http.server import BaseHTTPRequestHandler, HTTPServer

port = 1111
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        h = open("studyingHTTP.html", "rb")
        self.wfile.write(h.read())

httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
print(f'Server running on port:{port}')
httpd.serve_forever()

# def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
#     server_address = ('', port)
#     httpd = server_class(server_address, handler_class)
#     httpd.serve_forever()