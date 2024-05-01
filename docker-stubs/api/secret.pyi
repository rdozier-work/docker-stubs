from docker.types import DriverConfig

from .. import errors as errors, utils as utils
from _typeshed import Incomplete

from ..types._io import JsonDict
from ..types._io import JsonList
from ..types.misc_types import TrueOnSuccess

class SecretApiMixin:
    def create_secret(
        self,
        name: str,
        data: bytes,
        labels: dict[str, Incomplete] | None = ...,
        driver: DriverConfig | None = ...,
    ) -> JsonDict: ...
    def inspect_secret(self, id: str) -> JsonDict: ...
    def remove_secret(self, id: str) -> TrueOnSuccess: ...
    def secrets(self, filters: dict[str, Incomplete] | None = ...) -> JsonList: ...
