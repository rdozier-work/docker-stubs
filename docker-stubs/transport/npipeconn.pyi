from typing import Any

import urllib3.connection
from .npipesocket import NpipeSocket as NpipeSocket
from _typeshed import Incomplete
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter

RecentlyUsedContainer = Incomplete

class NpipeHTTPConnection(urllib3.connection.HTTPConnection):
    npipe_path: str
    timeout: int
    def __init__(self, npipe_path: str, timeout: int = ...) -> None: ...
    sock: Incomplete
    def connect(self) -> None: ...

class NpipeHTTPConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    npipe_path: str
    timeout: int
    def __init__(
        self, npipe_path: str, timeout: int = ..., maxsize: int = ...
    ) -> None: ...

class NpipeHTTPAdapter(BaseHTTPAdapter):
    __attrs__: list[str]
    npipe_path: str
    timeout: int
    max_pool_size: int
    pools: RecentlyUsedContainer
    def __init__(
        self,
        base_url: str,
        timeout: int = ...,
        pool_connections: int = ...,
        max_pool_size: int = ...,
    ) -> None: ...
    def get_connection(
        self, url: str, proxies: Incomplete | None = ...
    ) -> NpipeHTTPConnectionPool: ...
    def request_url(self, request: Any, proxies: Any) -> str: ...
