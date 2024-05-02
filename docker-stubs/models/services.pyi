from typing import Iterator

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
    def tasks(
        self, filters: dict[Incomplete, Incomplete] | None = ...
    ) -> list[dict[Incomplete, Incomplete]]: ...
    def logs(self, **kwargs: Incomplete) -> Iterator[bytes]: ...
    def update(self, **kwargs: Incomplete) -> None: ...
    def scale(self, replicas: int) -> TrueOnSuccess: ...
    def force_update(self) -> TrueOnSuccess: ...

class ServiceCollection(Collection):
    model = Service
    def create(  # type: ignore[override]
        self, image: str, command: list[str] | str | None = ..., **kwargs: Incomplete
    ) -> Service: ...
    def get(self, service_id: str, insert_defaults: bool | None = ...) -> Service: ...  # type: ignore[override]
    def list(self, **kwargs: Incomplete) -> list[Service]: ...  # type: ignore[override]

CONTAINER_SPEC_KWARGS: list[str]
TASK_TEMPLATE_KWARGS: list[str]
CREATE_SERVICE_KWARGS: list[str]
PLACEMENT_KWARGS: list[str]
