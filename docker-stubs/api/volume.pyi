from .. import errors as errors, utils as utils
from _typeshed import Incomplete

from ..types._io import JsonDict

class VolumeApiMixin:
    def volumes(
        self, filters: dict[Incomplete, Incomplete] | None = ...
    ) -> JsonDict: ...
    def create_volume(
        self,
        name: str | None = ...,
        driver: str | None = ...,
        driver_opts: dict[Incomplete, Incomplete] | None = ...,
        labels: dict[Incomplete, Incomplete] | None = ...,
    ) -> JsonDict: ...
    def inspect_volume(self, name: str) -> JsonDict: ...
    def prune_volumes(
        self, filters: dict[Incomplete, Incomplete] | None = ...
    ) -> dict[Incomplete, Incomplete]: ...
    def remove_volume(self, name: str, force: bool = ...) -> None: ...
