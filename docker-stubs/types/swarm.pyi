from ..errors import InvalidVersion as InvalidVersion
from ..utils import version_lt as version_lt
from _typeshed import Incomplete

class SwarmSpec(dict):
    def __init__(
        self,
        version,
        task_history_retention_limit: Incomplete | None = ...,
        snapshot_interval: Incomplete | None = ...,
        keep_old_snapshots: Incomplete | None = ...,
        log_entries_for_slow_followers: Incomplete | None = ...,
        heartbeat_tick: Incomplete | None = ...,
        election_tick: Incomplete | None = ...,
        dispatcher_heartbeat_period: Incomplete | None = ...,
        node_cert_expiry: Incomplete | None = ...,
        external_cas: Incomplete | None = ...,
        name: Incomplete | None = ...,
        labels: Incomplete | None = ...,
        signing_ca_cert: Incomplete | None = ...,
        signing_ca_key: Incomplete | None = ...,
        ca_force_rotate: Incomplete | None = ...,
        autolock_managers: Incomplete | None = ...,
        log_driver: Incomplete | None = ...,
    ) -> None: ...

class SwarmExternalCA(dict):
    def __init__(
        self,
        url,
        protocol: Incomplete | None = ...,
        options: Incomplete | None = ...,
        ca_cert: Incomplete | None = ...,
    ) -> None: ...
