import requests.exceptions
from requests.adapters import BaseAdapter

from .. import auth as auth
from ..constants import (
    DEFAULT_MAX_POOL_SIZE as DEFAULT_MAX_POOL_SIZE,
    DEFAULT_NUM_POOLS as DEFAULT_NUM_POOLS,
    DEFAULT_NUM_POOLS_SSH as DEFAULT_NUM_POOLS_SSH,
    DEFAULT_TIMEOUT_SECONDS as DEFAULT_TIMEOUT_SECONDS,
    DEFAULT_USER_AGENT as DEFAULT_USER_AGENT,
    IS_WINDOWS_PLATFORM as IS_WINDOWS_PLATFORM,
    MINIMUM_DOCKER_API_VERSION as MINIMUM_DOCKER_API_VERSION,
    STREAM_HEADER_SIZE_BYTES as STREAM_HEADER_SIZE_BYTES,
)
from ..errors import (
    DockerException as DockerException,
    InvalidVersion as InvalidVersion,
    TLSParameterError as TLSParameterError,
    create_api_error_from_http_exception as create_api_error_from_http_exception,
)
from ..tls import TLSConfig as TLSConfig
from ..transport import (
    NpipeHTTPAdapter as NpipeHTTPAdapter,
    SSHHTTPAdapter as SSHHTTPAdapter,
    UnixHTTPAdapter as UnixHTTPAdapter,
)
from ..utils import (
    check_resource as check_resource,
    config as config,
    update_headers as update_headers,
    utils as utils,
)
from ..utils.json_stream import json_stream as json_stream
from ..utils.proxy import ProxyConfig as ProxyConfig
from ..utils.socket import (
    consume_socket_output as consume_socket_output,
    demux_adaptor as demux_adaptor,
    frames_iter as frames_iter,
)
from .build import BuildApiMixin as BuildApiMixin
from .config import ConfigApiMixin as ConfigApiMixin
from .container import ContainerApiMixin as ContainerApiMixin
from .daemon import DaemonApiMixin as DaemonApiMixin
from .exec_api import ExecApiMixin as ExecApiMixin
from .image import ImageApiMixin as ImageApiMixin
from .network import NetworkApiMixin as NetworkApiMixin
from .plugin import PluginApiMixin as PluginApiMixin
from .secret import SecretApiMixin as SecretApiMixin
from .service import ServiceApiMixin as ServiceApiMixin
from .swarm import SwarmApiMixin as SwarmApiMixin
from .volume import VolumeApiMixin as VolumeApiMixin
from _typeshed import Incomplete

class APIClient(
    requests.Session,
    BuildApiMixin,
    ConfigApiMixin,
    ContainerApiMixin,
    DaemonApiMixin,
    ExecApiMixin,
    ImageApiMixin,
    NetworkApiMixin,
    PluginApiMixin,
    SecretApiMixin,
    ServiceApiMixin,
    SwarmApiMixin,
    VolumeApiMixin,
):
    __attrs__: list[str]
    base_url: str
    timeout: int
    credstore_env: dict[Incomplete, Incomplete]
    def __init__(
        self,
        base_url: str | None = ...,
        version: str | None = ...,
        timeout: int = ...,
        tls: bool | TLSConfig = ...,
        user_agent: str = ...,
        num_pools: int | None = ...,
        credstore_env: dict[Incomplete, Incomplete] | None = ...,
        use_ssh_client: bool = ...,
        max_pool_size: int = ...,
    ) -> None: ...
    @property
    def api_version(self) -> str: ...
    def get_adapter(self, url: str) -> BaseAdapter: ...
    def reload_config(self, dockercfg_path: str | None = ...) -> None: ...
