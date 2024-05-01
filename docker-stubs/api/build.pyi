from typing import AnyStr, BinaryIO, Iterator
from typing import TypedDict

from .. import auth as auth, constants as constants, errors as errors, utils as utils
from _typeshed import Incomplete

from ..types._io import PathType, ResponseResult

class ContainerLimitsDict(TypedDict, total=False):
    memory: int
    memswap: int
    cpushares: int
    cpusetcpus: str

class BuildApiMixin:
    def build(
        self,
        path: str | None = ...,
        tag: str | None = ...,
        quiet: bool = ...,
        fileobj: BinaryIO | None = ...,
        nocache: bool = ...,
        rm: bool = ...,
        timeout: int | None = ...,
        custom_context: bool = ...,
        encoding: str | None = ...,
        pull: bool = ...,
        forcerm: bool = ...,
        dockerfile: str | None = ...,
        container_limits: dict[Incomplete, Incomplete] | None = ...,
        decode: bool = ...,
        buildargs: dict[Incomplete, Incomplete] | None = ...,
        gzip: bool = ...,
        shmsize: int | None = ...,
        labels: dict[Incomplete, Incomplete] | None = ...,
        cache_from: list[Incomplete] | None = ...,
        target: str | None = ...,
        network_mode: str | None = ...,
        squash: bool | None = ...,
        extra_hosts: dict[Incomplete, Incomplete] | None = ...,
        platform: str | None = ...,
        isolation: str | None = ...,
        use_config_proxy: bool = ...,
    ) -> Iterator[ResponseResult]: ...
    def prune_builds(
        self,
        filters: dict[Incomplete, Incomplete] | None = ...,
        keep_storage: int | None = ...,
        all: bool | None = ...,
    ) -> dict[Incomplete, Incomplete]: ...

def process_dockerfile(
    dockerfile: PathType[str], path: PathType[str]
) -> tuple[PathType[str] | None, AnyStr | None]: ...
