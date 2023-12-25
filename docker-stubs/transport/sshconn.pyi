import socket
import urllib3.connection
from .. import constants as constants
from typing import Optional, Dict, Any, List
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter

class RecentlyUsedContainer(Dict[str, Any]):
    def __init__(self, maxsize: int = 10) -> None: ...

class SSHSocket(socket.socket):
    host: str
    port: int
    user: str
    proc: Any
    def __init__(self, host: str) -> None: ...
    def connect(self, **kwargs: Any) -> None: ...
    def sendall(self, data: bytes) -> None: ...
    def send(self, data: bytes) -> int: ...
    def recv(self, n: int) -> bytes: ...
    def makefile(self, mode: str) -> Any: ...
    def close(self) -> None: ...

class SSHConnection(urllib3.connection.HTTPConnection):
    ssh_transport: Any
    timeout: int
    ssh_host: str
    def __init__(
        self,
        ssh_transport: Optional[Any] = None,
        timeout: int = constants.DEFAULT_TIMEOUT_SECONDS,
        host: Optional[str] = None,
    ) -> None: ...
    sock: SSHSocket
    def connect(self) -> None: ...

class SSHConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    scheme: str
    ssh_transport: Any
    timeout: int
    ssh_host: str
    def __init__(
        self,
        ssh_client: Optional[Any] = None,
        timeout: int = constants.DEFAULT_TIMEOUT_SECONDS,
        maxsize: int = 1,
        host: Optional[str] = None,
    ) -> None: ...

class SSHHTTPAdapter(BaseHTTPAdapter):
    __attrs__: List[str]
    ssh_client: Any
    ssh_host: str
    timeout: int
    max_pool_size: int
    pools: RecentlyUsedContainer
    def __init__(
        self,
        base_url: str,
        timeout: int = constants.DEFAULT_TIMEOUT_SECONDS,
        pool_connections: int = constants.DEFAULT_MAX_POOL_SIZE,
        max_pool_size: int = constants.DEFAULT_MAX_POOL_SIZE,
        shell_out: bool = False,
    ) -> None: ...
    def get_connection(
        self, url: str, proxies: Optional[Dict[str, str]] = None
    ) -> SSHConnectionPool: ...
    def close(self) -> None: ...
