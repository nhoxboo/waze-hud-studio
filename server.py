import http.server
import socketserver
import ssl
import os
import sys
import threading

DIRECTORY = "E:/hermes-workspace/waze-hud-web-studio"
HTTP_PORT = 8088
HTTPS_PORT = 8443

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def run_http_server():
    try:
        with ReusableTCPServer(('0.0.0.0', HTTP_PORT), Handler) as httpd:
            print(f"[HTTP] Serving at http://0.0.0.0:{HTTP_PORT}")
            httpd.serve_forever()
    except Exception as e:
        print(f"[HTTP] Error: {e}")

def run_https_server():
    cert_file = os.path.join(DIRECTORY, 'cert.pem')
    key_file = os.path.join(DIRECTORY, 'key.pem')
    if not os.path.exists(cert_file) or not os.path.exists(key_file):
        print("[HTTPS] Certificate files not found, skipping HTTPS")
        return

    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=cert_file, keyfile=key_file)

        with ReusableTCPServer(('0.0.0.0', HTTPS_PORT), Handler) as httpsd:
            httpsd.socket = context.wrap_socket(httpsd.socket, server_side=True)
            print(f"[HTTPS] Serving at https://0.0.0.0:{HTTPS_PORT}")
            httpsd.serve_forever()
    except Exception as e:
        print(f"[HTTPS] Error: {e}")

if __name__ == '__main__':
    os.chdir(DIRECTORY)
    t_https = threading.Thread(target=run_https_server, daemon=True)
    t_https.start()
    run_http_server()
