from .. import auth as auth, constants as constants, errors as errors, utils as utils
from _typeshed import Incomplete

log: Incomplete

class BuildApiMixin:
    def build(self, path: Incomplete | None = ..., tag: Incomplete | None = ..., quiet: bool = ..., fileobj: Incomplete | None = ..., nocache: bool = ..., rm: bool = ..., timeout: Incomplete | None = ..., custom_context: bool = ..., encoding: Incomplete | None = ..., pull: bool = ..., forcerm: bool = ..., dockerfile: Incomplete | None = ..., container_limits: Incomplete | None = ..., decode: bool = ..., buildargs: Incomplete | None = ..., gzip: bool = ..., shmsize: Incomplete | None = ..., labels: Incomplete | None = ..., cache_from: Incomplete | None = ..., target: Incomplete | None = ..., network_mode: Incomplete | None = ..., squash: Incomplete | None = ..., extra_hosts: Incomplete | None = ..., platform: Incomplete | None = ..., isolation: Incomplete | None = ..., use_config_proxy: bool = ...): ...
    def prune_builds(self): ...

def process_dockerfile(dockerfile, path): ...
