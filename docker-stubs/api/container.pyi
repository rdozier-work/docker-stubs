from .. import errors as errors, utils as utils
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from ..types import (
    CancellableStream as CancellableStream,
    ContainerConfig as ContainerConfig,
    EndpointConfig as EndpointConfig,
    HostConfig as HostConfig,
    NetworkingConfig as NetworkingConfig,
)
from _typeshed import Incomplete

class ContainerApiMixin:
    def attach(
        self,
        container,
        stdout: bool = ...,
        stderr: bool = ...,
        stream: bool = ...,
        logs: bool = ...,
        demux: bool = ...,
    ): ...
    def attach_socket(
        self, container, params: Incomplete | None = ..., ws: bool = ...
    ): ...
    def commit(
        self,
        container,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        message: Incomplete | None = ...,
        author: Incomplete | None = ...,
        pause: bool = ...,
        changes: Incomplete | None = ...,
        conf: Incomplete | None = ...,
    ): ...
    def containers(
        self,
        quiet: bool = ...,
        all: bool = ...,
        trunc: bool = ...,
        latest: bool = ...,
        since: Incomplete | None = ...,
        before: Incomplete | None = ...,
        limit: int = ...,
        size: bool = ...,
        filters: Incomplete | None = ...,
    ): ...
    def create_container(
        self,
        image,
        command: Incomplete | None = ...,
        hostname: Incomplete | None = ...,
        user: Incomplete | None = ...,
        detach: bool = ...,
        stdin_open: bool = ...,
        tty: bool = ...,
        ports: Incomplete | None = ...,
        environment: Incomplete | None = ...,
        volumes: Incomplete | None = ...,
        network_disabled: bool = ...,
        name: Incomplete | None = ...,
        entrypoint: Incomplete | None = ...,
        working_dir: Incomplete | None = ...,
        domainname: Incomplete | None = ...,
        host_config: Incomplete | None = ...,
        mac_address: Incomplete | None = ...,
        labels: Incomplete | None = ...,
        stop_signal: Incomplete | None = ...,
        networking_config: Incomplete | None = ...,
        healthcheck: Incomplete | None = ...,
        stop_timeout: Incomplete | None = ...,
        runtime: Incomplete | None = ...,
        use_config_proxy: bool = ...,
        platform: Incomplete | None = ...,
    ): ...
    def create_container_config(self, *args, **kwargs): ...
    def create_container_from_config(
        self, config, name: Incomplete | None = ..., platform: Incomplete | None = ...
    ): ...
    def create_host_config(self, *args, **kwargs): ...
    def create_networking_config(self, *args, **kwargs): ...
    def create_endpoint_config(self, *args, **kwargs): ...
    def diff(self, container): ...
    def export(self, container, chunk_size=...): ...
    def get_archive(
        self, container, path, chunk_size=..., encode_stream: bool = ...
    ): ...
    def inspect_container(self, container): ...
    def kill(self, container, signal: Incomplete | None = ...) -> None: ...
    def logs(
        self,
        container,
        stdout: bool = ...,
        stderr: bool = ...,
        stream: bool = ...,
        timestamps: bool = ...,
        tail: str = ...,
        since: Incomplete | None = ...,
        follow: Incomplete | None = ...,
        until: Incomplete | None = ...,
    ): ...
    def pause(self, container) -> None: ...
    def port(self, container, private_port): ...
    def put_archive(self, container, path, data): ...
    def prune_containers(self, filters: Incomplete | None = ...): ...
    def remove_container(
        self, container, v: bool = ..., link: bool = ..., force: bool = ...
    ) -> None: ...
    def rename(self, container, name) -> None: ...
    def resize(self, container, height, width) -> None: ...
    def restart(self, container, timeout: int = ...) -> None: ...
    def start(self, container, *args, **kwargs) -> None: ...
    def stats(
        self,
        container,
        decode: Incomplete | None = ...,
        stream: bool = ...,
        one_shot: Incomplete | None = ...,
    ): ...
    def stop(self, container, timeout: Incomplete | None = ...) -> None: ...
    def top(self, container, ps_args: Incomplete | None = ...): ...
    def unpause(self, container) -> None: ...
    def update_container(
        self,
        container,
        blkio_weight: Incomplete | None = ...,
        cpu_period: Incomplete | None = ...,
        cpu_quota: Incomplete | None = ...,
        cpu_shares: Incomplete | None = ...,
        cpuset_cpus: Incomplete | None = ...,
        cpuset_mems: Incomplete | None = ...,
        mem_limit: Incomplete | None = ...,
        mem_reservation: Incomplete | None = ...,
        memswap_limit: Incomplete | None = ...,
        kernel_memory: Incomplete | None = ...,
        restart_policy: Incomplete | None = ...,
    ): ...
    def wait(
        self,
        container,
        timeout: Incomplete | None = ...,
        condition: Incomplete | None = ...,
    ): ...
