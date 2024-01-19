from typing import Optional, Union, Any
import requests
from .. import auth as auth, utils as utils
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
    SSLHTTPAdapter as SSLHTTPAdapter,
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
    __attrs__: dict[str, Any]
    base_url: str
    timeout: Union[int, float]
    credstore_env: dict[str, Any]
    def __init__(
        self,
        base_url: Optional[str] = None,
        version: Optional[str] = None,
        timeout: Union[int, float] = DEFAULT_TIMEOUT_SECONDS,
        tls: bool = False,
        user_agent: str = DEFAULT_USER_AGENT,
        num_pools: int = DEFAULT_NUM_POOLS,
        credstore_env: Optional[dict[str, Any]] = None,
        use_ssh_client: bool = False,
        max_pool_size: int = DEFAULT_MAX_POOL_SIZE,
    ) -> None: ...
    def get_adapter(
        self, url: str
    ) -> Union[NpipeHTTPAdapter, SSHHTTPAdapter, SSLHTTPAdapter, UnixHTTPAdapter]: ...
    @property
    def api_version(self) -> str: ...
    def reload_config(self, dockercfg_path: Optional[str] = None) -> None: ...
