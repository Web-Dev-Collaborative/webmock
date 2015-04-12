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

def assert_server_running(port):
    assert 'Hello' in urlopen('http://127.0.0.1:%d/hi' % port).read().decode('ascii')

def test_contextmanager():
    with mock_server(simple_server.demo_app) as port:
        assert_server_running(port)
    assert_port_closed(port)

def test_start_stop():
    svr = mock_server(simple_server.demo_app)
    port = svr.start()
    assert_server_running(port)
    svr.stop()
    assert_port_closed(port)

def test_decorator():
    port_storage = []

    @mock_server(simple_server.demo_app)
    def decorated(port, arg1, arg2=None):
        port_storage.append(port)
        assert arg1 == 1
        assert arg2 == 2
        assert_server_running(port)
    decorated(1, arg2=2)
    assert_port_closed(port_storage[0])
