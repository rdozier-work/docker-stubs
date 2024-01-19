from typing import Optional, Any
from ..errors import InvalidVersion
from ..utils import version_lt

class SwarmSpec(dict[str, Any]):
    def __init__(
        self,
        version: str,
        task_history_retention_limit: Optional[int] = None,
        snapshot_interval: Optional[int] = None,
        keep_old_snapshots: Optional[int] = None,
        log_entries_for_slow_followers: Optional[int] = None,
        heartbeat_tick: Optional[int] = None,
        election_tick: Optional[int] = None,
        dispatcher_heartbeat_period: Optional[int] = None,
        node_cert_expiry: Optional[int] = None,
        external_cas: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        labels: Optional[dict[str, str]] = None,
        signing_ca_cert: Optional[str] = None,
        signing_ca_key: Optional[str] = None,
        ca_force_rotate: Optional[int] = None,
        autolock_managers: Optional[bool] = None,
        log_driver: Optional[dict[str, Any]] = None,
    ) -> None: ...

class SwarmExternalCA(dict[str, Any]):
    def __init__(
        self,
        url: str,
        protocol: Optional[str] = None,
        options: Optional[dict[str, Any]] = None,
        ca_cert: Optional[str] = None,
    ) -> None: ...
