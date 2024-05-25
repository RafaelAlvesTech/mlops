from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_params = urllib.parse.urlparse(self.path).query
        query_dict = urllib.parse.parse_qs(query_params)
        auth_code = query_dict.get('code', [''])[0]

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Received Authorization Code!</h1></body></html>")

        print(f"Received Authorization Code: {auth_code}")

if __name__ == '__main__':
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Running server on {server_address[0]}:{server_address[1]}")
    httpd.serve_forever()