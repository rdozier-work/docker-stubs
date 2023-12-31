from _typeshed import Incomplete
from docker.context.config import (
    get_context_host as get_context_host,
    get_meta_dir as get_meta_dir,
    get_meta_file as get_meta_file,
    get_tls_dir as get_tls_dir,
)
from docker.errors import ContextException as ContextException
from docker.tls import TLSConfig as TLSConfig

class Context:
    name: Incomplete
    context_type: Incomplete
    orchestrator: Incomplete
    endpoints: Incomplete
    tls_cfg: Incomplete
    meta_path: str
    tls_path: str
    def __init__(
        self,
        name,
        orchestrator: Incomplete | None = ...,
        host: Incomplete | None = ...,
        endpoints: Incomplete | None = ...,
        tls: bool = ...,
    ) -> None: ...
    def set_endpoint(
        self,
        name: str = ...,
        host: Incomplete | None = ...,
        tls_cfg: Incomplete | None = ...,
        skip_tls_verify: bool = ...,
        def_namespace: Incomplete | None = ...,
    ) -> None: ...
    def inspect(self): ...
    @classmethod
    def load_context(cls, name): ...
    def save(self) -> None: ...
    def remove(self) -> None: ...
    def __call__(self): ...
    def is_docker_host(self): ...
    @property
    def Name(self): ...
    @property
    def Host(self): ...
    @property
    def Orchestrator(self): ...
    @property
    def Metadata(self): ...
    @property
    def TLSConfig(self): ...
    @property
    def TLSMaterial(self): ...
    @property
    def Storage(self): ...
