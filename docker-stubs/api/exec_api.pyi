from .. import errors as errors, utils as utils
from ..types import CancellableStream as CancellableStream
from _typeshed import Incomplete

from ..types.io import JsonDict
from ..types.io import Socket


class ExecApiMixin:
    def exec_create(
        self,
        container: str,
        cmd: str | list,
        stdout: bool = ...,
        stderr: bool = ...,
        stdin: bool = ...,
        tty: bool = ...,
        privileged: bool = ...,
        user: str = ...,
        environment: dict | list | None = ...,
        workdir: str | None = ...,
        detach_keys: str | None = ...,
    ) -> JsonDict: ...
    def exec_inspect(self, exec_id: str) -> JsonDict: ...
    def exec_resize(
        self, exec_id: str, height: int | None = ..., width: int | None = ...
    ) -> None: ...
    def exec_start(
        self,
        exec_id: str,
        detach: bool = ...,
        tty: bool = ...,
        stream: bool = ...,
        socket: bool = ...,
        demux: bool = ...,
    ) -> str | CancellableStream | Socket: ...
