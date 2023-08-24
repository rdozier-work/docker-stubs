from . import errors as errors
from .transport import SSLHTTPAdapter as SSLHTTPAdapter
from _typeshed import Incomplete

class TLSConfig:
    cert: Incomplete
    ca_cert: Incomplete
    verify: Incomplete
    ssl_version: Incomplete
    assert_hostname: Incomplete
    assert_fingerprint: Incomplete
    def __init__(self, client_cert: Incomplete | None = ..., ca_cert: Incomplete | None = ..., verify: Incomplete | None = ..., ssl_version: Incomplete | None = ..., assert_hostname: Incomplete | None = ..., assert_fingerprint: Incomplete | None = ...) -> None: ...
    def configure_client(self, client) -> None: ...
