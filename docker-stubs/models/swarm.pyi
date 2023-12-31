from .resource import Model as Model
from _typeshed import Incomplete
from docker.api import APIClient as APIClient
from docker.errors import APIError as APIError

class Swarm(Model):
    id_attribute: str
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def version(self): ...
    def get_unlock_key(self): ...
    def init(
        self,
        advertise_addr: Incomplete | None = ...,
        listen_addr: str = ...,
        force_new_cluster: bool = ...,
        default_addr_pool: Incomplete | None = ...,
        subnet_size: Incomplete | None = ...,
        data_path_addr: Incomplete | None = ...,
        data_path_port: Incomplete | None = ...,
        **kwargs
    ): ...
    def join(self, *args, **kwargs): ...
    def leave(self, *args, **kwargs): ...
    attrs: Incomplete
    def reload(self) -> None: ...
    def unlock(self, key): ...
    def update(
        self,
        rotate_worker_token: bool = ...,
        rotate_manager_token: bool = ...,
        rotate_manager_unlock_key: bool = ...,
        **kwargs
    ): ...
