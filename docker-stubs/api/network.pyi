from typing import Optional
from .. import utils as utils
from ..errors import InvalidVersion as InvalidVersion
from ..utils import (
    check_resource as check_resource,
    minimum_version as minimum_version,
    version_lt as version_lt,
)

class NetworkApiMixin:
    def networks(
        self,
        names: Optional[list[str]] = None,
        ids: Optional[list[str]] = None,
        filters: Optional[dict[str, str]] = None,
    ): ...
    def create_network(
        self,
        name: str,
        driver: Optional[str] = None,
        options: Optional[dict[str, str]] = None,
        ipam: Optional[dict[str, str]] = None,
        check_duplicate: Optional[bool] = None,
        internal: bool = False,
        labels: Optional[dict[str, str]] = None,
        enable_ipv6: bool = False,
        attachable: Optional[bool] = None,
        scope: Optional[str] = None,
        ingress: Optional[bool] = None,
    ): ...
    def prune_networks(self, filters: Optional[dict[str, str]] = None): ...
    def remove_network(self, net_id: str) -> None: ...
    def inspect_network(
        self, net_id: str, verbose: Optional[bool] = None, scope: Optional[str] = None
    ): ...
    def connect_container_to_network(
        self,
        container: str,
        net_id: str,
        ipv4_address: Optional[str] = None,
        ipv6_address: Optional[str] = None,
        aliases: Optional[list[str]] = None,
        links: Optional[list[str]] = None,
        link_local_ips: Optional[list[str]] = None,
        driver_opt: Optional[dict[str, str]] = None,
        mac_address: Optional[str] = None,
    ) -> None: ...
    def disconnect_container_from_network(
        self, container: str, net_id: str, force: bool = False
    ) -> None: ...
