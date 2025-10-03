import http.server
import socketserver
import os
import webbrowser

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index"):  # si entras sin ruta o pones /index
            self.path = "/index.html"     # siempre abre index.html
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Nos aseguramos que sirva desde la carpeta actual
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"\n🔥 Servidor corriendo en {url}\n")
    # Abrir navegador automáticamente
    webbrowser.open(url)
    httpd.serve_forever()
