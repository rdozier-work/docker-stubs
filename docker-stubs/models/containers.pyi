from ..api import APIClient as APIClient
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from ..errors import ContainerError as ContainerError, DockerException as DockerException, ImageNotFound as ImageNotFound, NotFound as NotFound, create_unexpected_kwargs_error as create_unexpected_kwargs_error
from ..types import HostConfig as HostConfig
from ..utils import version_gte as version_gte
from .images import Image as Image
from .resource import Collection as Collection, Model as Model
from _typeshed import Incomplete
from typing import NamedTuple

class Container(Model):
    @property
    def name(self): ...
    @property
    def image(self): ...
    @property
    def labels(self): ...
    @property
    def status(self): ...
    @property
    def ports(self): ...
    def attach(self, **kwargs): ...
    def attach_socket(self, **kwargs): ...
    def commit(self, repository: Incomplete | None = ..., tag: Incomplete | None = ..., **kwargs): ...
    def diff(self): ...
    def exec_run(self, cmd, stdout: bool = ..., stderr: bool = ..., stdin: bool = ..., tty: bool = ..., privileged: bool = ..., user: str = ..., detach: bool = ..., stream: bool = ..., socket: bool = ..., environment: Incomplete | None = ..., workdir: Incomplete | None = ..., demux: bool = ...): ...
    def export(self, chunk_size=...): ...
    def get_archive(self, path, chunk_size=..., encode_stream: bool = ...): ...
    def kill(self, signal: Incomplete | None = ...): ...
    def logs(self, **kwargs): ...
    def pause(self): ...
    def put_archive(self, path, data): ...
    def remove(self, **kwargs): ...
    def rename(self, name): ...
    def resize(self, height, width): ...
    def restart(self, **kwargs): ...
    def start(self, **kwargs): ...
    def stats(self, **kwargs): ...
    def stop(self, **kwargs): ...
    def top(self, **kwargs): ...
    def unpause(self): ...
    def update(self, **kwargs): ...
    def wait(self, **kwargs): ...

class ContainerCollection(Collection):
    model = Container
    def run(self, image, command: Incomplete | None = ..., stdout: bool = ..., stderr: bool = ..., remove: bool = ..., **kwargs): ...
    def create(self, image, command: Incomplete | None = ..., **kwargs): ...
    def get(self, container_id): ...
    def list(self, all: bool = ..., before: Incomplete | None = ..., filters: Incomplete | None = ..., limit: int = ..., since: Incomplete | None = ..., sparse: bool = ..., ignore_removed: bool = ...): ...
    def prune(self, filters: Incomplete | None = ...): ...

RUN_CREATE_KWARGS: Incomplete
RUN_HOST_CONFIG_KWARGS: Incomplete

class ExecResult(NamedTuple):
    exit_code: Incomplete
    output: Incomplete