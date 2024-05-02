from docker.types import SwarmSpec

from .. import errors as errors, types as types, utils as utils
from ..constants import (
    DEFAULT_SWARM_ADDR_POOL as DEFAULT_SWARM_ADDR_POOL,
    DEFAULT_SWARM_SUBNET_SIZE as DEFAULT_SWARM_SUBNET_SIZE,
)
from _typeshed import Incomplete

from ..types._io import JsonDict
from ..types.misc_types import TrueOnSuccess

log: Incomplete

class SwarmApiMixin:
    def create_swarm_spec(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> SwarmSpec: ...
    def get_unlock_key(self) -> dict[Incomplete, Incomplete]: ...
    def init_swarm(
        self,
        advertise_addr: str | None = ...,
        listen_addr: str = ...,
        force_new_cluster: bool = ...,
        swarm_spec: dict[Incomplete, Incomplete] | None = ...,
        default_addr_pool: list[str] | None = ...,
        subnet_size: int | None = ...,
        data_path_addr: str | None = ...,
        data_path_port: int | None = ...,
    ) -> str: ...
    def inspect_swarm(self) -> JsonDict: ...
    def inspect_node(self, node_id: str) -> JsonDict: ...
    def join_swarm(
        self,
        remote_addrs: list[str],
        join_token: str,
        listen_addr: str = ...,
        advertise_addr: str | None = ...,
        data_path_addr: str | None = ...,
    ) -> TrueOnSuccess: ...
    def leave_swarm(self, force: bool = ...) -> TrueOnSuccess: ...
    def nodes(
        self, filters: dict[Incomplete, Incomplete] | None = ...
    ) -> list[JsonDict]: ...
    def remove_node(self, node_id: str, force: bool = ...) -> TrueOnSuccess: ...
    def unlock_swarm(self, key: str) -> TrueOnSuccess: ...
    def update_node(
        self,
        node_id: str,
        version: int,
        node_spec: dict[Incomplete, Incomplete] | None = ...,
    ) -> TrueOnSuccess: ...
    def update_swarm(
        self,
        version: int,
        swarm_spec: dict[Incomplete, Incomplete] | None = ...,
        rotate_worker_token: bool = ...,
        rotate_manager_token: bool = ...,
        rotate_manager_unlock_key: bool = ...,
    ) -> TrueOnSuccess: ...
