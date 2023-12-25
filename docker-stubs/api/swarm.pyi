from typing import Optional, Dict, List
from .. import errors as errors, types as types, utils as utils
from ..constants import (
    DEFAULT_SWARM_ADDR_POOL as DEFAULT_SWARM_ADDR_POOL,
    DEFAULT_SWARM_SUBNET_SIZE as DEFAULT_SWARM_SUBNET_SIZE,
)

class SwarmApiMixin:
    def create_swarm_spec(self, *args, **kwargs): ...
    def get_unlock_key(self): ...
    def init_swarm(
        self,
        advertise_addr: Optional[str] = None,
        listen_addr: str = DEFAULT_SWARM_ADDR_POOL,
        force_new_cluster: bool = False,
        swarm_spec: Optional[Dict[str, str]] = None,
        default_addr_pool: Optional[List[str]] = None,
        subnet_size: Optional[int] = None,
        data_path_addr: Optional[str] = None,
        data_path_port: Optional[int] = None,
    ): ...
    def inspect_swarm(self): ...
    def inspect_node(self, node_id: str): ...
    def join_swarm(
        self,
        remote_addrs: List[str],
        join_token: str,
        listen_addr: str = DEFAULT_SWARM_ADDR_POOL,
        advertise_addr: Optional[str] = None,
        data_path_addr: Optional[str] = None,
    ): ...
    def leave_swarm(self, force: bool = False): ...
    def nodes(self, filters: Optional[Dict[str, str]] = None): ...
    def remove_node(self, node_id: str, force: bool = False): ...
    def unlock_swarm(self, key: str): ...
    def update_node(
        self, node_id: str, version: str, node_spec: Optional[Dict[str, str]] = None
    ): ...
    def update_swarm(
        self,
        version: str,
        swarm_spec: Optional[Dict[str, str]] = None,
        rotate_worker_token: bool = False,
        rotate_manager_token: bool = False,
        rotate_manager_unlock_key: bool = False,
    ): ...
