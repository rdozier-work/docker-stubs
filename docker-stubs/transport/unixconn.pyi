import urllib3.connection
from .. import constants as constants
from typing import Optional, Any
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter

class RecentlyUsedContainer(dict[str, Any]):
    def __init__(self, maxsize: int = 10) -> None: ...

class UnixHTTPConnection(urllib3.connection.HTTPConnection):
    base_url: str
    unix_socket: str
    timeout: int
    def __init__(
        self,
        base_url: str,
        unix_socket: str,
        timeout: int = constants.DEFAULT_TIMEOUT_SECONDS,
    ) -> None: ...
    sock: Any
    def connect(self) -> None: ...

class UnixHTTPConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    base_url: str
    socket_path: str
    timeout: int
    def __init__(
        self,
        base_url: str,
        socket_path: str,
        timeout: int = constants.DEFAULT_TIMEOUT_SECONDS,
        maxsize: int = 1,
    ) -> None: ...

class UnixHTTPAdapter(BaseHTTPAdapter):
    __attrs__: list[str]
    socket_path: str
    timeout: int
    max_pool_size: int
    pools: RecentlyUsedContainer
    def __init__(
        self,
        socket_url: str,
        timeout: int = constants.DEFAULT_TIMEOUT_SECONDS,
        pool_connections: int = constants.DEFAULT_MAX_POOL_SIZE,
        max_pool_size: int = constants.DEFAULT_MAX_POOL_SIZE,
    ) -> None: ...
    def get_connection(
        self, url: str, proxies: Optional[dict[str, str]] = None
    ) -> UnixHTTPConnectionPool: ...
    def request_url(self, request: Any, proxies: dict[str, str]) -> str: ...
