from typing import Generator, Iterator, Literal

from docker.types import RollbackConfig

from docker.types import EndpointConfig

from docker.types import EndpointSpec

from docker.types import UpdateConfig

from docker.types import TaskTemplate

from .. import auth as auth, errors as errors, utils as utils
from ..types import ServiceMode as ServiceMode
from _typeshed import Incomplete

from ..types._io import JsonDict
from ..types.misc_types import TrueOnSuccess

class ServiceApiMixin:
    def create_service(
        self,
        task_template: TaskTemplate,
        name: str | None = ...,
        labels: dict[str, Incomplete] | None = ...,
        mode: ServiceMode | None = ...,
        update_config: UpdateConfig | None = ...,
        networks: list[str] | None = ...,
        endpoint_config: EndpointConfig | None = ...,
        endpoint_spec: EndpointSpec | None = ...,
        rollback_config: RollbackConfig | None = ...,
    ) -> JsonDict: ...
    def inspect_service(
        self, service: str, insert_defaults: bool | None = ...
    ) -> JsonDict: ...
    def inspect_task(self, task: str) -> JsonDict: ...
    def remove_service(self, service: str) -> TrueOnSuccess: ...
    def services(
        self, filters: dict[str, Incomplete] | None = ..., status: bool | None = ...
    ) -> list[JsonDict]: ...
    def service_logs(
        self,
        service: str,
        details: bool = ...,
        follow: bool = ...,
        stdout: bool = ...,
        stderr: bool = ...,
        since: int = ...,
        timestamps: bool = ...,
        tail: str = ...,
        is_tty: bool | None = ...,
    ) -> Iterator[bytes]: ...
    def tasks(self, filters: dict[str, Incomplete] | None = ...) -> list[JsonDict]: ...
    def update_service(
        self,
        service: str,
        version: int,
        task_template: TaskTemplate | None = ...,
        name: str | None = ...,
        labels: dict[Incomplete, Incomplete] | None = ...,
        mode: ServiceMode | None = ...,
        update_config: UpdateConfig | None = ...,
        networks: list[str] | None = ...,
        endpoint_config: EndpointConfig | None = ...,
        endpoint_spec: EndpointSpec | None = ...,
        fetch_current_spec: bool = ...,
        rollback_config: RollbackConfig | None = ...,
    ) -> dict[Literal["Warnings"], Incomplete]: ...
