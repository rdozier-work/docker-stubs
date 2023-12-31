from .. import auth as auth, types as types, utils as utils
from _typeshed import Incomplete

class DaemonApiMixin:
    def df(self): ...
    def events(
        self,
        since: Incomplete | None = ...,
        until: Incomplete | None = ...,
        filters: Incomplete | None = ...,
        decode: Incomplete | None = ...,
    ): ...
    def info(self): ...
    def login(
        self,
        username,
        password: Incomplete | None = ...,
        email: Incomplete | None = ...,
        registry: Incomplete | None = ...,
        reauth: bool = ...,
        dockercfg_path: Incomplete | None = ...,
    ): ...
    def ping(self): ...
    def version(self, api_version: bool = ...): ...
