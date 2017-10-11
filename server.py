from os import curdir
from os.path import join as pjoin
import time
import json
import urlparse

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    # def do_POST(self):
    #     print self.path

    #     suffix = time.time() * 1000000
    #     store_path = pjoin(curdir, 'Check_%d' % suffix)
    #     length = self.handers['content-length']
    #     data = self.rfile.read(int(length))

    #     with open(store_path, 'w') as fh:
    #         fh.write(data)

    #     suffix += 1
    #     self.send_response(200)


    def do_GET(self):
        self.send_response(200)



    def do_POST(self):

        length = int(self.headers['Content-Length'])
        # print length
        # post_data = urlparse.parse_qs(self.rfile.read().decode('utf-8'))
        post_data = self.rfile.read(length).decode('utf-8')
        # print post_data
        data = json.loads(post_data)
        # print data['domain']
        with open((("-").join(data['filename'].split('/')))[2:], 'w') as f:
            f.write(data['filecontent'])

        # print "Sum of values in json is:", sum(data.values())
        self.send_response(200)
        print "\n\n\n\n\n"




        # print self
        # self.send_response(200)
        # # self.send_header('Content-type', 'text/html')
        # self.end_headers()


        # print "got post!!"
        # content_len = int(self.headers.getheader('content-length', 0))
        # post_body = self.rfile.read(content_len)



        # test_data = simplejson.loads(post_body)
        # print "post_body(%s)" % (test_data)
        # return SimpleHTTPRequestHandler.do_POST(self)

    # def do_GET(self):
    #     print self

    #     # suffix = time.time() * 1000000
    #     # store_path = pjoin(curdir, 'Check_%d' % suffix)
    #     # length = self.handers['content-length']
    #     # data = self.rfile.read(int(length))

    #     # with open(store_path, 'w') as fh:
    #     #     fh.write(data)

    #     # suffix += 1
    #     self.send_response(200)

sever = HTTPServer(('', 80), MyServer)
sever.serve_forever()