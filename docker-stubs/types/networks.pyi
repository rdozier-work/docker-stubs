from .. import errors as errors
from ..utils import normalize_links as normalize_links, version_lt as version_lt
from _typeshed import Incomplete

class EndpointConfig(dict):
    def __init__(
        self,
        version,
        aliases: Incomplete | None = ...,
        links: Incomplete | None = ...,
        ipv4_address: Incomplete | None = ...,
        ipv6_address: Incomplete | None = ...,
        link_local_ips: Incomplete | None = ...,
        driver_opt: Incomplete | None = ...,
        mac_address: Incomplete | None = ...,
    ) -> None: ...

class NetworkingConfig(dict):
    def __init__(self, endpoints_config: Incomplete | None = ...) -> None: ...

class IPAMConfig(dict):
    def __init__(
        self,
        driver: str = ...,
        pool_configs: Incomplete | None = ...,
        options: Incomplete | None = ...,
    ) -> None: ...

class IPAMPool(dict):
    def __init__(
        self,
        subnet: Incomplete | None = ...,
        iprange: Incomplete | None = ...,
        gateway: Incomplete | None = ...,
        aux_addresses: Incomplete | None = ...,
    ) -> None: ...
