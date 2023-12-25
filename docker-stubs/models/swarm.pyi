from typing import Any, Dict, Optional, List
from docker.api import APIClient as APIClient
from docker.errors import APIError as APIError
from .resource import Model as Model

class Swarm(Model):
    id_attribute: str = "ID"
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def version(self) -> Dict[str, Any]: ...
    def get_unlock_key(self) -> Dict[str, Any]: ...
    def init(
        self,
        advertise_addr: Optional[str] = None,
        listen_addr: str = "0.0.0.0:2377",
        force_new_cluster: bool = False,
        default_addr_pool: Optional[List[str]] = None,
        subnet_size: Optional[int] = None,
        data_path_addr: Optional[str] = None,
        data_path_port: Optional[int] = None,
        **kwargs: Any
    ) -> Dict[str, Any]: ...
    def join(self, *args: Any, **kwargs: Any) -> Dict[str, Any]: ...
    def leave(self, *args: Any, **kwargs: Any) -> Dict[str, Any]: ...
    attrs: Dict[str, Any]
    def reload(self) -> None: ...
    def unlock(self, key: str) -> Dict[str, Any]: ...
    def update(
        self,
        rotate_worker_token: bool = False,
        rotate_manager_token: bool = False,
        rotate_manager_unlock_key: bool = False,
        **kwargs: Any
    ) -> Dict[str, Any]: ...
