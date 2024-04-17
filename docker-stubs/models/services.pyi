from typing import Generator

from .resource import Collection as Collection, Model as Model
from _typeshed import Incomplete
from docker.errors import (
    InvalidArgument as InvalidArgument,
    create_unexpected_kwargs_error as create_unexpected_kwargs_error,
)
from docker.types import (
    ContainerSpec as ContainerSpec,
    Placement as Placement,
    ServiceMode as ServiceMode,
    TaskTemplate as TaskTemplate,
)
from ..types.misc_types import TrueOnSuccess


class Service(Model):
    id_attribute: str
    @property
    def name(self) -> str: ...
    @property
    def version(self) -> str: ...
    def remove(self) -> None: ...
    def tasks(self, filters: dict | None = ...) -> list[dict]: ...
    def logs(self, **kwargs) -> Generator[bytes, None, None]: ...
    def update(self, **kwargs) -> None: ...
    def scale(self, replicas: int) -> TrueOnSuccess: ...
    def force_update(self) -> TrueOnSuccess: ...

class ServiceCollection(Collection):
    model = Service
    def create(self, image: str, command: list[str] | str | None = ..., **kwargs) -> Service: ...
    def get(self, service_id: str, insert_defaults: bool | None = ...) -> Service: ...
    def list(self, **kwargs) -> list[Service]: ...

CONTAINER_SPEC_KWARGS: list[str]
TASK_TEMPLATE_KWARGS: list[str]
CREATE_SERVICE_KWARGS: list[str]
PLACEMENT_KWARGS: list[str]
