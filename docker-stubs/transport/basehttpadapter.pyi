import requests.adapters
from typing import Any, Optional
from urllib3.util.retry import Retry
from requests.models import PreparedRequest, Response

class BaseHTTPAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def send(
        self,
        request: PreparedRequest,
        stream: Optional[bool] = None,
        timeout: Optional[Any] = None,
        verify: Optional[Any] = None,
        cert: Optional[Any] = None,
        proxies: Optional[dict] = None,
    ) -> Response: ...
    def close(self) -> None: ...
    def init_poolmanager(
        self, connections: int, maxsize: int, block: bool = False, **pool_kwargs: Any
    ) -> None: ...
    def proxy_manager_for(self, proxy: str, **proxy_kwargs: Any) -> Any: ...
    def cert_verify(self, conn: Any, url: str, verify: bool, cert: Any) -> None: ...
    def build_response(self, req: PreparedRequest, resp: Any) -> Response: ...
    def get_connection(self, url: str, proxies: Optional[dict] = None) -> Any: ...
    def close(self) -> None: ...
    def request_url(self, request: PreparedRequest, proxies: Optional[dict]) -> str: ...
    def add_headers(
        self,
        request: PreparedRequest,
        stream: Optional[bool] = None,
        timeout: Optional[Any] = None,
        verify: Optional[Any] = None,
        cert: Optional[Any] = None,
        proxies: Optional[dict] = None,
    ) -> None: ...
    def proxy_headers(self, proxy: Optional[str]) -> dict: ...
    def request(
        self,
        method: str,
        url: str,
        headers: Optional[dict] = None,
        files: Optional[dict] = None,
        data: Optional[Any] = None,
        params: Optional[dict] = None,
        auth: Optional[Any] = None,
        cookies: Optional[dict] = None,
        hooks: Optional[dict] = None,
        json: Optional[Any] = None,
    ) -> PreparedRequest: ...
