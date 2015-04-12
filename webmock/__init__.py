from wsgiref import simple_server
from contextlib import contextmanager
import threading
import urllib2


# TODO: allow .start/.stop and decoration

class StoppableWSGIServer(simple_server.WSGIServer):

    stopped = False
    def serve_forever(self):
        while not self.stopped:
            self.handle_request()


@contextmanager
def mock_server(app):
    quit_path = '/$!mock_server/quit'

    def middleware(environ, start_response):
        if environ['PATH_INFO'] == quit_path:
            svr.stopped = True
            start_response('200 OK', [])
            return []
        return app(environ, start_response)
    svr = simple_server.make_server('127.0.0.1', 0, middleware, server_class=StoppableWSGIServer)

    thd = threading.Thread(name='mock_server', target=svr.serve_forever)
    thd.daemon = True
    thd.start()

    yield svr.server_port

    urllib2.urlopen('http://127.0.0.1:%d%s' % (svr.server_port, quit_path))
    thd.join()


def test_test():
    with mock_server(simple_server.demo_app) as port:
        print urllib2.urlopen('http://127.0.0.1:%d/hi' % port).read()
