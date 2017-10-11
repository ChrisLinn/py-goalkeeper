from os import curdir
from os.path import join as pjoin
import os
import time
import json
import urlparse
from datetime import datetime

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.send_response(200)

    def do_POST(self):
        subdirectory = datetime.now().strftime("%d_%H")+"_s"

        try:
            os.mkdir(subdirectory)
        except Exception:
            pass

        length = int(self.headers['Content-Length'])
        # post_data = urlparse.parse_qs(self.rfile.read().decode('utf-8'))
        post_data = self.rfile.read(length).decode('utf-8')
        # print post_data
        data = json.loads(post_data)

        fname = (("-").join(data['filename'].split('/')))[2:]

        with open(os.path.join(subdirectory,fname), 'w') as f:
            f.write(data['filecontent'])

        self.send_response(200)
        print "\n\n\n\n\n"


sever = HTTPServer(('', 80), MyServer)
sever.serve_forever()