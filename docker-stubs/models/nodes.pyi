from .resource import Collection as Collection, Model as Model
from ..types.misc_types import TrueOnSuccess
from _typeshed import Incomplete

class Node(Model):
    id_attribute: str
    @property
    def version(self) -> str: ...
    def update(self, node_spec: dict[Incomplete, Incomplete]) -> TrueOnSuccess: ...
    def remove(self, force: bool = ...) -> TrueOnSuccess: ...

class NodeCollection(Collection):
    model = Node
    def get(self, node_id: str) -> Node: ...  # type: ignore[override]
    def list(self, *args: Incomplete, **kwargs: Incomplete) -> list[Node]: ...  # type: ignore[override]
