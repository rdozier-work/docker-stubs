from typing import Optional
from .. import errors as errors, utils as utils

class SecretApiMixin:
    def create_secret(
        self,
        name: str,
        data: str,
        labels: Optional[dict[str, str]] = None,
        driver: Optional[str] = None,
    ) -> dict[str, str]: ...
    def inspect_secret(self, id: str) -> dict[str, str]: ...
    def remove_secret(self, id: str) -> None: ...
    def secrets(
        self, filters: Optional[dict[str, str]] = None
    ) -> list[dict[str, str]]: ...
