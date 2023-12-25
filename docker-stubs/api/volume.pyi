from typing import Optional
from .. import errors as errors, utils as utils

class VolumeApiMixin:
    def volumes(self, filters: Optional[dict[str, str]] = None) -> dict[str, str]: ...
    def create_volume(
        self,
        name: Optional[str] = None,
        driver: Optional[str] = None,
        driver_opts: Optional[dict[str, str]] = None,
        labels: Optional[dict[str, str]] = None,
    ) -> dict[str, str]: ...
    def inspect_volume(self, name: str) -> dict[str, str]: ...
    def prune_volumes(
        self, filters: Optional[dict[str, str]] = None
    ) -> dict[str, str]: ...
    def remove_volume(self, name: str, force: bool = False) -> None: ...
