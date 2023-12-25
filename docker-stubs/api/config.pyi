from typing import Optional, Union, List, Dict, Any
from .. import utils as utils

class ConfigApiMixin:
    def create_config(
        self,
        name: str,
        data: Dict[str, Any],
        labels: Optional[Dict[str, str]] = None,
        templating: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]: ...
    def inspect_config(self, id: str) -> Dict[str, Any]: ...
    def remove_config(self, id: str) -> None: ...
    def configs(
        self, filters: Optional[Dict[str, Union[str, bool]]] = None
    ) -> List[Dict[str, Any]]: ...
