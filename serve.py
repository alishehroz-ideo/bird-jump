import http.server, socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        if path.endswith('.wasm'):   return 'application/wasm'
        if path.endswith('.js'):     return 'application/javascript'
        if path.endswith('.data'):   return 'application/octet-stream'
        if path.endswith('.br'):     return 'application/octet-stream'
        return super().guess_type(path)

    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

with socketserver.TCPServer(('', 8080), Handler) as httpd:
    print('Serving at http://localhost:8080')
    httpd.serve_forever()
