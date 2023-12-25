from typing import Optional, Union
from .. import errors as errors, utils as utils
from ..types import CancellableStream as CancellableStream

class ExecApiMixin:
    def exec_create(
        self,
        container: str,
        cmd: Union[str, list[str]],
        stdout: bool = True,
        stderr: bool = True,
        stdin: bool = False,
        tty: bool = False,
        privileged: bool = False,
        user: Optional[str] = None,
        environment: Optional[dict[str, str]] = None,
        workdir: Optional[str] = None,
        detach_keys: Optional[str] = None,
    ) -> dict: ...
    def exec_inspect(self, exec_id: str) -> dict: ...
    def exec_resize(
        self, exec_id: str, height: Optional[int] = None, width: Optional[int] = None
    ) -> None: ...
    def exec_start(
        self,
        exec_id: str,
        detach: bool = False,
        tty: bool = False,
        stream: bool = False,
        socket: bool = False,
        demux: bool = False,
    ) -> Union[str, CancellableStream]: ...
