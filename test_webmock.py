from webmock import mock_server
from wsgiref import simple_server
import urllib2
import socket

def assert_port_closed(port):
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.connect(('127.0.0.1', port))
    except socket.error:
        pass
    else:
        assert 0, "port still open"

def test_contextmanager():
    with mock_server(simple_server.demo_app) as port:
        assert 'Hello' in urllib2.urlopen('http://127.0.0.1:%d/hi' % port).read()
    assert_port_closed(port)
