from _typeshed import Incomplete
from typing import Literal

from docker.context.config import (
    get_context_host as get_context_host,
    get_meta_dir as get_meta_dir,
    get_meta_file as get_meta_file,
    get_tls_dir as get_tls_dir,
)
from docker.errors import ContextException as ContextException
from docker.tls import TLSConfig as TLSConfig

class Context:
    name: str
    context_type: Incomplete | None
    orchestrator: str | None
    endpoints: dict[Incomplete, Incomplete]
    tls_cfg: dict[Incomplete, Incomplete]
    meta_path: str
    tls_path: str
    def __init__(
        self,
        name: str,
        orchestrator: str | None = ...,
        host: str | None = ...,
        endpoints: dict[Incomplete, Incomplete] | None = ...,
        tls: bool = ...,
    ) -> None: ...
    def set_endpoint(
        self,
        name: str = ...,
        host: str | None = ...,
        tls_cfg: dict[Incomplete, Incomplete] | None = ...,
        skip_tls_verify: bool = ...,
        def_namespace: str | None = ...,
    ) -> None: ...
    def inspect(self) -> dict[Incomplete, Incomplete]: ...
    @classmethod
    def load_context(cls, name: str) -> Context | None: ...
    def save(self) -> None: ...
    def remove(self) -> None: ...
    def __call__(self) -> dict[Incomplete, Incomplete]: ...
    def is_docker_host(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Host(self) -> Incomplete | None: ...
    @property
    def Orchestrator(self) -> str: ...
    @property
    def Metadata(self) -> dict[Incomplete, Incomplete]: ...
    @property
    def TLSConfig(self) -> Incomplete | None: ...
    @property
    def TLSMaterial(
        self,
    ) -> dict[Literal["TLSMaterial"], dict[Incomplete, Incomplete]]: ...
    @property
    def Storage(self) -> dict[Literal["Storage"], dict[Incomplete, Incomplete]]: ...
