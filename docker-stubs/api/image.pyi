from typing import BinaryIO, Collection, Iterator
from typing import Generator

from .. import auth as auth, errors as errors, utils as utils
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from _typeshed import Incomplete

from ..types._io import Json
from ..types._io import JsonDict
from ..types._io import ResponseResult
from ..types.misc_types import TrueOnSuccess

class ImageApiMixin:
    def get_image(
        self, image: str, chunk_size: int = ...
    ) -> Iterator[ResponseResult]: ...
    def history(self, image: str) -> str: ...
    def images(
        self,
        name: str | None = ...,
        quiet: bool = ...,
        all: bool = ...,
        filters: dict[str, Incomplete] | None = ...,
    ) -> dict[Incomplete, Incomplete] | list[Incomplete]: ...
    def import_image(
        self,
        src: str | BinaryIO | None = ...,
        repository: str | None = ...,
        tag: str | None = ...,
        image: str | None = ...,
        changes: Incomplete | None = ...,
        stream_src: bool = ...,
    ) -> ResponseResult: ...
    def import_image_from_data(
        self,
        data: Collection[bytes],
        repository: str | None = ...,
        tag: str | None = ...,
        changes: Incomplete | None = ...,
    ) -> ResponseResult: ...
    def import_image_from_file(
        self,
        filename: str,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ) -> ResponseResult: ...
    def import_image_from_stream(
        self,
        stream: Incomplete,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ) -> ResponseResult: ...
    def import_image_from_url(
        self,
        url: str,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ) -> ResponseResult: ...
    def import_image_from_image(
        self,
        image: Incomplete,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ) -> ResponseResult: ...
    def inspect_image(self, image: str) -> JsonDict: ...
    def inspect_distribution(
        self, image: str, auth_config: dict[Incomplete, Incomplete] | None = ...
    ) -> JsonDict: ...
    def load_image(
        self, data: Incomplete, quiet: bool | None = ...
    ) -> Iterator[ResponseResult]: ...
    def prune_images(
        self, filters: dict[str, Incomplete] | None = ...
    ) -> dict[str, Incomplete]: ...
    def pull(
        self,
        repository: str,
        tag: str | None = ...,
        stream: bool = ...,
        auth_config: dict[str, Incomplete] | None = ...,
        decode: bool = ...,
        platform: str | None = ...,
        all_tags: bool = ...,
    ) -> str | Iterator[ResponseResult]: ...
    def push(
        self,
        repository: str,
        tag: str | None = ...,
        stream: bool = ...,
        auth_config: dict[str, Incomplete] | None = ...,
        decode: bool = ...,
    ) -> str | Generator[ResponseResult, None, None]: ...
    def remove_image(
        self, image: str, force: bool = ..., noprune: bool = ...
    ) -> Json: ...
    def search(self, term: str, limit: int | None = ...) -> list[JsonDict]: ...
    def tag(
        self, image: str, repository: str, tag: str | None = ..., force: bool = ...
    ) -> TrueOnSuccess: ...

def is_file(src: Incomplete) -> bool: ...
