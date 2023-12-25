from typing import TypedDict, Optional, Union
from .. import errors as errors, utils as utils
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from ..types import (
    CancellableStream as CancellableStream,
    ContainerConfig as ContainerConfig,
    EndpointConfig as EndpointConfig,
    HostConfig as HostConfig,
    NetworkingConfig as NetworkingConfig,
)
from ..types.base import Command, PathStr, MacAddress, Signal

class CreateContainerReturndict(TypedDict):
    Id: str
    Warnings: list[str]

class ContainerApiMixin:
    def attach(
        self,
        container: str,
        stdout: bool = True,
        stderr: bool = True,
        stream: bool = True,
        logs: bool = True,
        demux: bool = False,
    ) -> CancellableStream: ...
    def attach_socket(
        self, container: str, params: Optional[dict[str, str]] = None, ws: bool = False
    ) -> CancellableStream: ...
    def commit(
        self,
        container: str,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        message: Optional[str] = None,
        author: Optional[str] = None,
        pause: bool = True,
        changes: Optional[list[str]] = None,
        conf: Optional[ContainerConfig] = None,
    ) -> dict[str, str]: ...
    def containers(
        self,
        quiet: bool = False,
        all: bool = False,
        trunc: bool = False,
        latest: bool = False,
        since: Optional[str] = None,
        before: Optional[str] = None,
        limit: int = -1,
        size: bool = False,
        filters: Optional[dict[str, str]] = None,
    ) -> list[dict[str, str]]: ...
    def create_container(
        self,
        image: str,
        command: Optional[Command] = None,
        hostname: Optional[str] = None,
        user: Optional[Union[str, int]] = None,
        detach: bool = False,
        stdin_open: bool = False,
        tty: bool = False,
        ports: Optional[list[int]] = None,
        environment: Optional[Union[list[str], dict[str, str]]] = None,
        volumes: Optional[Union[str, list[PathStr]]] = None,
        network_disabled: bool = False,
        name: Optional[str] = None,
        entrypoint: Optional[Command] = None,
        working_dir: Optional[PathStr] = None,
        domainname: Optional[str] = None,
        host_config: Optional[dict] = None,
        mac_address: Optional[MacAddress] = None,
        labels: Optional[Union[dict[str, str], list[str]]] = None,
        stop_signal: Optional[Signal] = None,
        networking_config: Optional[dict] = None,
        healthcheck: Optional[dict] = None,
        stop_timeout: Optional[int] = None,
        runtime: Optional[str] = None,
        use_config_proxy: bool = False,
        platform: Optional[str] = None,
    ) -> CreateContainerReturndict: ...
    def create_container_config(
        self, *args: str, **kwargs: dict[str, str]
    ) -> dict[str, str]: ...
    def create_container_from_config(
        self,
        config: dict[str, str],
        name: Optional[str] = None,
        platform: Optional[str] = None,
    ) -> dict[str, str]: ...
    def create_host_config(
        self, *args: str, **kwargs: dict[str, str]
    ) -> HostConfig: ...
    def create_networking_config(
        self, *args: str, **kwargs: dict[str, str]
    ) -> NetworkingConfig: ...
    def create_endpoint_config(
        self, *args: str, **kwargs: dict[str, str]
    ) -> EndpointConfig: ...
    def diff(self, container: str) -> list[dict[str, str]]: ...
    def export(
        self, container: str, chunk_size: int = DEFAULT_DATA_CHUNK_SIZE
    ) -> CancellableStream: ...
    def get_archive(
        self,
        container: str,
        path: PathStr,
        chunk_size: int = DEFAULT_DATA_CHUNK_SIZE,
        encode_stream: bool = False,
    ) -> CancellableStream: ...
    def inspect_container(self, container: str) -> dict[str, str]: ...
    def kill(self, container: str, signal: Optional[Signal] = None) -> None: ...
    def logs(
        self,
        container: str,
        stdout: bool = True,
        stderr: bool = True,
        stream: bool = True,
        timestamps: bool = False,
        tail: str = "all",
        since: Optional[int] = None,
        follow: Optional[bool] = None,
        until: Optional[int] = None,
    ) -> CancellableStream: ...
    def pause(self, container: str) -> None: ...
    def port(self, container: str, private_port: int) -> dict[str, str]: ...
    def put_archive(
        self, container: str, path: PathStr, data: bytes
    ) -> dict[str, str]: ...
    def prune_containers(
        self, filters: Optional[dict[str, str]] = None
    ) -> dict[str, str]: ...
    def remove_container(
        self, container: str, v: bool = False, link: bool = False, force: bool = False
    ) -> None: ...
    def rename(self, container: str, name: str) -> None: ...
    def resize(self, container: str, height: int, width: int) -> None: ...
    def restart(self, container: str, timeout: int = 10) -> None: ...
    def start(self, container: str, *args: str, **kwargs: dict[str, str]) -> None: ...
