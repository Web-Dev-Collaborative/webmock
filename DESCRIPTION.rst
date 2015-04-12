webmock
=======

This tool provides an in-process WSGI server on an ephemeral port.
It is intended for use in unit tests, when the system under test makes outgoing HTTP connections that cannot easily be mocked.
