from .. import errors as errors, types as types, utils as utils
from ..constants import (
    DEFAULT_SWARM_ADDR_POOL as DEFAULT_SWARM_ADDR_POOL,
    DEFAULT_SWARM_SUBNET_SIZE as DEFAULT_SWARM_SUBNET_SIZE,
)
from _typeshed import Incomplete

log: Incomplete

class SwarmApiMixin:
    def create_swarm_spec(self, *args, **kwargs): ...
    def get_unlock_key(self): ...
    def init_swarm(
        self,
        advertise_addr: Incomplete | None = ...,
        listen_addr: str = ...,
        force_new_cluster: bool = ...,
        swarm_spec: Incomplete | None = ...,
        default_addr_pool: Incomplete | None = ...,
        subnet_size: Incomplete | None = ...,
        data_path_addr: Incomplete | None = ...,
        data_path_port: Incomplete | None = ...,
    ): ...
    def inspect_swarm(self): ...
    def inspect_node(self, node_id): ...
    def join_swarm(
        self,
        remote_addrs,
        join_token,
        listen_addr: str = ...,
        advertise_addr: Incomplete | None = ...,
        data_path_addr: Incomplete | None = ...,
    ): ...
    def leave_swarm(self, force: bool = ...): ...
    def nodes(self, filters: Incomplete | None = ...): ...
    def remove_node(self, node_id, force: bool = ...): ...
    def unlock_swarm(self, key): ...
    def update_node(self, node_id, version, node_spec: Incomplete | None = ...): ...
    def update_swarm(
        self,
        version,
        swarm_spec: Incomplete | None = ...,
        rotate_worker_token: bool = ...,
        rotate_manager_token: bool = ...,
        rotate_manager_unlock_key: bool = ...,
    ): ...
