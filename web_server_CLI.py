from http.server import HTTPServer, BaseHTTPRequestHandler
import os

def vatodo():
    global page
    print("")
    print('\x1b[6;30;42m' + "Choose an option. " + '\x1b[0m')
    print("")
    print("")
    print('\x1b[4;34;40m' + "1 - Templates" + '\x1b[0m')
    print("")
    print('\x1b[4;34;40m' + "2 - Import a file" + '\x1b[0m')
    print("")
    print('\x1b[4;31;40m' + "99 - Exit" + '\x1b[0m')
    print("")
    todo = input("")
    if todo == "1":
        print("")
        print('\x1b[6;31;43m' + "Choose a template. " + '\x1b[0m')
        print("")
        print("")
        print('\x1b[4;33;40m' + "1 - Discord" + '\x1b[0m')
        print("")
        print('\x1b[4;33;40m' + "2 - Insta" + '\x1b[0m')
        print("")
        print('\x1b[4;31;40m' + "99 - Exit" + '\x1b[0m')
        print("")
        page = input("")
        if page == "1":
            page = '/templates/discord_html+css.html'
        if page == "2":
            page = '/templates/insta_html+css.html'
        if page == "99":
            main()
    if todo == "2":
        page = input("Enter the name of your file (or full path) :\n\n")
    if todo == "99":
        exit(-1)
    if len(todo) == 0:
        vatodo()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
        #    self.path = '/templates/discord_html+css.html'
           self.path = page
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
    print("\n")
    print('\x1b[4;30;44m' + "Enter the IP address to use :" + '\x1b[0m')
    address = input("")
    print("\n")
    print('\x1b[4;30;44m' + "Specify the port :" + '\x1b[0m')
    port = input("")
    if len(port) == 0:
        port = 55555
        print(port)
    else:
        port = int(port)
    print("\n")
    server_address = (address, port)
    vatodo()
    http_server = HTTPServer((server_address), handler)
    print("")
    print('\x1b[6;30;42m' + f'Server running on {address} on port {port}...' + '\x1b[0m')
    http_server.serve_forever()

if __name__ == '__main__':
    main()
