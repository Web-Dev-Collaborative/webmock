from webmock import mock_server
from wsgiref import simple_server
import socket

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

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
        assert 'Hello' in urlopen('http://127.0.0.1:%d/hi' % port).read().decode('ascii')
    assert_port_closed(port)
