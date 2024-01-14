import http.server
import os.path
import ssl
import socket

# This works but:
# DeprecationWarning: ssl.wrap_socket() is deprecated, use SSLContext.wrap_socket()

class Static(http.server.SimpleHTTPRequestHandler):
    def __init__(self, socket, address, server, dir=None):
        if not dir:
            dir=os.path.join(os.path.dirname(os.path.abspath(__file__)),'static')
        print(f'Dir is now {dir}')
        super().__init__(socket, address, server, directory=dir)

def run():
    server = http.server.HTTPServer(('localhost',8443), Static)
    with ssl.wrap_socket(server.socket,keyfile='./key.pem', certfile='./cert.pem', server_side=True) as ssock:
        server.socket = ssock
        server.serve_forever()

run()