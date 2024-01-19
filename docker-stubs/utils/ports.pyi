from typing import Union

PORT_SPEC: dict[str, Union[int, tuple[int, int]]]

def add_port_mapping(
    port_bindings: dict[str, Union[int, tuple[int, int]]],
    internal_port: int,
    external: Union[int, tuple[int, int]],
) -> None: ...
def add_port(
    port_bindings: dict[str, Union[int, tuple[int, int]]],
    internal_port_range: Union[int, tuple[int, int]],
    external_range: Union[int, tuple[int, int]],
) -> None: ...
def build_port_bindings(
    ports: dict[str, Union[int, tuple[int, int]]]
) -> dict[str, Union[int, tuple[int, int]]]: ...
def port_range(
    start: int, end: int, proto: str, randomly_available_port: bool = False
) -> list[int]: ...
def split_port(port: Union[int, tuple[int, int]]) -> tuple[int, int]: ...
