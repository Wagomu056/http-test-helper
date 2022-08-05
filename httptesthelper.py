# -*- coding: utf-8 -*-

import http.server as s
from urllib.parse import urlparse
from urllib.parse import parse_qs

def start_server(port, callback):
    def handler(*args):
        CallbackServer(callback, *args)
    host = '0.0.0.0'
    httpd = s.HTTPServer((host, port), handler)
    print('Start server. - port:%s' % port)
    httpd.serve_forever()

class CallbackServer(s.BaseHTTPRequestHandler):
    def __init__(self, callback, *args):
        self.callback = callback
        s.BaseHTTPRequestHandler.__init__(self, *args)

    def do_POST(self):
        content_len  = int(self.headers.get("content-length", 0))
        req_body = self.rfile.read(content_len).decode("utf-8")

        self.callback(req_body)

        # responce
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', 0)
        self.end_headers()
