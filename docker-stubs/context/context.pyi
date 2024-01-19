from typing import Any, Optional
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
    context_type: str
    orchestrator: str
    endpoints: dict[str, Any]
    tls_cfg: TLSConfig
    meta_path: str
    tls_path: str
    def __init__(
        self,
        name: str,
        orchestrator: Optional[str] = None,
        host: Optional[str] = None,
        endpoints: Optional[dict[str, Any]] = None,
        tls: bool = False,
    ) -> None: ...
    def set_endpoint(
        self,
        name: str = None,
        host: Optional[str] = None,
        tls_cfg: Optional[TLSConfig] = None,
        skip_tls_verify: bool = False,
        def_namespace: Optional[str] = None,
    ) -> None: ...
    def inspect(self) -> dict[str, Any]: ...
    @classmethod
    def load_context(cls, name: str) -> "Context": ...
    def save(self) -> None: ...
    def remove(self) -> None: ...
    def __call__(self) -> dict[str, Any]: ...
    def is_docker_host(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Host(self) -> str: ...
    @property
    def Orchestrator(self) -> str: ...
    @property
    def Metadata(self) -> dict[str, Any]: ...
    @property
    def TLSConfig(self) -> TLSConfig: ...
    @property
    def TLSMaterial(self) -> dict[str, Any]: ...
    @property
    def Storage(self) -> dict[str, Any]: ...
