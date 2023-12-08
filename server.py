from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

directory = "/"
port = 3000

handler = SimpleHTTPRequestHandler
handler.extensions_map.update({
    ".html": "text/html",
    ".css": "text/css",
    ".js": "application/javascript",
})

with TCPServer(("", port), handler) as httpd:
    print(f"Web server berjalan di port {port}")
    print(f"Buka browser dan kunjungi http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print("\nServer dimatikan")
