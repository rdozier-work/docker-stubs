from typing import BinaryIO, Iterator, List, Mapping, TypedDict, Unpack
from typing_extensions import NotRequired

from ..api import APIClient as APIClient
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from ..errors import (
    BuildError as BuildError,
    ImageLoadError as ImageLoadError,
    InvalidArgument as InvalidArgument,
)
from ..types._io import Json
from ..types._io import ResponseResult
from ..types.misc_types import TrueOnSuccess
from ..utils import parse_repository_tag as parse_repository_tag
from ..utils.json_stream import json_stream as json_stream
from .resource import Collection as Collection, Model as Model
from _typeshed import Incomplete

class Image(Model):
    @property
    def labels(self) -> dict[Incomplete, Incomplete]: ...
    @property
    def short_id(self) -> str: ...
    @property
    def tags(self) -> list[str]: ...
    def history(self) -> str: ...
    def remove(self, force: bool = ..., noprune: bool = ...) -> Json: ...
    def save(
        self, chunk_size: int = ..., named: bool = ...
    ) -> Iterator[ResponseResult]: ...
    def tag(
        self, repository: str, tag: str | None = ..., **kwargs: Incomplete
    ) -> TrueOnSuccess: ...

class RegistryData(Model):
    image_name: Incomplete
    def __init__(
        self, image_name: str, *args: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    @property
    def id(self) -> str: ...
    @property
    def short_id(self) -> str: ...
    def pull(self, platform: str | None = ...) -> Image: ...
    def has_platform(self, platform: str | dict[Incomplete, Incomplete]) -> bool: ...
    attrs: Incomplete
    def reload(self) -> None: ...

class ContainerLimitDict(TypedDict):
    cpusetcpus: NotRequired[str]
    cpushares: NotRequired[int]
    memory: NotRequired[int]
    memswap: NotRequired[int]

class ImageCollectionBuildKwargs(TypedDict):
    buildargs: NotRequired[Mapping[str, str | None]]
    cache_from: NotRequired[list[str | Image]]
    container_limits: NotRequired[ContainerLimitDict]
    custom_context: NotRequired[bool]
    dockerfile: NotRequired[str]
    extra_hosts: NotRequired[Mapping[str, str]]
    fileobj: NotRequired[BinaryIO]
    forcerm: NotRequired[bool]
    isolation: NotRequired[str | None]
    labels: NotRequired[Mapping[str, str]]
    network_mode: NotRequired[str]
    nocache: NotRequired[bool]
    path: NotRequired[str]
    platform: NotRequired[str]
    pull: NotRequired[bool]
    quiet: NotRequired[bool]
    rm: NotRequired[bool]
    shmsize: NotRequired[int]
    squash: NotRequired[bool]
    tag: NotRequired[str]
    target: NotRequired[str]
    timeout: NotRequired[int]
    use_config_proxy: NotRequired[bool]

class ListFiltersDict(TypedDict):
    dangling: NotRequired[bool]
    label: NotRequired[str | list[str]]

class ImageCollection(Collection):
    model = Image
    def build(
        self, **kwargs: Unpack[ImageCollectionBuildKwargs]
    ) -> tuple[Image, Iterator[Mapping[str, Incomplete]]]: ...
    def get(self, name: str) -> Image: ...  # type: ignore[override]
    def get_registry_data(
        self, name: str, auth_config: dict[Incomplete, Incomplete] | None = ...
    ) -> RegistryData: ...
    def list(  # type: ignore[override]
        self,
        name: str | None = ...,
        all: bool = ...,
        filters: dict[Incomplete, Incomplete] | None = ...,
    ) -> list[Image]: ...
    def load(self, data: Incomplete) -> List[Image]: ...
    def pull(
        self,
        repository: str,
        tag: str | None = ...,
        all_tags: bool = ...,
        **kwargs: Incomplete
    ) -> Image | List[Image]: ...
    def push(
        self, repository: str, tag: str | None = ..., **kwargs: Incomplete
    ) -> Iterator[ResponseResult] | str: ...
    def remove(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def search(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> List[dict[Incomplete, Incomplete]]: ...
    def prune(
        self, filters: Incomplete | None = ...
    ) -> dict[Incomplete, Incomplete]: ...
    def prune_builds(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> dict[Incomplete, Incomplete]: ...

def normalize_platform(
    platform: dict[Incomplete, Incomplete] | None,
    engine_info: dict[Incomplete, Incomplete],
) -> dict[Incomplete, Incomplete]: ...
