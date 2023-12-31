from .. import utils as utils
from _typeshed import Incomplete

class ConfigApiMixin:
    def create_config(
        self,
        name,
        data,
        labels: Incomplete | None = ...,
        templating: Incomplete | None = ...,
    ): ...
    def inspect_config(self, id): ...
    def remove_config(self, id): ...
    def configs(self, filters: Incomplete | None = ...): ...
