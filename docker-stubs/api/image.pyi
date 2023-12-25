from typing import Optional, Union, List, Dict, Any
from .. import auth as auth, errors as errors, utils as utils
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from ..types import ImageSummary, ImageInspect, DistributionInspect

log: Any

class ImageApiMixin:
    def get_image(
        self, image: str, chunk_size: int = DEFAULT_DATA_CHUNK_SIZE
    ) -> Any: ...
    def history(self, image: str) -> List[Dict[str, Any]]: ...
    def images(
        self,
        name: Optional[str] = None,
        quiet: bool = False,
        all: bool = False,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[ImageSummary]: ...
    def import_image(
        self,
        src: Optional[str] = None,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        image: Optional[str] = None,
        changes: Optional[List[str]] = None,
        stream_src: bool = False,
    ) -> Dict[str, Any]: ...
    def import_image_from_data(
        self,
        data: Any,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        changes: Optional[List[str]] = None,
    ) -> Dict[str, Any]: ...
    def import_image_from_file(
        self,
        filename: str,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        changes: Optional[List[str]] = None,
    ) -> Dict[str, Any]: ...
    def import_image_from_stream(
        self,
        stream: Any,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        changes: Optional[List[str]] = None,
    ) -> Dict[str, Any]: ...
    def import_image_from_url(
        self,
        url: str,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        changes: Optional[List[str]] = None,
    ) -> Dict[str, Any]: ...
    def import_image_from_image(
        self,
        image: str,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        changes: Optional[List[str]] = None,
    ) -> Dict[str, Any]: ...
    def inspect_image(self, image: str) -> ImageInspect: ...
    def inspect_distribution(
        self, image: str, auth_config: Optional[Dict[str, Any]] = None
    ) -> DistributionInspect: ...
    def load_image(self, data: Any, quiet: Optional[bool] = None) -> Dict[str, Any]: ...
    def prune_images(
        self, filters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]: ...
    def pull(
        self,
        repository: str,
        tag: Optional[str] = None,
        stream: bool = False,
        auth_config: Optional[Dict[str, Any]] = None,
        decode: bool = False,
        platform: Optional[str] = None,
        all_tags: bool = False,
    ) -> Any: ...
    def push(
        self,
        repository: str,
        tag: Optional[str] = None,
        stream: bool = False,
        auth_config: Optional[Dict[str, Any]] = None,
        decode: bool = False,
    ) -> Any: ...
    def remove_image(
        self, image: str, force: bool = False, noprune: bool = False
    ) -> Dict[str, Any]: ...
    def search(
        self, term: str, limit: Optional[int] = None
    ) -> List[Dict[str, Any]]: ...
    def tag(
        self,
        image: str,
        repository: str,
        tag: Optional[str] = None,
        force: bool = False,
    ) -> Dict[str, Any]: ...

def is_file(src: Any) -> bool: ...
