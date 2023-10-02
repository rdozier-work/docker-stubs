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

class TaskTemplate(dict):
    def __init__(
        self,
        container_spec,
        resources: Incomplete | None = ...,
        restart_policy: Incomplete | None = ...,
        placement: Incomplete | None = ...,
        log_driver: Incomplete | None = ...,
        networks: Incomplete | None = ...,
        force_update: Incomplete | None = ...,
    ) -> None: ...
    @property
    def container_spec(self): ...
    @property
    def resources(self): ...
    @property
    def restart_policy(self): ...
    @property
    def placement(self): ...

class ContainerSpec(dict):
    def __init__(
        self,
        image,
        command: Incomplete | None = ...,
        args: Incomplete | None = ...,
        hostname: Incomplete | None = ...,
        env: Incomplete | None = ...,
        workdir: Incomplete | None = ...,
        user: Incomplete | None = ...,
        labels: Incomplete | None = ...,
        mounts: Incomplete | None = ...,
        stop_grace_period: Incomplete | None = ...,
        secrets: Incomplete | None = ...,
        tty: Incomplete | None = ...,
        groups: Incomplete | None = ...,
        open_stdin: Incomplete | None = ...,
        read_only: Incomplete | None = ...,
        stop_signal: Incomplete | None = ...,
        healthcheck: Incomplete | None = ...,
        hosts: Incomplete | None = ...,
        dns_config: Incomplete | None = ...,
        configs: Incomplete | None = ...,
        privileges: Incomplete | None = ...,
        isolation: Incomplete | None = ...,
        init: Incomplete | None = ...,
        cap_add: Incomplete | None = ...,
        cap_drop: Incomplete | None = ...,
        sysctls: Incomplete | None = ...,
    ) -> None: ...

class Mount(dict):
    def __init__(
        self,
        target,
        source,
        type: str = ...,
        read_only: bool = ...,
        consistency: Incomplete | None = ...,
        propagation: Incomplete | None = ...,
        no_copy: bool = ...,
        labels: Incomplete | None = ...,
        driver_config: Incomplete | None = ...,
        tmpfs_size: Incomplete | None = ...,
        tmpfs_mode: Incomplete | None = ...,
    ) -> None: ...
    @classmethod
    def parse_mount_string(cls, string): ...

class Resources(dict):
    def __init__(
        self,
        cpu_limit: Incomplete | None = ...,
        mem_limit: Incomplete | None = ...,
        cpu_reservation: Incomplete | None = ...,
        mem_reservation: Incomplete | None = ...,
        generic_resources: Incomplete | None = ...,
    ) -> None: ...

class UpdateConfig(dict):
    def __init__(
        self,
        parallelism: int = ...,
        delay: Incomplete | None = ...,
        failure_action: str = ...,
        monitor: Incomplete | None = ...,
        max_failure_ratio: Incomplete | None = ...,
        order: Incomplete | None = ...,
    ) -> None: ...

class RollbackConfig(UpdateConfig): ...

class RestartConditionTypesEnum:
    NONE: Incomplete
    ON_FAILURE: Incomplete
    ANY: Incomplete

class RestartPolicy(dict):
    condition_types = RestartConditionTypesEnum
    def __init__(
        self,
        condition=...,
        delay: int = ...,
        max_attempts: int = ...,
        window: int = ...,
    ) -> None: ...

class DriverConfig(dict):
    def __init__(self, name, options: Incomplete | None = ...) -> None: ...

class EndpointSpec(dict):
    def __init__(
        self, mode: Incomplete | None = ..., ports: Incomplete | None = ...
    ) -> None: ...

def convert_service_ports(ports): ...

class ServiceMode(dict):
    mode: Incomplete
    def __init__(
        self,
        mode,
        replicas: Incomplete | None = ...,
        concurrency: Incomplete | None = ...,
    ) -> None: ...
    @property
    def replicas(self): ...

class SecretReference(dict):
    def __init__(
        self,
        secret_id,
        secret_name,
        filename: Incomplete | None = ...,
        uid: Incomplete | None = ...,
        gid: Incomplete | None = ...,
        mode: int = ...,
    ) -> None: ...

class ConfigReference(dict):
    def __init__(
        self,
        config_id,
        config_name,
        filename: Incomplete | None = ...,
        uid: Incomplete | None = ...,
        gid: Incomplete | None = ...,
        mode: int = ...,
    ) -> None: ...

class Placement(dict):
    def __init__(
        self,
        constraints: Incomplete | None = ...,
        preferences: Incomplete | None = ...,
        platforms: Incomplete | None = ...,
        maxreplicas: Incomplete | None = ...,
    ) -> None: ...

class PlacementPreference(dict):
    def __init__(self, strategy, descriptor) -> None: ...

class DNSConfig(dict):
    def __init__(
        self,
        nameservers: Incomplete | None = ...,
        search: Incomplete | None = ...,
        options: Incomplete | None = ...,
    ) -> None: ...

class Privileges(dict):
    def __init__(
        self,
        credentialspec_file: Incomplete | None = ...,
        credentialspec_registry: Incomplete | None = ...,
        selinux_disable: Incomplete | None = ...,
        selinux_user: Incomplete | None = ...,
        selinux_role: Incomplete | None = ...,
        selinux_type: Incomplete | None = ...,
        selinux_level: Incomplete | None = ...,
    ) -> None: ...

class NetworkAttachmentConfig(dict):
    def __init__(
        self, target, aliases: Incomplete | None = ..., options: Incomplete | None = ...
    ) -> None: ...
