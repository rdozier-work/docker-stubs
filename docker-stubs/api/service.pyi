from typing import Optional
from .. import auth as auth, errors as errors, utils as utils
from ..types import ServiceMode as ServiceMode

class ServiceApiMixin:
    def create_service(
        self,
        task_template: dict[str, str],
        name: Optional[str] = None,
        labels: Optional[dict[str, str]] = None,
        mode: Optional[ServiceMode] = None,
        update_config: Optional[dict[str, str]] = None,
        networks: Optional[list[str]] = None,
        endpoint_config: Optional[dict[str, str]] = None,
        endpoint_spec: Optional[dict[str, str]] = None,
        rollback_config: Optional[dict[str, str]] = None,
    ) -> dict[str, str]: ...
    def inspect_service(
        self, service: str, insert_defaults: Optional[bool] = None
    ) -> dict[str, str]: ...
    def inspect_task(self, task: str) -> dict[str, str]: ...
    def remove_service(self, service: str) -> None: ...
    def services(
        self, filters: Optional[dict[str, str]] = None, status: Optional[str] = None
    ) -> list[dict[str, str]]: ...
    def service_logs(
        self,
        service: str,
        details: bool = False,
        follow: bool = False,
        stdout: bool = False,
        stderr: bool = False,
        since: int = 0,
        timestamps: bool = False,
        tail: str = "all",
        is_tty: Optional[bool] = None,
    ) -> str: ...
    def tasks(
        self, filters: Optional[dict[str, str]] = None
    ) -> list[dict[str, str]]: ...
    def update_service(
        self,
        service: str,
        version: str,
        task_template: Optional[dict[str, str]] = None,
        name: Optional[str] = None,
        labels: Optional[dict[str, str]] = None,
        mode: Optional[ServiceMode] = None,
        update_config: Optional[dict[str, str]] = None,
        networks: Optional[list[str]] = None,
        endpoint_config: Optional[dict[str, str]] = None,
        endpoint_spec: Optional[dict[str, str]] = None,
        fetch_current_spec: bool = False,
        rollback_config: Optional[dict[str, str]] = None,
    ) -> dict[str, str]: ...
