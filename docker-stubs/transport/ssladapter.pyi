from typing import Optional, Any, List
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter
from urllib3.poolmanager import PoolManager

class SSLHTTPAdapter(BaseHTTPAdapter):
    __attrs__: List[str]
    ssl_version: Optional[int]
    assert_hostname: Optional[bool]
    assert_fingerprint: Optional[str]
    def __init__(
        self,
        ssl_version: Optional[int] = None,
        assert_hostname: Optional[bool] = None,
        assert_fingerprint: Optional[str] = None,
        **kwargs: Any
    ) -> None: ...
    poolmanager: PoolManager
    def init_poolmanager(
        self, connections: int, maxsize: int, block: bool = False
    ) -> None: ...
    def get_connection(self, *args: Any, **kwargs: Any) -> Any: ...
    def can_override_ssl_version(self) -> bool: ...
