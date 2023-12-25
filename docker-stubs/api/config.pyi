from typing import Optional, Union

class ConfigApiMixin:
    def create_config(
        self,
        name: str,
        data: dict[str, object],
        labels: Optional[dict[str, str]] = None,
        templating: Optional[dict[str, object]] = None,
    ) -> dict[str, object]: ...
    def inspect_config(self, id: str) -> dict[str, object]: ...
    def remove_config(self, id: str) -> None: ...
    def configs(
        self, filters: Optional[dict[str, Union[str, bool]]] = None
    ) -> list[dict[str, object]]: ...
