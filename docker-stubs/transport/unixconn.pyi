import urllib3.connection
from .. import constants as constants
from _typeshed import Incomplete
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter

RecentlyUsedContainer: Incomplete

class UnixHTTPConnection(urllib3.connection.HTTPConnection):
    base_url: Incomplete
    unix_socket: Incomplete
    timeout: Incomplete
    def __init__(self, base_url, unix_socket, timeout: int = ...) -> None: ...
    sock: Incomplete
    def connect(self) -> None: ...

class UnixHTTPConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    base_url: Incomplete
    socket_path: Incomplete
    timeout: Incomplete
    def __init__(
        self, base_url, socket_path, timeout: int = ..., maxsize: int = ...
    ) -> None: ...

class UnixHTTPAdapter(BaseHTTPAdapter):
    __attrs__: Incomplete
    socket_path: Incomplete
    timeout: Incomplete
    max_pool_size: Incomplete
    pools: Incomplete
    def __init__(
        self, socket_url, timeout: int = ..., pool_connections=..., max_pool_size=...
    ) -> None: ...
    def get_connection(self, url, proxies: Incomplete | None = ...): ...
    def request_url(self, request, proxies): ...
