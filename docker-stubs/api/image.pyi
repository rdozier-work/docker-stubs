from typing import Optional, Union, Any
from .. import auth as auth, errors as errors, utils as utils
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from ..types import ImageSummary, ImageInspect, DistributionInspect

log: Any

class ImageApiMixin:
    def get_image(
        self, image: str, chunk_size: int = DEFAULT_DATA_CHUNK_SIZE
    ) -> Any: ...
    def history(self, image: str) -> list[dict[str, Any]]: ...
    def images(
        self,
        name: Optional[str] = None,
        quiet: bool = False,
        all: bool = False,
        filters: Optional[dict[str, Any]] = None,
    ) -> list[ImageSummary]: ...
    def import_image(
        self,
        src: Optional[str] = None,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        image: Optional[str] = None,
        changes: Optional[list[str]] = None,
        stream_src: bool = False,
    ) -> dict[str, Any]: ...
    def import_image_from_data(
        self,
        data: Any,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        changes: Optional[list[str]] = None,
    ) -> dict[str, Any]: ...
    def import_image_from_file(
        self,
        filename: str,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        changes: Optional[list[str]] = None,
    ) -> dict[str, Any]: ...
    def import_image_from_stream(
        self,
        stream: Any,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        changes: Optional[list[str]] = None,
    ) -> dict[str, Any]: ...
    def import_image_from_url(
        self,
        url: str,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        changes: Optional[list[str]] = None,
    ) -> dict[str, Any]: ...
    def import_image_from_image(
        self,
        image: str,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        changes: Optional[list[str]] = None,
    ) -> dict[str, Any]: ...
    def inspect_image(self, image: str) -> ImageInspect: ...
    def inspect_distribution(
        self, image: str, auth_config: Optional[dict[str, Any]] = None
    ) -> DistributionInspect: ...
    def load_image(self, data: Any, quiet: Optional[bool] = None) -> dict[str, Any]: ...
    def prune_images(
        self, filters: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]: ...
    def pull(
        self,
        repository: str,
        tag: Optional[str] = None,
        stream: bool = False,
        auth_config: Optional[dict[str, Any]] = None,
        decode: bool = False,
        platform: Optional[str] = None,
        all_tags: bool = False,
    ) -> Any: ...
    def push(
        self,
        repository: str,
        tag: Optional[str] = None,
        stream: bool = False,
        auth_config: Optional[dict[str, Any]] = None,
        decode: bool = False,
    ) -> Any: ...
    def remove_image(
        self, image: str, force: bool = False, noprune: bool = False
    ) -> dict[str, Any]: ...
    def search(
        self, term: str, limit: Optional[int] = None
    ) -> list[dict[str, Any]]: ...
    def tag(
        self,
        image: str,
        repository: str,
        tag: Optional[str] = None,
        force: bool = False,
    ) -> dict[str, Any]: ...

def is_file(src: Any) -> bool: ...
