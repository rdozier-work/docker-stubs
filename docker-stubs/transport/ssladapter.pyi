from _typeshed import Incomplete
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter

PoolManager: Incomplete

class SSLHTTPAdapter(BaseHTTPAdapter):
    __attrs__: Incomplete
    ssl_version: Incomplete
    assert_hostname: Incomplete
    assert_fingerprint: Incomplete
    def __init__(self, ssl_version: Incomplete | None = ..., assert_hostname: Incomplete | None = ..., assert_fingerprint: Incomplete | None = ..., **kwargs) -> None: ...
    poolmanager: Incomplete
    def init_poolmanager(self, connections, maxsize, block: bool = ...) -> None: ...
    def get_connection(self, *args, **kwargs): ...
    def can_override_ssl_version(self): ...
