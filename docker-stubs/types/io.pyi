from _typeshed import Incomplete
from os import PathLike
from typing import AnyStr
from typing import NewType
from typing import Protocol
from typing import Union

JsonString = NewType("JsonString", str)
Json = Union[str, int, float, bool, list["Json"], dict[str, "Json"]]
JsonList = list[Json]
JsonDict = dict[str, Json]
PathType = Union[str, PathLike]
ResponseResult = Union[Json, bytes, AnyStr]


class Response(Protocol):
    status_code: Incomplete
    url: Incomplete


class Socket(Protocol): ...


class SupportsEncode(Protocol):
    def encode(self, input: str) -> AnyStr: ...
