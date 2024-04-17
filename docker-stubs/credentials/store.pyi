from . import constants as constants, errors as errors
from .utils import create_environment_dict as create_environment_dict
from _typeshed import Incomplete

from ..types.io import JsonString
from ..types.io import SupportsEncode


class Store:
    program: str
    exe: str
    environment: Incomplete
    def __init__(self, program, environment: Incomplete | None = ...) -> None: ...
    def get(self, server: bytes | SupportsEncode) -> JsonString: ...
    def store(self, server: Incomplete, username: Incomplete, secret: Incomplete) -> Incomplete: ...
    def erase(self, server: Incomplete) -> None: ...
    def list(self) -> JsonString: ...
