from _typeshed import Incomplete
from os import PathLike
from typing import AnyStr, NewType, Protocol

JsonString = NewType("JsonString", str)
Json = str | int | float | bool | list["Json"] | dict[str, "Json"]
JsonList = list[Json]
JsonDict = dict[str, Json]
PathType = str | PathLike[AnyStr]
ResponseResult = Json | bytes | str

class Response(Protocol):
    status_code: Incomplete
    url: Incomplete

class Socket(Protocol): ...

class SupportsEncode(Protocol):
    def encode(self, input: AnyStr) -> AnyStr: ...
