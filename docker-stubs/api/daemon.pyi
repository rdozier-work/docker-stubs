from datetime import datetime

from docker.types import CancellableStream
from _typeshed import Incomplete
from .. import auth as auth, types as types, utils as utils

from ..types._io import JsonDict

class DaemonApiMixin:
    def df(self) -> JsonDict: ...
    def events(
        self,
        since: int | datetime | None = ...,
        until: int | datetime | None = ...,
        filters: dict[Incomplete, Incomplete] | None = ...,
        decode: bool | None = ...,
    ) -> CancellableStream: ...
    def info(self) -> JsonDict: ...
    def login(
        self,
        username: str,
        password: str | None = ...,
        email: str | None = ...,
        registry: str | None = ...,
        reauth: bool = ...,
        dockercfg_path: str | None = ...,
    ) -> JsonDict: ...
    def ping(self) -> bool: ...
    def version(self, api_version: bool = ...) -> JsonDict: ...
