from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        path = os.path.join(os.getcwd(), 'public')
        if not os.path.exists(path):
            path = os.getcwd()

        try:
            if self.path == '/':
                with open(os.path.join(path, 'index.html'), 'rb') as file:
                    self.wfile.write(file.read())
            else:
                with open(os.path.join(path, self.path[1:]), 'rb') as file:
                    self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)

    print("Starting web server on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()