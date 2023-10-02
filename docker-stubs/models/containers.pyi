from ..api import APIClient as APIClient
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from ..errors import (
    ContainerError as ContainerError,
    DockerException as DockerException,
    ImageNotFound as ImageNotFound,
    NotFound as NotFound,
    create_unexpected_kwargs_error as create_unexpected_kwargs_error,
)
from ..types import HostConfig as HostConfig, DeviceRequest, LogConfig, Mount, RestartPolicy, Ulimit, CancellableStream
from ..types.base import Command, Versioned, PathStr, MacAddress, Port
from ..utils import version_gte as version_gte
from .images import Image as Image
from .resource import Collection as _Collection, Model as Model
from _typeshed import Incomplete
from typing import NamedTuple, Literal, Dict, Collection, Unpack, TypedDict

ContainerStatus = Literal[
    "created", "running", "paused", "restarting", "removing", "exited", "dead"
]

class Container(Model):
    @property
    def name(self) -> str: ...
    @property
    def image(self) -> Image: ...
    @property
    def labels(self) -> dict: ...
    @property
    def status(self) -> ContainerStatus: ...
    @property
    def ports(self) -> Dict[str, Collection[str]]: ...
    def attach(self, **kwargs): ...
    def attach_socket(self, **kwargs): ...
    def commit(
        self,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        **kwargs
    ): ...
    def diff(self): ...
    def exec_run(
        self,
        cmd,
        stdout: bool = ...,
        stderr: bool = ...,
        stdin: bool = ...,
        tty: bool = ...,
        privileged: bool = ...,
        user: str = ...,
        detach: bool = ...,
        stream: bool = ...,
        socket: bool = ...,
        environment: Incomplete | None = ...,
        workdir: Incomplete | None = ...,
        demux: bool = ...,
    ): ...
    def export(self, chunk_size=...): ...
    def get_archive(self, path, chunk_size=..., encode_stream: bool = ...): ...
    def kill(self, signal: Incomplete | None = ...): ...
    def logs(self, **kwargs): ...
    def pause(self): ...
    def put_archive(self, path, data): ...
    def remove(self, **kwargs): ...
    def rename(self, name): ...
    def resize(self, height, width): ...
    def restart(self, **kwargs): ...
    def start(self, **kwargs): ...
    def stats(self, **kwargs): ...
    def stop(self, **kwargs): ...
    def top(self, **kwargs): ...
    def unpause(self): ...
    def update(self, **kwargs): ...
    def wait(self, **kwargs): ...


class BlockIOWeightDevice(TypedDict):
    Path: PathStr
    Weight: float


class HealthCheckDict(TypedDict):
    test: list[str] | str
    interval: int
    timeout: int
    retries: int
    start_period: int


class VolumeMappingDict(TypedDict):
    bind: PathStr
    mode: Literal["rw", "ro"]


class ContainerCollectionRunKwargs(Versioned, total=False):
    image: str
    command: Command
    auto_remove: bool
    blkio_weight_device: BlockIOWeightDevice
    blkio_weight: int
    cap_add: list[str]
    cap_drop: list[str]
    cgroup_parent: str
    cgroupns: Literal["private", "host"]
    cpu_count: int
    cpu_percent: int
    cpu_period: int
    cpu_quota: int
    cpu_rt_period: int
    cpu_rt_runtime: int
    cpu_shares: int
    cpuset_cpus: str
    cpuset_mems: str
    detach: bool
    device_cgroup_rules: list
    device_read_bps: int
    device_read_iops: int
    device_write_bps: int
    device_write_iops: int
    devices: list[str]
    device_requests: list[DeviceRequest]
    dns: list
    dns_opt: list
    dns_search: list
    domainname: str | list
    entrypoint: str | list
    environment: dict| list
    extra_hosts: dict[str, str]
    group_add: list[str]
    healthcheck: HealthCheckDict
    hostname: str
    init: bool
    init_path: PathStr
    ipc_mode: str
    isolation: str | None
    kernel_memory: int | str
    labels: dict[str, str] | list[str]
    links: dict[str, str] | None
    log_config: LogConfig
    lxc_conf: dict
    mac_address: MacAddress
    mem_limit: int | str
    mem_reservation: int | str
    mem_swappiness: int
    memswap_limit: str | int
    mounts: list[Mount]
    name: str
    nano_cpus: int
    network: str
    network_disabled: bool
    network_mode: str | Literal["bridge", "none", "host"]
    network_driver_opt: dict | None
    oom_kill_disable: bool
    oom_score_adj: int
    pid_mode: str
    pids_limit: int
    platform: str
    ports: dict[Port, Port | tuple[str, Port] | list[int] | None]
    privileged: bool
    publish_all_ports: bool
    read_only: bool
    remove: bool
    restart_policy: dict
    runtime: str
    security_opt: list[str]
    shm_size: str | int
    stdin_open: bool
    stdout: bool
    stderr: bool
    stop_signal: str
    storage_opt: dict
    stream: bool
    sysctls: dict
    tmpfs: dict
    tty: bool
    ulimits: list[Ulimit]
    use_config_proxy: bool
    user: str | int
    userns_mode: str
    uts_mode: str
    volume_driver: str
    volumes: VolumeMappingDict | list[str]
    volumes_from: list[str]
    working_dir: str

class ContainerCollectionCreateKwargs(Versioned, total=False):
    image: str
    command: Command
    ports: dict
    volumes: dict
    network: dict
    network_driver_opt: Incomplete | None


class ContainerCollection(_Collection):
    model = Container
    def run(
        self,
        image: str | Image,
        command: Command | None = ...,
        stdout: bool = ...,
        stderr: bool = ...,
        remove: bool = ...,
        **kwargs: Unpack[ContainerCollectionRunKwargs]
    ) -> Container | bytes | CancellableStream: ...
    def create(self,
               image: str | Image,
               command: Command | None = ...,
               **kwargs: Unpack[ContainerCollectionCreateKwargs]) -> Container: ...
    def get(self, container_id: str) -> Container: ...
    def list(
        self,
        all: bool = ...,
        before: Incomplete | None = ...,
        filters: Incomplete | None = ...,
        limit: int = ...,
        since: Incomplete | None = ...,
        sparse: bool = ...,
        ignore_removed: bool = ...,
    ): ...
    def prune(self, filters: Incomplete | None = ...): ...

RUN_CREATE_KWARGS: Incomplete
RUN_HOST_CONFIG_KWARGS: Incomplete

class ExecResult(NamedTuple):
    exit_code: Incomplete
    output: Incomplete
