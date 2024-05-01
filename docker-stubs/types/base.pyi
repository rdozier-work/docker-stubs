from typing import Literal, TypeVar, TypedDict, TypeAlias
from _typeshed import Incomplete

_Command: TypeAlias = str | list[str]
_Port: TypeAlias = int | str
_Signal: TypeAlias = Literal["SIGINT", "SIGKILL", "SIGTERM"]

class _Versioned(TypedDict):
    version: str

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class DictType(dict[_KT, _VT]):
    def __init__(self, init: Incomplete) -> None: ...
