from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/':
           self.path = '/templates/discord_html+css.html'
        else:
            self.path = '/index.html'

        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path[1: ]).read()
        except:
           f = "File not found"
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes(f, "utf-8"))

def main():
    port = 8000
    address = ''
    server_address = (address, port)
    http_server = HTTPServer((server_address), handler)
    print(f'Server running on {address} on port {port}...')
    http_server.serve_forever()

if __name__ == '__main__':
    main()