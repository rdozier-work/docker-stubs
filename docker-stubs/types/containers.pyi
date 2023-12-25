from typing import Any, Optional, NoReturn, Type
from .. import errors
from ..utils.utils import (
    convert_port_bindings,
    convert_tmpfs_mounts,
    convert_volume_binds,
    format_environment,
    format_extra_hosts,
    normalize_links,
    parse_bytes,
    parse_devices,
    split_command,
    version_gte,
    version_lt,
)
from .base import DictType
from .healthcheck import Healthcheck
from _typeshed import Incomplete

class LogConfigTypesEnum:
    JSON: str = "json-file"
    SYSLOG: str = "syslog"
    JOURNALD: str = "journald"
    GELF: str = "gelf"
    FLUENTD: str = "fluentd"
    NONE: str = "none"

class LogConfig(DictType):
    types = LogConfigTypesEnum
    def __init__(self, **kwargs: Any) -> None: ...
    @property
    def type(self) -> str: ...
    @property
    def config(self) -> dict[str, Any]: ...
    def set_config_value(self, key: str, value: Any) -> None: ...
    def unset_config(self, key: str) -> None: ...

class Ulimit(DictType):
    def __init__(self, **kwargs: Any) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def soft(self) -> int: ...
    @property
    def hard(self) -> int: ...

class DeviceRequest(DictType):
    def __init__(self, **kwargs: Any) -> None: ...
    @property
    def driver(self) -> str: ...
    @property
    def count(self) -> int: ...
    @property
    def device_ids(self) -> list[str]: ...
    @property
    def capabilities(self) -> list[str]: ...
    @property
    def options(self) -> dict[str, Any]: ...

class HostConfig(dict):
    def __init__(
        self,
        version: Any,
        binds: Any = None,
        port_bindings: Any = None,
        lxc_conf: Any = None,
        publish_all_ports: bool = False,
        links: Any = None,
        privileged: bool = False,
        dns: Any = None,
        dns_search: Any = None,
        volumes_from: Any = None,
        network_mode: Any = None,
        restart_policy: Any = None,
        cap_add: Any = None,
        cap_drop: Any = None,
        devices: Any = None,
        extra_hosts: Any = None,
        read_only: Any = None,
        pid_mode: Any = None,
        ipc_mode: Any = None,
        security_opt: Any = None,
        ulimits: Any = None,
        log_config: Any = None,
        mem_limit: Any = None,
        memswap_limit: Any = None,
        mem_reservation: Any = None,
        kernel_memory: Any = None,
        mem_swappiness: Any = None,
        cgroup_parent: Any = None,
        group_add: Any = None,
        cpu_quota: Any = None,
        cpu_period: Any = None,
        blkio_weight: Any = None,
        blkio_weight_device: Any = None,
        device_read_bps: Any = None,
        device_write_bps: Any = None,
        device_read_iops: Any = None,
        device_write_iops: Any = None,
        oom_kill_disable: bool = False,
        shm_size: Any = None,
        sysctls: Any = None,
        tmpfs: Any = None,
        oom_score_adj: Any = None,
        dns_opt: Any = None,
        cpu_shares: Any = None,
        cpuset_cpus: Any = None,
        userns_mode: Any = None,
        uts_mode: Any = None,
        pids_limit: Any = None,
        isolation: Any = None,
        auto_remove: bool = False,
        storage_opt: Any = None,
        init: Any = None,
        init_path: Any = None,
        volume_driver: Any = None,
        cpu_count: Any = None,
        cpu_percent: Any = None,
        nano_cpus: Any = None,
        cpuset_mems: Any = None,
        runtime: Any = None,
        mounts: Any = None,
        cpu_rt_period: Any = None,
        cpu_rt_runtime: Any = None,
        device_cgroup_rules: Any = None,
        device_requests: Any = None,
        cgroupns: Any = None,
    ) -> None: ...

def host_config_type_error(
    param: str, param_value: Any, expected: Type
) -> NoReturn: ...
def host_config_version_error(
    param: str, version: str, less_than: bool = True
) -> NoReturn: ...
def host_config_value_error(param: str, param_value: Any) -> NoReturn: ...
def host_config_incompatible_error(
    param: str, param_value: Any, incompatible_param: str
) -> NoReturn: ...

class ContainerConfig(dict):
    def __init__(
        self,
        version: str,
        image: str,
        command: str,
        hostname: Optional[str] = None,
        user: Optional[str] = None,
        detach: bool = False,
        stdin_open: bool = False,
        tty: bool = False,
        ports: Optional[dict[str, Any]] = None,
        environment: Optional[dict[str, str]] = None,
        volumes: Optional[dict[str, str]] = None,
        network_disabled: bool = False,
        entrypoint: Optional[str] = None,
        working_dir: Optional[str] = None,
        domainname: Optional[str] = None,
        host_config: Optional[HostConfig] = None,
        mac_address: Optional[str] = None,
        labels: Optional[dict[str, str]] = None,
        stop_signal: Optional[str] = None,
        networking_config: Optional[dict[str, Any]] = None,
        healthcheck: Optional[Healthcheck] = None,
        stop_timeout: Optional[int] = None,
        runtime: Optional[str] = None,
    ) -> None: ...
