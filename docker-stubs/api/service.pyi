from typing import Optional, Dict, List
from .. import auth as auth, errors as errors, utils as utils
from ..types import ServiceMode as ServiceMode

class ServiceApiMixin:
    def create_service(
        self,
        task_template: Dict[str, str],
        name: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        mode: Optional[ServiceMode] = None,
        update_config: Optional[Dict[str, str]] = None,
        networks: Optional[List[str]] = None,
        endpoint_config: Optional[Dict[str, str]] = None,
        endpoint_spec: Optional[Dict[str, str]] = None,
        rollback_config: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]: ...
    def inspect_service(
        self, service: str, insert_defaults: Optional[bool] = None
    ) -> Dict[str, str]: ...
    def inspect_task(self, task: str) -> Dict[str, str]: ...
    def remove_service(self, service: str) -> None: ...
    def services(
        self, filters: Optional[Dict[str, str]] = None, status: Optional[str] = None
    ) -> List[Dict[str, str]]: ...
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
        self, filters: Optional[Dict[str, str]] = None
    ) -> List[Dict[str, str]]: ...
    def update_service(
        self,
        service: str,
        version: str,
        task_template: Optional[Dict[str, str]] = None,
        name: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        mode: Optional[ServiceMode] = None,
        update_config: Optional[Dict[str, str]] = None,
        networks: Optional[List[str]] = None,
        endpoint_config: Optional[Dict[str, str]] = None,
        endpoint_spec: Optional[Dict[str, str]] = None,
        fetch_current_spec: bool = False,
        rollback_config: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]: ...
