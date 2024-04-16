from typing import Collection
from typing import Generator
from typing import IO

from .. import auth as auth, errors as errors, utils as utils
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from _typeshed import Incomplete

from ..types.io import Json
from ..types.io import JsonDict
from ..types.io import ResponseResult
from ..types.misc_types import TrueOnSuccess


class ImageApiMixin:
    def get_image(self, image: str, chunk_size: int = ...) -> Generator[ResponseResult, None, None]: ...
    def history(self, image: str) -> str: ...
    def images(
        self,
        name: str | None = ...,
        quiet: bool = ...,
        all: bool = ...,
        filters: dict[str, Incomplete] | None = ...,
    ) -> dict | list: ...
    def import_image(
        self,
        src: str | IO | None = ...,
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
        filename,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ) -> ResponseResult: ...
    def import_image_from_stream(
        self,
        stream,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ) -> ResponseResult: ...
    def import_image_from_url(
        self,
        url,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ) -> ResponseResult: ...
    def import_image_from_image(
        self,
        image,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ) -> ResponseResult: ...
    def inspect_image(self, image: str) -> JsonDict: ...
    def inspect_distribution(self, image: str, auth_config: dict | None = ...) -> JsonDict: ...
    def load_image(self, data, quiet: bool | None = ...) -> Generator[ResponseResult, None, None]: ...
    def prune_images(self, filters: dict[str, Incomplete] | None = ...) -> dict[str, Incomplete]: ...
    def pull(
        self,
        repository: str,
        tag: str | None = ...,
        stream: bool = ...,
        auth_config: dict[str, Incomplete] | None = ...,
        decode: bool = ...,
        platform: str | None = ...,
        all_tags: bool = ...,
    ) -> str | Generator[ResponseResult, None, None]: ...
    def push(
        self,
        repository: str,
        tag: str | None = ...,
        stream: bool = ...,
        auth_config: dict[str, Incomplete] | None = ...,
        decode: bool = ...,
    ) -> str | Generator[ResponseResult, None, None]: ...
    def remove_image(self, image: str, force: bool = ..., noprune: bool = ...) -> Json: ...
    def search(self, term: str, limit: int | None = ...) -> list[JsonDict]: ...
    def tag(
        self, image: str, repository: str, tag: str | None = ..., force: bool = ...
    ) -> TrueOnSuccess: ...

def is_file(src) -> bool: ...
