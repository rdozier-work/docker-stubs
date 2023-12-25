from typing import Optional, Union, Any
from .. import auth as auth, types as types, utils as utils

class DaemonApiMixin:
    def df(self) -> dict[str, Any]: ...
    def events(
        self,
        since: Optional[Union[int, str]] = None,
        until: Optional[Union[int, str]] = None,
        filters: Optional[dict[str, Union[str, bool]]] = None,
        decode: bool = False,
    ) -> dict[str, Any]: ...
    def info(self) -> dict[str, Any]: ...
    def login(
        self,
        username: str,
        password: Optional[str] = None,
        email: Optional[str] = None,
        registry: Optional[str] = None,
        reauth: bool = False,
        dockercfg_path: Optional[str] = None,
    ) -> dict[str, Any]: ...
    def ping(self) -> dict[str, Any]: ...
    def version(self, api_version: bool = False) -> dict[str, Any]: ...
