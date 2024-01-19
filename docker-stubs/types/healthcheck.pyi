from typing import Optional
from .base import DictType as DictType

class Healthcheck(DictType):
    def __init__(
        self,
        test: Optional[list[str]] = None,
        interval: Optional[int] = None,
        timeout: Optional[int] = None,
        retries: Optional[int] = None,
        start_period: Optional[int] = None,
    ) -> None: ...
    @property
    def test(self) -> Optional[list[str]]: ...
    @property
    def interval(self) -> Optional[int]: ...
    @property
    def timeout(self) -> Optional[int]: ...
    @property
    def retries(self) -> Optional[int]: ...
    @property
    def start_period(self) -> Optional[int]: ...
