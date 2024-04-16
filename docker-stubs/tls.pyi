from . import errors as errors
from _typeshed import Incomplete

class TLSConfig:
    cert: Incomplete
    ca_cert: Incomplete
    verify: Incomplete
    def __init__(
        self,
        client_cert: Incomplete | None = ...,
        ca_cert: Incomplete | None = ...,
        verify: Incomplete | None = ...,
    ) -> None: ...
    def configure_client(self, client) -> None: ...
