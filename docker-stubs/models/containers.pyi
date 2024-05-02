from socket import socket
from typing import (
    Any,
    Generator,
    Iterator,
    Literal,
    Mapping,
    NamedTuple,
    TypedDict,
    overload,
)

from ..types.containers import DeviceRequest, LogConfig, Ulimit

from ..types.services import Mount

from ..types.daemon import CancellableStream

from ..api import APIClient as APIClient
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from ..errors import (
    ContainerError as ContainerError,
    DockerException as DockerException,
    ImageNotFound as ImageNotFound,
    NotFound as NotFound,
    create_unexpected_kwargs_error as create_unexpected_kwargs_error,
)
from ..types import HostConfig as HostConfig, NetworkingConfig as NetworkingConfig
from ..types.base import _Command, _Port, _Versioned
from ..types._io import Socket
from ..utils import version_gte as version_gte
from .images import Image as Image
from .resource import Collection, Model
from _typeshed import Incomplete
from typing_extensions import NotRequired, Unpack

class Container(Model):
    @property
    def name(self) -> str: ...
    @property
    def image(self) -> Image | None: ...
    @property
    def labels(self) -> dict[Incomplete, Incomplete]: ...
    @property
    def status(self) -> str: ...
    @property
    def health(self) -> str: ...
    @property
    def ports(self) -> dict[Incomplete, Incomplete]: ...
    def attach(self, **kwargs: Incomplete) -> str | Generator[str, None, None]: ...
    def attach_socket(self, **kwargs: Incomplete) -> Socket: ...
    def commit(
        self, repository: str | None = ..., tag: str | None = ..., **kwargs: Incomplete
    ) -> str: ...
    def diff(self) -> list[dict[Incomplete, Incomplete]]: ...
    @overload
    def exec_run(
        self,
        cmd: tuple[str, ...] | list[str],
        demux: Literal[True],
        stdout: bool = ...,
        stderr: bool = ...,
        stdin: bool = ...,
        tty: bool = ...,
        privileged: bool = ...,
        user: str = ...,
        detach: bool = ...,
        environment: Incomplete | None = ...,
        workdir: Incomplete | None = ...,
    ) -> tuple[int, tuple[bytes, bytes | None]]: ...
    @overload
    def exec_run(
        self,
        cmd: tuple[str, ...] | list[str],
        stdout: bool = ...,
        stderr: bool = ...,
        stdin: bool = ...,
        tty: bool = ...,
        privileged: bool = ...,
        user: str = ...,
        detach: bool = ...,
        environment: Incomplete | None = ...,
        workdir: Incomplete | None = ...,
    ) -> tuple[int, bytes]: ...
    @overload
    def exec_run(
        self,
        cmd: tuple[str, ...] | list[str],
        stream: Literal[True],
        stdout: bool = ...,
        stderr: bool = ...,
        stdin: bool = ...,
        tty: bool = ...,
        privileged: bool = ...,
        user: str = ...,
        detach: bool = ...,
        environment: Incomplete | None = ...,
        workdir: Incomplete | None = ...,
    ) -> tuple[int, Iterator[bytes]]: ...
    @overload
    def exec_run(
        self,
        cmd: tuple[str, ...] | list[str],
        socket: Literal[True],
        stdout: bool = ...,
        stderr: bool = ...,
        stdin: bool = ...,
        tty: bool = ...,
        privileged: bool = ...,
        user: str = ...,
        detach: bool = ...,
        environment: Incomplete | None = ...,
        workdir: Incomplete | None = ...,
    ) -> tuple[int, socket]: ...
    def export(self, chunk_size: int = ...) -> Iterator[Incomplete]: ...
    def get_archive(
        self, path: str, chunk_size: int = ..., encode_stream: bool = ...
    ) -> tuple[Iterator[Incomplete], dict[Incomplete, Incomplete]]: ...
    def kill(self, signal: str | int | None = ...) -> None: ...
    def logs(self, **kwargs: Incomplete) -> Iterator[str] | str: ...
    def pause(self) -> None: ...
    def put_archive(self, path: str, data: bytes | Iterator[Incomplete]) -> bool: ...
    def remove(self, v: bool = ..., link: bool = ..., force: bool = ...) -> None: ...
    def rename(self, name: str) -> None: ...
    def resize(self, height: int, width: int) -> None: ...
    def restart(self, *, timeout: int = ...) -> None: ...
    def start(self, **kwargs: Incomplete) -> None: ...
    def stats(self, **kwargs: Incomplete) -> Incomplete: ...
    def stop(self, timeout: int | None = ...) -> None: ...
    def top(self, **kwargs: Incomplete) -> str: ...
    def unpause(self) -> None: ...
    def update(self, **kwargs: Incomplete) -> dict[Incomplete, Incomplete]: ...
    def wait(self, **kwargs: Incomplete) -> dict[Incomplete, Incomplete]: ...

class _BlockIOWeightDevice(TypedDict):
    Path: str
    Weight: float

class _HealthCheckDict(TypedDict):
    test: list[str] | str
    interval: int
    timeout: int
    retries: int
    start_period: int

class _VolumeMappingDict(TypedDict):
    bind: str
    mode: Literal["ro", "rw"]

