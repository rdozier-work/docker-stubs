from typing import Optional, Dict, List
from .. import errors as errors, utils as utils

class SecretApiMixin:
    def create_secret(
        self,
        name: str,
        data: str,
        labels: Optional[Dict[str, str]] = None,
        driver: Optional[str] = None,
    ) -> Dict[str, str]: ...
    def inspect_secret(self, id: str) -> Dict[str, str]: ...
    def remove_secret(self, id: str) -> None: ...
    def secrets(
        self, filters: Optional[Dict[str, str]] = None
    ) -> List[Dict[str, str]]: ...
