from .. import auth as auth, errors as errors, utils as utils
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from _typeshed import Incomplete

log: Incomplete

class ImageApiMixin:
    def get_image(self, image, chunk_size=...): ...
    def history(self, image): ...
    def images(
        self,
        name: Incomplete | None = ...,
        quiet: bool = ...,
        all: bool = ...,
        filters: Incomplete | None = ...,
    ): ...
    def import_image(
        self,
        src: Incomplete | None = ...,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        image: Incomplete | None = ...,
        changes: Incomplete | None = ...,
        stream_src: bool = ...,
    ): ...
    def import_image_from_data(
        self,
        data,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ): ...
    def import_image_from_file(
        self,
        filename,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ): ...
    def import_image_from_stream(
        self,
        stream,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ): ...
    def import_image_from_url(
        self,
        url,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ): ...
    def import_image_from_image(
        self,
        image,
        repository: Incomplete | None = ...,
        tag: Incomplete | None = ...,
        changes: Incomplete | None = ...,
    ): ...
    def inspect_image(self, image): ...
    def inspect_distribution(self, image, auth_config: Incomplete | None = ...): ...
    def load_image(self, data, quiet: Incomplete | None = ...): ...
    def prune_images(self, filters: Incomplete | None = ...): ...
    def pull(
        self,
        repository,
        tag: Incomplete | None = ...,
        stream: bool = ...,
        auth_config: Incomplete | None = ...,
        decode: bool = ...,
        platform: Incomplete | None = ...,
        all_tags: bool = ...,
    ): ...
    def push(
        self,
        repository,
        tag: Incomplete | None = ...,
        stream: bool = ...,
        auth_config: Incomplete | None = ...,
        decode: bool = ...,
    ): ...
    def remove_image(self, image, force: bool = ..., noprune: bool = ...): ...
    def search(self, term, limit: Incomplete | None = ...): ...
    def tag(
        self, image, repository, tag: Incomplete | None = ..., force: bool = ...
    ): ...

def is_file(src): ...
