from typing import Optional, Union
from . import errors as errors
from .transport import SSLHTTPAdapter as SSLHTTPAdapter

class TLSConfig:
    cert: Optional[Union[str, tuple[str, str]]]
    ca_cert: Optional[str]
    verify: Union[bool, str]
    ssl_version: Optional[int]
    assert_hostname: Optional[Union[bool, str]]
    assert_fingerprint: Optional[str]
    def __init__(
        self,
        client_cert: Optional[Union[str, tuple[str, str]]] = None,
        ca_cert: Optional[str] = None,
        verify: Union[bool, str] = None,
        ssl_version: Optional[int] = None,
        assert_hostname: Optional[Union[bool, str]] = None,
        assert_fingerprint: Optional[str] = None,
    ) -> None: ...
    def configure_client(self, client: SSLHTTPAdapter) -> None: ...
