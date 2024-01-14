import http.server
import os.path
import ssl
import socket

class Static(http.server.SimpleHTTPRequestHandler):
    def __init__(self, socket, address, server, dir=None):
        if not dir:
            dir=os.path.join(os.path.dirname(os.path.abspath(__file__)),'static')
        print(f'Dir is now {dir}')
        super().__init__(socket, address, server, directory=dir)

def run():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='./cert.pem', keyfile='./key.pem')
    server = http.server.HTTPServer(('localhost',8443), Static)
    with context.wrap_socket(server.socket, server_side=True) as ssock:
        server.socket = ssock
        server.serve_forever()

run()