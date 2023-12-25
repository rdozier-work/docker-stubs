from typing import Optional, Dict, List
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
        names: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
        filters: Optional[Dict[str, str]] = None,
    ): ...
    def create_network(
        self,
        name: str,
        driver: Optional[str] = None,
        options: Optional[Dict[str, str]] = None,
        ipam: Optional[Dict[str, str]] = None,
        check_duplicate: Optional[bool] = None,
        internal: bool = False,
        labels: Optional[Dict[str, str]] = None,
        enable_ipv6: bool = False,
        attachable: Optional[bool] = None,
        scope: Optional[str] = None,
        ingress: Optional[bool] = None,
    ): ...
    def prune_networks(self, filters: Optional[Dict[str, str]] = None): ...
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
        aliases: Optional[List[str]] = None,
        links: Optional[List[str]] = None,
        link_local_ips: Optional[List[str]] = None,
        driver_opt: Optional[Dict[str, str]] = None,
        mac_address: Optional[str] = None,
    ) -> None: ...
    def disconnect_container_from_network(
        self, container: str, net_id: str, force: bool = False
    ) -> None: ...
