#!/usr/bin/python3

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from core import route
 
@route('/ws')
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('new connection')
      
    def on_message(self, message):
        print('message received:  %s' % message)
        # Reverse Message and send it back
        print('sending back message: %s' % message[::-1])
        self.write_message(message[::-1])
 
    def on_close(self):
        print('connection closed')
 
    def check_origin(self, origin):
        return True

from core import logging, main_loop, route

class RedirectToSSL(tornado.web.RequestHandler):
    def get(self, path):
        self.redirect('https://www.cloud-fortress.com:9999/{}'.format(path))

redirect_app = tornado.web.Application([(r"/(.*)", RedirectToSSL),],)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(redirect_app)
    http_server.listen(8888, '::')
    ssl_options = {'certfile': '/etc/ssl/certs/ssl-cert-snakeoil.pem',
                   'keyfile': '/etc/ssl/private/ssl-cert-snakeoil.key'}
    https_server = tornado.httpserver.HTTPServer(application, ssl_options=ssl_options)
    https_server.listen(9999, '::')
    tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    tornado.ioloop.IOLoop.current().start()
    tornado.ioloop.IOLoop.instance().start()
