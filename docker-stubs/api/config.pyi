from typing import Literal

from .. import utils as utils
from ..types.io import JsonDict
from ..types.io import JsonList
from ..types.misc_types import TrueOnSuccess


class ConfigApiMixin:
    def create_config(
        self,
        name: str,
        data: bytes,
        labels: dict | None = ...,
        templating: dict | None = ...,
    ) -> JsonDict: ...
    def inspect_config(self, id: str) -> JsonDict: ...
    def remove_config(self, id) -> TrueOnSuccess: ...
    def configs(self, filters: dict | None = ...) -> JsonList: ...
