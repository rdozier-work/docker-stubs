from docker.types import CancellableStream

from .api.client import APIClient as APIClient
from .constants import (
    DEFAULT_MAX_POOL_SIZE as DEFAULT_MAX_POOL_SIZE,
    DEFAULT_TIMEOUT_SECONDS as DEFAULT_TIMEOUT_SECONDS,
)
from .models.configs import ConfigCollection as ConfigCollection
from .models.containers import ContainerCollection as ContainerCollection
from .models.images import ImageCollection as ImageCollection
from .models.networks import NetworkCollection as NetworkCollection
from .models.nodes import NodeCollection as NodeCollection
from .models.plugins import PluginCollection as PluginCollection
from .models.secrets import SecretCollection as SecretCollection
from .models.services import ServiceCollection as ServiceCollection
from .models.swarm import Swarm as Swarm
from .models.volumes import VolumeCollection as VolumeCollection
from .utils import kwargs_from_env as kwargs_from_env
from _typeshed import Incomplete

class DockerClient:
    api: APIClient
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    @classmethod
    def from_env(cls, **kwargs: Incomplete) -> DockerClient: ...
    @property
    def configs(self) -> ConfigCollection: ...
    @property
    def containers(self) -> ContainerCollection: ...
    @property
    def images(self) -> ImageCollection: ...
    @property
    def networks(self) -> NetworkCollection: ...
    @property
    def nodes(self) -> NodeCollection: ...
    @property
    def plugins(self) -> PluginCollection: ...
    @property
    def secrets(self) -> SecretCollection: ...
    @property
    def services(self) -> ServiceCollection: ...
    @property
    def swarm(self) -> Swarm: ...
    @property
    def volumes(self) -> VolumeCollection: ...
    def events(self, *args: Incomplete, **kwargs: Incomplete) -> CancellableStream: ...
    def df(self) -> dict[Incomplete, Incomplete]: ...
    def info(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> dict[Incomplete, Incomplete]: ...
    def login(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> dict[Incomplete, Incomplete]: ...
    def ping(self, *args: Incomplete, **kwargs: Incomplete) -> bool: ...
    def version(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> dict[Incomplete, Incomplete]: ...
    def close(self) -> None: ...
    def __getattr__(self, name: str) -> None: ...

def from_env(
    *,
    assert_hostname: bool = ...,
    max_pool_size: int = ...,
    timeout: int = ...,
    use_ssh_client: bool = ...,
    version: str | None = ...
) -> DockerClient: ...
