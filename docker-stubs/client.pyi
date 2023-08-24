from .api.client import APIClient as APIClient
from .constants import DEFAULT_MAX_POOL_SIZE as DEFAULT_MAX_POOL_SIZE, DEFAULT_TIMEOUT_SECONDS as DEFAULT_TIMEOUT_SECONDS
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
    api: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def from_env(cls, **kwargs): ...
    @property
    def configs(self): ...
    @property
    def containers(self): ...
    @property
    def images(self): ...
    @property
    def networks(self): ...
    @property
    def nodes(self): ...
    @property
    def plugins(self): ...
    @property
    def secrets(self): ...
    @property
    def services(self): ...
    @property
    def swarm(self): ...
    @property
    def volumes(self): ...
    def events(self, *args, **kwargs): ...
    def df(self): ...
    def info(self, *args, **kwargs): ...
    def login(self, *args, **kwargs): ...
    def ping(self, *args, **kwargs): ...
    def version(self, *args, **kwargs): ...
    def close(self): ...
    def __getattr__(self, name) -> None: ...

from_env: Incomplete