class _ContainerCollectionRunKwargs(TypedDict):
    auto_remove: NotRequired[bool]
    blkio_weight_device: NotRequired[_BlockIOWeightDevice]
    blkio_weight: NotRequired[int]
    cap_add: NotRequired[list[str]]
    cap_drop: NotRequired[list[str]]
    cgroup_parent: NotRequired[str]
    cgroupns: NotRequired[Literal["private", "host"]]
    cpu_count: NotRequired[int]
    cpu_percent: NotRequired[int]
    cpu_period: NotRequired[int]
    cpu_quota: NotRequired[int]
    cpu_rt_period: NotRequired[int]
    cpu_rt_runtime: NotRequired[int]
    cpu_shares: NotRequired[int]
    cpuset_cpus: NotRequired[str]
    cpuset_mems: NotRequired[str]
    device_cgroup_rules: NotRequired[list[Incomplete]]
    device_read_bps: NotRequired[int]
    device_read_iops: NotRequired[int]
    device_write_bps: NotRequired[int]
    device_write_iops: NotRequired[int]
    devices: NotRequired[list[str]]
    device_requests: NotRequired[list[DeviceRequest]]
    dns: NotRequired[list[Incomplete]]
    dns_opt: NotRequired[list[Incomplete]]
    dns_search: NotRequired[list[Incomplete]]
    domainname: NotRequired[str | list[Incomplete]]
    entrypoint: NotRequired[str | list[Incomplete]]
    environment: NotRequired[Mapping[Incomplete, Incomplete] | list[Incomplete]]
    extra_hosts: NotRequired[dict[str, str]]
    group_add: NotRequired[list[str]]
    healthcheck: NotRequired[_HealthCheckDict]
    hostname: NotRequired[str]
    init: NotRequired[bool]
    init_path: NotRequired[str]
    ipc_mode: NotRequired[str]
    isolation: NotRequired[str | None]
    kernel_memory: NotRequired[int | str]
    labels: NotRequired[dict[str, str] | list[str]]
    links: NotRequired[dict[str, str] | None]
    log_config: NotRequired[LogConfig]
    lxc_conf: NotRequired[dict[Incomplete, Incomplete]]
    mac_address: NotRequired[str]
    mem_limit: NotRequired[int | str]
    mem_reservation: NotRequired[int | str]
    mem_swappiness: NotRequired[int]
    memswap_limit: NotRequired[str | int]
    mounts: NotRequired[list[Mount]]
    name: NotRequired[str]
    nano_cpus: NotRequired[int]
    network: NotRequired[str]
    network_disabled: NotRequired[bool]
    network_mode: NotRequired[Literal["bridge", "none", "host"]]
    network_driver_opt: NotRequired[dict[Incomplete, Incomplete] | None]
    oom_kill_disable: NotRequired[bool]
    oom_score_adj: NotRequired[int]
    pid_mode: NotRequired[str]
    pids_limit: NotRequired[int]
    platform: NotRequired[str]
    ports: NotRequired[dict[_Port, _Port | tuple[str, _Port] | list[int] | None]]
    privileged: NotRequired[bool]
    publish_all_ports: NotRequired[bool]
    read_only: NotRequired[bool]
    restart_policy: NotRequired[dict[Incomplete, Incomplete]]
    runtime: NotRequired[str]
    security_opt: NotRequired[list[str]]
    shm_size: NotRequired[str | int]
    stdin_open: NotRequired[bool]
    stop_signal: NotRequired[str]
    storage_opt: NotRequired[dict[Incomplete, Incomplete]]
    sysctls: NotRequired[dict[Incomplete, Incomplete]]
    tmpfs: NotRequired[dict[Incomplete, Incomplete]]
    tty: NotRequired[bool]
    ulimits: NotRequired[list[Ulimit]]
    use_config_proxy: NotRequired[bool]
    user: NotRequired[str | int]
    userns_mode: NotRequired[str]
    uts_mode: NotRequired[str]
    volume_driver: NotRequired[str]
    volumes: NotRequired[Mapping[str, _VolumeMappingDict] | list[str]]
    volumes_from: NotRequired[list[str]]
    working_dir: NotRequired[str]

class _ContainerCollectionCreateKwargs(_Versioned, total=False):
    image: NotRequired[str]
    command: NotRequired[_Command]
    ports: NotRequired[dict[Incomplete, Incomplete]]
    volumes: NotRequired[Any]
    network: NotRequired[dict[Incomplete, Incomplete]]
    network_driver_opt: NotRequired[Incomplete | None]

class ContainerCollection(Collection):
    model = Container
    @overload
    def run(
        self,
        image: str | Image,
        detach: Literal[True],
        command: _Command | None = ...,
        stdout: bool = ...,
        stderr: bool = ...,
        remove: bool = ...,
        **kwargs: Unpack[_ContainerCollectionRunKwargs]
    ) -> Container: ...
    @overload
    def run(
        self,
        image: str | Image,
        stream: Literal[True],
        command: _Command | None = ...,
        stdout: bool = ...,
        stderr: bool = ...,
        remove: bool = ...,
        **kwargs: Unpack[_ContainerCollectionRunKwargs]
    ) -> CancellableStream: ...
    @overload
    def run(
        self,
        image: str | Image,
        command: _Command | None = ...,
        stdout: bool = ...,
        stderr: bool = ...,
        remove: bool = ...,
        **kwargs: Unpack[_ContainerCollectionRunKwargs]
    ) -> bytes: ...
    def create(  # type: ignore[override]
        self, image: str | Image, command: Incomplete | None = ..., **kwargs: Incomplete
    ) -> Container: ...
    def get(self, container_id: str) -> Container: ...  # type: ignore[override]
    def list(  # type: ignore[override]
        self,
        all: bool = ...,
        before: str | None = ...,
        filters: dict[Incomplete, Incomplete] | None = ...,
        limit: int = ...,
        since: str | None = ...,
        sparse: bool = ...,
        ignore_removed: bool = ...,
    ) -> list[Container]: ...
    def prune(
        self, filters: Incomplete | None = ...
    ) -> dict[Incomplete, Incomplete]: ...

RUN_CREATE_KWARGS: list[str]
RUN_HOST_CONFIG_KWARGS: list[str]

class ExecResult(NamedTuple):
    exit_code: Any
    output: Any
