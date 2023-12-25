from typing import Any, Optional
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

class TaskTemplate(dict[str, Any]):
    def __init__(
        self,
        container_spec: Any,
        resources: dict[str, Any] | None = None,
        restart_policy: dict[str, Any] | None = None,
        placement: dict[str, Any] | None = None,
        log_driver: dict[str, Any] | None = None,
        networks: list[dict[str, Any]] | None = None,
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

class ContainerSpec(dict[str, Any]):
    def __init__(
        self,
        image: str,
        command: list[str] | None = None,
        args: list[str] | None = None,
        hostname: str | None = None,
        env: dict[str, str] | None = None,
        workdir: str | None = None,
        user: str | None = None,
        labels: dict[str, str] | None = None,
        mounts: list[dict[str, Any]] | None = None,
        stop_grace_period: int | None = None,
        secrets: list[dict[str, Any]] | None = None,
        tty: bool | None = None,
        groups: list[str] | None = None,
        open_stdin: bool | None = None,
        read_only: bool | None = None,
        stop_signal: str | None = None,
        healthcheck: dict[str, Any] | None = None,
        hosts: dict[str, str] | None = None,
        dns_config: dict[str, Any] | None = None,
        configs: list[dict[str, Any]] | None = None,
        privileges: dict[str, Any] | None = None,
        isolation: str | None = None,
        init: bool | None = None,
        cap_add: list[str] | None = None,
        cap_drop: list[str] | None = None,
        sysctls: dict[str, str] | None = None,
    ) -> None: ...

class Mount(dict[str, Any]):
    def __init__(
        self,
        target: str,
        source: str,
        type: str = "bind",
        read_only: bool = False,
        consistency: str | None = None,
        propagation: str | None = None,
        no_copy: bool = False,
        labels: dict[str, str] | None = None,
        driver_config: dict[str, Any] | None = None,
        tmpfs_size: int | None = None,
        tmpfs_mode: int | None = None,
    ) -> None: ...
    @classmethod
    def parse_mount_string(cls, string): ...

class Resources(dict[str, Any]):
    def __init__(
        self,
        cpu_limit: int | None = None,
        mem_limit: int | None = None,
        cpu_reservation: int | None = None,
        mem_reservation: int | None = None,
        generic_resources: list[dict[str, Any]] | None = None,
    ) -> None: ...

class UpdateConfig(dict[str, Any]):
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

class RestartPolicy(dict[str, Any]):
    def __init__(
        self,
        condition: str = "any",
        delay: int = 5,
        max_attempts: int = 5,
        window: int = 5,
    ) -> None: ...

class DriverConfig(dict[str, Any]):
    def __init__(self, name: str, options: Optional[Incomplete] = None) -> None: ...

class EndpointSpec(dict[str, Any]):
    def __init__(
        self, mode: Optional[Incomplete] = None, ports: Optional[Incomplete] = None
    ) -> None: ...

class ServiceMode(dict[str, Any]):
    mode: Incomplete
    def __init__(
        self,
        mode: Any,
        replicas: Optional[Incomplete] = None,
        concurrency: Optional[Incomplete] = None,
    ) -> None: ...
    @property
    def replicas(self) -> Any: ...

class SecretReference(dict[str, Any]):
    def __init__(
        self,
        secret_id: str,
        secret_name: str,
        filename: Optional[Incomplete] = None,
        uid: Optional[Incomplete] = None,
        gid: Optional[Incomplete] = None,
        mode: int = 0,
    ) -> None: ...

class ConfigReference(dict[str, Any]):
    def __init__(
        self,
        config_id: str,
        config_name: str,
        filename: Optional[Incomplete] = None,
        uid: Optional[Incomplete] = None,
        gid: Optional[Incomplete] = None,
        mode: int = 0,
    ) -> None: ...

class Placement(dict[str, Any]):
    def __init__(
        self,
        constraints: Optional[Incomplete] = None,
        preferences: Optional[Incomplete] = None,
        platforms: Optional[Incomplete] = None,
        maxreplicas: Optional[Incomplete] = None,
    ) -> None: ...

class PlacementPreference(dict[str, Any]):
    def __init__(self, strategy: Any, descriptor: Any) -> None: ...

class DNSConfig(dict[str, Any]):
    def __init__(
        self,
        nameservers: Optional[Incomplete] = None,
        search: Optional[Incomplete] = None,
        options: Optional[Incomplete] = None,
    ) -> None: ...

class Privileges(dict[str, Any]):
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

class NetworkAttachmentConfig(dict[str, Any]):
    def __init__(
        self,
        target: str,
        aliases: Optional[Incomplete] = None,
        options: Optional[Incomplete] = None,
    ) -> None: ...
