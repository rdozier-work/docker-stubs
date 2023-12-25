from typing import Any, Dict, List, Optional
from .. import errors as errors
from ..constants import IS_WINDOWS_PLATFORM as IS_WINDOWS_PLATFORM
from ..utils import (
    check_resource as check_resource,
    convert_service_networks as convert_service_networks,
    format_environment as format_environment,
    format_extra_hosts as format_extra_hosts,
    parse_bytes as parse_bytes,
    split_command as split_command,
)
from _typeshed import Incomplete

class TaskTemplate(Dict[str, Any]):
    def __init__(
        self,
        container_spec: Any,
        resources: Dict[str, Any] | None = None,
        restart_policy: Dict[str, Any] | None = None,
        placement: Dict[str, Any] | None = None,
        log_driver: Dict[str, Any] | None = None,
        networks: List[Dict[str, Any]] | None = None,
        force_update: int | None = None,
    ) -> None: ...
    @property
    def container_spec(self): ...
    @property
    def resources(self): ...
    @property
    def restart_policy(self): ...
    @property
    def placement(self): ...

class ContainerSpec(Dict[str, Any]):
    def __init__(
        self,
        image: str,
        command: List[str] | None = None,
        args: List[str] | None = None,
        hostname: str | None = None,
        env: Dict[str, str] | None = None,
        workdir: str | None = None,
        user: str | None = None,
        labels: Dict[str, str] | None = None,
        mounts: List[Dict[str, Any]] | None = None,
        stop_grace_period: int | None = None,
        secrets: List[Dict[str, Any]] | None = None,
        tty: bool | None = None,
        groups: List[str] | None = None,
        open_stdin: bool | None = None,
        read_only: bool | None = None,
        stop_signal: str | None = None,
        healthcheck: Dict[str, Any] | None = None,
        hosts: Dict[str, str] | None = None,
        dns_config: Dict[str, Any] | None = None,
        configs: List[Dict[str, Any]] | None = None,
        privileges: Dict[str, Any] | None = None,
        isolation: str | None = None,
        init: bool | None = None,
        cap_add: List[str] | None = None,
        cap_drop: List[str] | None = None,
        sysctls: Dict[str, str] | None = None,
    ) -> None: ...

class Mount(Dict[str, Any]):
    def __init__(
        self,
        target: str,
        source: str,
        type: str = "bind",
        read_only: bool = False,
        consistency: str | None = None,
        propagation: str | None = None,
        no_copy: bool = False,
        labels: Dict[str, str] | None = None,
        driver_config: Dict[str, Any] | None = None,
        tmpfs_size: int | None = None,
        tmpfs_mode: int | None = None,
    ) -> None: ...
    @classmethod
    def parse_mount_string(cls, string): ...

class Resources(Dict[str, Any]):
    def __init__(
        self,
        cpu_limit: int | None = None,
        mem_limit: int | None = None,
        cpu_reservation: int | None = None,
        mem_reservation: int | None = None,
        generic_resources: List[Dict[str, Any]] | None = None,
    ) -> None: ...

class UpdateConfig(Dict[str, Any]):
    def __init__(
        self,
        parallelism: int = 1,
        delay: int | None = None,
        failure_action: str = "pause",
        monitor: int | None = None,
        max_failure_ratio: float | None = None,
        order: str | None = None,
    ) -> None: ...

class RollbackConfig(UpdateConfig):
    pass

class RestartConditionTypesEnum:
    NONE: Incomplete
    ON_FAILURE: Incomplete
    ANY: Incomplete

class RestartPolicy(Dict[str, Any]):
    def __init__(
        self,
        condition: str = "any",
        delay: int = 5,
        max_attempts: int = 5,
        window: int = 5,
    ) -> None: ...

class DriverConfig(Dict[str, Any]):
    def __init__(self, name: str, options: Optional[Incomplete] = None) -> None: ...

class EndpointSpec(Dict[str, Any]):
    def __init__(
        self, mode: Optional[Incomplete] = None, ports: Optional[Incomplete] = None
    ) -> None: ...

class ServiceMode(Dict[str, Any]):
    mode: Incomplete
    def __init__(
        self,
        mode: Any,
        replicas: Optional[Incomplete] = None,
        concurrency: Optional[Incomplete] = None,
    ) -> None: ...
    @property
    def replicas(self) -> Any: ...

class SecretReference(Dict[str, Any]):
    def __init__(
        self,
        secret_id: str,
        secret_name: str,
        filename: Optional[Incomplete] = None,
        uid: Optional[Incomplete] = None,
        gid: Optional[Incomplete] = None,
        mode: int = 0,
    ) -> None: ...

class ConfigReference(Dict[str, Any]):
    def __init__(
        self,
        config_id: str,
        config_name: str,
        filename: Optional[Incomplete] = None,
        uid: Optional[Incomplete] = None,
        gid: Optional[Incomplete] = None,
        mode: int = 0,
    ) -> None: ...

class Placement(Dict[str, Any]):
    def __init__(
        self,
        constraints: Optional[Incomplete] = None,
        preferences: Optional[Incomplete] = None,
        platforms: Optional[Incomplete] = None,
        maxreplicas: Optional[Incomplete] = None,
    ) -> None: ...

class PlacementPreference(Dict[str, Any]):
    def __init__(self, strategy: Any, descriptor: Any) -> None: ...

class DNSConfig(Dict[str, Any]):
    def __init__(
        self,
        nameservers: Optional[Incomplete] = None,
        search: Optional[Incomplete] = None,
        options: Optional[Incomplete] = None,
    ) -> None: ...

class Privileges(Dict[str, Any]):
    def __init__(
        self,
        credentialspec_file: Optional[Incomplete] = None,
        credentialspec_registry: Optional[Incomplete] = None,
        selinux_disable: Optional[Incomplete] = None,
        selinux_user: Optional[Incomplete] = None,
        selinux_role: Optional[Incomplete] = None,
        selinux_type: Optional[Incomplete] = None,
        selinux_level: Optional[Incomplete] = None,
    ) -> None: ...

class NetworkAttachmentConfig(Dict[str, Any]):
    def __init__(
        self,
        target: str,
        aliases: Optional[Incomplete] = None,
        options: Optional[Incomplete] = None,
    ) -> None: ...
