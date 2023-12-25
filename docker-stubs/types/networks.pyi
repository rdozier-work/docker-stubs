from typing import Optional, Any
from .. import errors as errors
from ..utils import normalize_links as normalize_links, version_lt as version_lt

class EndpointConfig(dict[str, Any]):
    def __init__(
        self,
        version: str,
        aliases: Optional[list[str]] = None,
        links: Optional[list[str]] = None,
        ipv4_address: Optional[str] = None,
        ipv6_address: Optional[str] = None,
        link_local_ips: Optional[list[str]] = None,
        driver_opt: Optional[dict[str, Any]] = None,
        mac_address: Optional[str] = None,
    ) -> None: ...

class NetworkingConfig(dict[str, Any]):
    def __init__(self, endpoints_config: Optional[dict[str, Any]] = None) -> None: ...

class IPAMConfig(dict[str, Any]):
    def __init__(
        self,
        driver: str = "",
        pool_configs: Optional[list[dict[str, Any]]] = None,
        options: Optional[dict[str, Any]] = None,
    ) -> None: ...

class IPAMPool(dict[str, Any]):
    def __init__(
        self,
        subnet: Optional[str] = None,
        iprange: Optional[str] = None,
        gateway: Optional[str] = None,
        aux_addresses: Optional[dict[str, str]] = None,
    ) -> None: ...
