from typing import Optional, Dict
from .. import errors as errors, utils as utils

class VolumeApiMixin:
    def volumes(self, filters: Optional[Dict[str, str]] = None) -> Dict[str, str]: ...
    def create_volume(
        self,
        name: Optional[str] = None,
        driver: Optional[str] = None,
        driver_opts: Optional[Dict[str, str]] = None,
        labels: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]: ...
    def inspect_volume(self, name: str) -> Dict[str, str]: ...
    def prune_volumes(
        self, filters: Optional[Dict[str, str]] = None
    ) -> Dict[str, str]: ...
    def remove_volume(self, name: str, force: bool = False) -> None: ...
