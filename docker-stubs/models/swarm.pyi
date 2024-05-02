from .resource import Model as Model
from _typeshed import Incomplete
from docker.api import APIClient as APIClient
from docker.errors import APIError as APIError

from ..types.misc_types import TrueOnSuccess

class Swarm(Model):
    id_attribute: str
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    @property
    def version(self) -> str: ...
    def get_unlock_key(self) -> dict[Incomplete, Incomplete]: ...
    def init(
        self,
        advertise_addr: str | None = ...,
        listen_addr: str = ...,
        force_new_cluster: bool = ...,
        default_addr_pool: list[str] | None = ...,
        subnet_size: int | None = ...,
        data_path_addr: str | None = ...,
        data_path_port: int | None = ...,
        **kwargs: Incomplete
    ) -> str: ...
    def join(self, *args: Incomplete, **kwargs: Incomplete) -> TrueOnSuccess: ...
    def leave(self, *args: Incomplete, **kwargs: Incomplete) -> TrueOnSuccess: ...
    attrs: dict[Incomplete, Incomplete]
    def reload(self) -> None: ...
    def unlock(self, key: str) -> TrueOnSuccess: ...
    def update(
        self,
        rotate_worker_token: bool = ...,
        rotate_manager_token: bool = ...,
        rotate_manager_unlock_key: bool = ...,
        **kwargs: Incomplete
    ) -> TrueOnSuccess: ...
