from ..api import APIClient as APIClient
from .resource import Collection as Collection, Model as Model
from _typeshed import Incomplete

class Volume(Model):
    id_attribute: str
    @property
    def name(self) -> str: ...
    def remove(self, force: bool = ...) -> None: ...

class VolumeCollection(Collection):
    model = Volume
    def create(self, name: str | None = ..., **kwargs) -> Volume: ...
    def get(self, volume_id: str) -> Volume: ...
    def list(self, **kwargs) -> list[Volume]: ...
    def prune(self, filters: Incomplete | None = ...): ...
