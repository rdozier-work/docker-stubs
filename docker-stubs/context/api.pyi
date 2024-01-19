from typing import Optional
from docker import errors as errors
from docker.context import Context as Context
from docker.context.config import (
    METAFILE as METAFILE,
    get_current_context_name as get_current_context_name,
    get_meta_dir as get_meta_dir,
    write_context_name_to_docker_config as write_context_name_to_docker_config,
)
from docker.tls import TLSConfig as TLSConfig

class ContextAPI:
    DEFAULT_CONTEXT: str
    @classmethod
    def create_context(
        cls,
        name: str,
        orchestrator: Optional[str] = None,
        host: Optional[str] = None,
        tls_cfg: Optional[TLSConfig] = None,
        default_namespace: Optional[str] = None,
        skip_tls_verify: bool = False,
    ) -> Context: ...
    @classmethod
    def get_context(cls, name: Optional[str] = None) -> Context: ...
    @classmethod
    def contexts(cls) -> list[Context]: ...
    @classmethod
    def get_current_context(cls) -> Context: ...
    @classmethod
    def set_current_context(cls, name: str) -> None: ...
    @classmethod
    def remove_context(cls, name: str) -> None: ...
    @classmethod
    def inspect_context(cls, name: str) -> Context: ...
