from typing import NewType, Literal, TypedDict, Any

Command = str | list[str]
PathStr = NewType("PathStr", str)
MacAddress = NewType("MacAddress", str)
Port = int | str
Signal = str | Literal["SIGINT", "SIGKILL", "SIGTERM"]

class Versioned(TypedDict):
    version: str

class DictType(dict):
    def __init__(self, init: Command) -> None: ...
