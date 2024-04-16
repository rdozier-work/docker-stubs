from .. import errors as errors, utils as utils
from _typeshed import Incomplete

from ..types.io import JsonDict


class VolumeApiMixin:
    def volumes(self, filters: dict | None = ...) -> JsonDict: ...
    def create_volume(
        self,
        name: str | None = ...,
        driver: str | None = ...,
        driver_opts: dict | None = ...,
        labels: dict | None = ...,
    ) -> JsonDict: ...
    def inspect_volume(self, name: str) -> JsonDict: ...
    def prune_volumes(self, filters: dict | None = ...) -> dict: ...
    def remove_volume(self, name: str, force: bool = ...) -> None: ...
