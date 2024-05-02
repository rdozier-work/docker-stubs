from _typeshed import Incomplete
from typing import Type

class Model:
    id_attribute: str
    client: Incomplete
    collection: Incomplete
    attrs: dict[Incomplete, Incomplete]
    def __init__(
        self,
        attrs: dict[Incomplete, Incomplete] | None = ...,
        client: Incomplete | None = ...,
        collection: Incomplete | None = ...,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def id(self) -> str: ...
    @property
    def short_id(self) -> str: ...
    def reload(self) -> None: ...

class Collection:
    model: Type[Model] | None
    client: Incomplete
    def __init__(self, client: Incomplete | None = ...) -> None: ...
    def __call__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def list(self) -> None: ...
    def get(self, key: str) -> None: ...
    def create(self, attrs: Incomplete) -> None: ...
    def prepare_model(
        self, attrs: Model | dict[Incomplete, Incomplete] | None = ...
    ) -> Model: ...
