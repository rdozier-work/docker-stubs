from ..api import APIClient as APIClient
from ..utils import version_gte as version_gte
from .containers import Container as Container
from .resource import Collection as Collection, Model as Model
from _typeshed import Incomplete

class Network(Model):
    @property
    def name(self) -> str: ...
    @property
    def containers(self) -> list[Container]: ...
    def connect(self, container: str, *args, **kwargs) -> None: ...
    def disconnect(self, container: str, *args, **kwargs) -> None: ...
    def remove(self) -> None: ...

class NetworkCollection(Collection):
    model = Network
    def create(self, name: str, *args, **kwargs) -> Network: ...
    def get(self, network_id: str, *args, **kwargs) -> Network: ...
    def list(self, *args, **kwargs) -> list[Network]: ...
    def prune(self, filters: Incomplete | None = ...): ...
