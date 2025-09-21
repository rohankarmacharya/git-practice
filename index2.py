from http.server import SimpleHTTPRequestHandler, HTTPServer


class IndexHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <html>
                    <head><title>Index Page</title></head>
                    <body>
                        <h1>Welcome to the Index Page!</h1>
                    </body>
                </html>
            """)
        else:
            self.send_error(404, "File Not Found")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, IndexHandler)
    print("Serving on http://localhost:8000/")
    httpd.serve_forever()
