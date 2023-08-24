import urllib3.connection
from .. import constants as constants
from .npipesocket import NpipeSocket as NpipeSocket
from _typeshed import Incomplete
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter

RecentlyUsedContainer: Incomplete

class NpipeHTTPConnection(urllib3.connection.HTTPConnection):
    npipe_path: Incomplete
    timeout: Incomplete
    def __init__(self, npipe_path, timeout: int = ...) -> None: ...
    sock: Incomplete
    def connect(self) -> None: ...

class NpipeHTTPConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    npipe_path: Incomplete
    timeout: Incomplete
    def __init__(self, npipe_path, timeout: int = ..., maxsize: int = ...) -> None: ...

class NpipeHTTPAdapter(BaseHTTPAdapter):
    __attrs__: Incomplete
    npipe_path: Incomplete
    timeout: Incomplete
    max_pool_size: Incomplete
    pools: Incomplete
    def __init__(self, base_url, timeout: int = ..., pool_connections=..., max_pool_size=...) -> None: ...
    def get_connection(self, url, proxies: Incomplete | None = ...): ...
    def request_url(self, request, proxies): ...
