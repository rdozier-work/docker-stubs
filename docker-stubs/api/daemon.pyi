from typing import Optional, Union, Dict, Any
from .. import auth as auth, types as types, utils as utils

class DaemonApiMixin:
    def df(self) -> Dict[str, Any]: ...
    def events(
        self,
        since: Optional[Union[int, str]] = None,
        until: Optional[Union[int, str]] = None,
        filters: Optional[Dict[str, Union[str, bool]]] = None,
        decode: bool = False,
    ) -> Dict[str, Any]: ...
    def info(self) -> Dict[str, Any]: ...
    def login(
        self,
        username: str,
        password: Optional[str] = None,
        email: Optional[str] = None,
        registry: Optional[str] = None,
        reauth: bool = False,
        dockercfg_path: Optional[str] = None,
    ) -> Dict[str, Any]: ...
    def ping(self) -> Dict[str, Any]: ...
    def version(self, api_version: bool = False) -> Dict[str, Any]: ...
