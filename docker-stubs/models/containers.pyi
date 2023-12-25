from typing import Optional, Union, List, Dict, Any
from .. import auth as auth, errors as errors, utils as utils
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from ..types import (
    HostConfig as HostConfig,
    DeviceRequest,
    LogConfig,
    Mount,
    RestartPolicy,
    Ulimit,
    CancellableStream,
)
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
    def attach(self, **kwargs: Any): ...
    def attach_socket(self, **kwargs: Any): ...
    def commit(
        self, repository: Optional[str] = None, tag: Optional[str] = None, **kwargs: Any
    ): ...
    def diff(self): ...
    def exec_run(
        self,
        cmd: Union[str, List[str]],
        stdout: bool = True,
        stderr: bool = True,
        stdin: bool = False,
        tty: bool = False,
        privileged: bool = False,
        user: str = "",
        detach: bool = False,
        stream: bool = False,
        socket: bool = False,
        environment: Optional[Union[Dict[str, str], List[str]]] = None,
        workdir: Optional[str] = None,
        demux: bool = False,
    ) -> Any: ...
    def export(self, chunk_size: int = DEFAULT_DATA_CHUNK_SIZE) -> Any: ...
    def get_archive(
        self,
        path: str,
        chunk_size: int = DEFAULT_DATA_CHUNK_SIZE,
        encode_stream: bool = False,
    ) -> Any: ...
    def kill(self, signal: Optional[str] = None): ...
    def logs(self, **kwargs: Any): ...
    def pause(self): ...
    def put_archive(self, path: str, data: Any): ...
    def remove(self, **kwargs: Any): ...
    def rename(self, name: str): ...
    def resize(self, height: int, width: int): ...
    def restart(self, **kwargs: Any): ...
    def start(self, **kwargs: Any): ...
    def stats(self, **kwargs: Any): ...
    def stop(self, **kwargs: Any): ...
    def top(self, **kwargs: Any): ...
    def unpause(self): ...
    def update(self, **kwargs: Any): ...
    def wait(self, **kwargs: Any): ...

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
    environment: dict | list
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
    ports: Dict[str, Union[int, str]]
    volumes: Dict[str, str]
    network: Dict[str, Union[int, str]]
    network_driver_opt: Optional[Dict[str, Union[int, str]]]

class ContainerCollection(_Collection):
    model = Container
    def run(
        self,
        image: Union[str, Image],
        command: Optional[Union[str, List[str]]] = None,
        stdout: bool = True,
        stderr: bool = True,
        remove: bool = False,
        **kwargs: Unpack[ContainerCollectionRunKwargs]
    ) -> Union[Container, bytes, CancellableStream]: ...
    def create(
        self,
        image: Union[str, Image],
        command: Optional[Union[str, List[str]]] = None,
        **kwargs: Unpack[ContainerCollectionCreateKwargs]
    ) -> Container: ...
    def get(self, container_id: str) -> Container: ...
    def list(
        self,
        all: bool = False,
        before: Optional[str] = None,
        filters: Optional[Dict[str, Union[str, List[str]]]] = None,
        limit: int = -1,
        since: Optional[str] = None,
        sparse: bool = False,
        ignore_removed: bool = False,
    ) -> List[Container]: ...
    def prune(
        self, filters: Optional[Dict[str, Union[str, List[str]]]] = None
    ) -> Dict[str, Any]: ...

class ExecResult(NamedTuple):
    exit_code: int
    output: Union[str, bytes]
