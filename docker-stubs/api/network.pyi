from docker.types import IPAMConfig

from .. import utils as utils
from ..errors import InvalidVersion as InvalidVersion
from ..types._io import Json, JsonDict
from ..utils import (
    check_resource as check_resource,
    minimum_version as minimum_version,
    version_lt as version_lt,
)
from _typeshed import Incomplete

class NetworkApiMixin:
    def networks(
        self,
        names: list[str] | None = ...,
        ids: list[str] | None = ...,
        filters: dict[str, Incomplete] | None = ...,
    ) -> JsonDict: ...
    def create_network(
        self,
        name: str,
        driver: str | None = ...,
        options: dict[Incomplete, Incomplete] | None = ...,
        ipam: IPAMConfig | None = ...,
        check_duplicate: bool | None = ...,
        internal: bool = ...,
        labels: dict[str, Incomplete] | None = ...,
        enable_ipv6: bool = ...,
        attachable: bool | None = ...,
        scope: str | None = ...,
        ingress: bool | None = ...,
    ) -> JsonDict: ...
    def prune_networks(self, filters: Incomplete | None = ...) -> JsonDict: ...
    def remove_network(self, net_id: str) -> None: ...
    def inspect_network(
        self, net_id: str, verbose: bool | None = ..., scope: str | None = ...
    ) -> Json: ...
    def connect_container_to_network(
        self,
        container: str,
        net_id: str,
        ipv4_address: str | None = ...,
        ipv6_address: str | None = ...,
        aliases: list[Incomplete] | None = ...,
        links: list[Incomplete] | None = ...,
        link_local_ips: list[str] | None = ...,
        driver_opt: dict[str, Incomplete] | None = ...,
        mac_address: str | None = ...,
    ) -> None: ...
    def disconnect_container_from_network(
        self, container: str, net_id: str, force: bool = ...
    ) -> None: ...
