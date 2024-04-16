from collections.abc import Generator
from typing import AnyStr
from typing import TypedDict

from .. import auth as auth, constants as constants, errors as errors, utils as utils
from _typeshed import Incomplete

from ..types.io import ResponseResult
from ..types.io import PathType


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
        fileobj: Incomplete | None = ...,
        nocache: bool = ...,
        rm: bool = ...,
        timeout: int | None = ...,
        custom_context: bool = ...,
        encoding: str | None = ...,
        pull: bool = ...,
        forcerm: bool = ...,
        dockerfile: str | None = ...,
        container_limits: dict | None = ...,
        decode: bool = ...,
        buildargs: dict | None = ...,
        gzip: bool = ...,
        shmsize: int | None = ...,
        labels: dict | None = ...,
        cache_from: list | None = ...,
        target: str | None = ...,
        network_mode: str | None = ...,
        squash: bool | None = ...,
        extra_hosts: dict | None = ...,
        platform: str | None = ...,
        isolation: str | None = ...,
        use_config_proxy: bool = ...,
    ) -> Generator[ResponseResult, None, None]: ...
    def prune_builds(
        self,
        filters: dict | None = ...,
        keep_storage: int | None = ...,
        all: bool | None = ...,
    ): ...

def process_dockerfile(dockerfile: PathType, path: PathType) -> tuple[PathType | None, AnyStr | None]: ...
