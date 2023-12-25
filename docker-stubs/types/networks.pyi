from typing import Optional, Dict, Any, List
from .. import errors as errors
from ..utils import normalize_links as normalize_links, version_lt as version_lt

class EndpointConfig(Dict[str, Any]):
    def __init__(
        self,
        version: str,
        aliases: Optional[List[str]] = None,
        links: Optional[List[str]] = None,
        ipv4_address: Optional[str] = None,
        ipv6_address: Optional[str] = None,
        link_local_ips: Optional[List[str]] = None,
        driver_opt: Optional[Dict[str, Any]] = None,
        mac_address: Optional[str] = None,
    ) -> None: ...

class NetworkingConfig(Dict[str, Any]):
    def __init__(self, endpoints_config: Optional[Dict[str, Any]] = None) -> None: ...

class IPAMConfig(Dict[str, Any]):
    def __init__(
        self,
        driver: str = "",
        pool_configs: Optional[List[Dict[str, Any]]] = None,
        options: Optional[Dict[str, Any]] = None,
    ) -> None: ...

class IPAMPool(Dict[str, Any]):
    def __init__(
        self,
        subnet: Optional[str] = None,
        iprange: Optional[str] = None,
        gateway: Optional[str] = None,
        aux_addresses: Optional[Dict[str, str]] = None,
    ) -> None: ...
