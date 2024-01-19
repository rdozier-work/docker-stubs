import urllib3.connection
from .. import constants as constants
from .npipesocket import NpipeSocket as NpipeSocket
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter
from typing import Optional, Any

class RecentlyUsedContainer(dict[str, Any]):
    def __init__(self, maxsize: int = 10) -> None: ...

class NpipeHTTPConnection(urllib3.connection.HTTPConnection):
    npipe_path: str
    timeout: int
    def __init__(
        self, npipe_path: str, timeout: int = constants.DEFAULT_TIMEOUT_SECONDS
    ) -> None: ...
    sock: NpipeSocket
    def connect(self) -> None: ...

class NpipeHTTPConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    npipe_path: str
    timeout: int
    def __init__(
        self,
        npipe_path: str,
        timeout: int = constants.DEFAULT_TIMEOUT_SECONDS,
        maxsize: int = 1,
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
        timeout: int = constants.DEFAULT_TIMEOUT_SECONDS,
        pool_connections: int = constants.DEFAULT_MAX_POOL_SIZE,
        max_pool_size: int = constants.DEFAULT_MAX_POOL_SIZE,
    ) -> None: ...
    def get_connection(
        self, url: str, proxies: Optional[dict[str, str]] = None
    ) -> NpipeHTTPConnectionPool: ...
    def request_url(self, request: Any, proxies: Optional[dict[str, str]]) -> str: ...
