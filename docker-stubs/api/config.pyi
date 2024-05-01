from .. import utils as utils
from ..types._io import JsonDict
from ..types._io import JsonList
from ..types.misc_types import TrueOnSuccess
from _typeshed import Incomplete

class ConfigApiMixin:
    def create_config(
        self,
        name: str,
        data: bytes,
        labels: dict[Incomplete, Incomplete] | None = ...,
        templating: dict[Incomplete, Incomplete] | None = ...,
    ) -> JsonDict: ...
    def inspect_config(self, id: str) -> JsonDict: ...
    def remove_config(self, id: str) -> TrueOnSuccess: ...
    def configs(
        self, filters: dict[Incomplete, Incomplete] | None = ...
    ) -> JsonList: ...
