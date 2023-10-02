import socket
import urllib3.connection
from .. import constants as constants
from _typeshed import Incomplete
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter

RecentlyUsedContainer: Incomplete

class SSHSocket(socket.socket):
    host: Incomplete
    port: Incomplete
    user: Incomplete
    proc: Incomplete
    def __init__(self, host) -> None: ...
    def connect(self, **kwargs) -> None: ...
    def sendall(self, data) -> None: ...
    def send(self, data): ...
    def recv(self, n): ...
    def makefile(self, mode): ...
    def close(self) -> None: ...

class SSHConnection(urllib3.connection.HTTPConnection):
    ssh_transport: Incomplete
    timeout: Incomplete
    ssh_host: Incomplete
    def __init__(
        self,
        ssh_transport: Incomplete | None = ...,
        timeout: int = ...,
        host: Incomplete | None = ...,
    ) -> None: ...
    sock: Incomplete
    def connect(self) -> None: ...

class SSHConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    scheme: str
    ssh_transport: Incomplete
    timeout: Incomplete
    ssh_host: Incomplete
    def __init__(
        self,
        ssh_client: Incomplete | None = ...,
        timeout: int = ...,
        maxsize: int = ...,
        host: Incomplete | None = ...,
    ) -> None: ...

class SSHHTTPAdapter(BaseHTTPAdapter):
    __attrs__: Incomplete
    ssh_client: Incomplete
    ssh_host: Incomplete
    timeout: Incomplete
    max_pool_size: Incomplete
    pools: Incomplete
    def __init__(
        self,
        base_url,
        timeout: int = ...,
        pool_connections=...,
        max_pool_size=...,
        shell_out: bool = ...,
    ) -> None: ...
    def get_connection(self, url, proxies: Incomplete | None = ...): ...
    def close(self) -> None: ...
