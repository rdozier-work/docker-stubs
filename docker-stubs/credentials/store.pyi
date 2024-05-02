from . import constants as constants, errors as errors
from .utils import create_environment_dict as create_environment_dict
from _typeshed import Incomplete

from ..types._io import JsonString
from ..types._io import SupportsEncode

class Store:
    program: str
    exe: str
    environment: Incomplete
    def __init__(self, program: str, environment: Incomplete | None = ...) -> None: ...
    def get(self, server: bytes | SupportsEncode) -> JsonString: ...
    def store(
        self, server: Incomplete, username: Incomplete, secret: Incomplete
    ) -> Incomplete: ...
    def erase(self, server: Incomplete) -> None: ...
    def list(self) -> JsonString: ...
