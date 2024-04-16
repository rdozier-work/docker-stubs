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


class Socket(Protocol): ...
