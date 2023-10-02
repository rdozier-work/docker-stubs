from _typeshed import Incomplete
from typing import Any


class Model:
    id_attribute: str
    client: Incomplete
    collection: Incomplete
    attrs: Incomplete
    def __init__(
        self,
        attrs: Incomplete | None = ...,
        client: Incomplete | None = ...,
        collection: Incomplete | None = ...,
    ) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    @property
    def id(self): ...
    @property
    def short_id(self): ...
    def reload(self) -> None: ...

class Collection:
    model: Incomplete
    client: Incomplete
    def __init__(self, client: Incomplete | None = ...) -> None: ...
    def __call__(self, *args, **kwargs) -> None: ...
    def list(self) -> None: ...
    def get(self, key) -> None: ...
    def create(self, **_: Any) -> Any: ...
    def prepare_model(self, attrs): ...
