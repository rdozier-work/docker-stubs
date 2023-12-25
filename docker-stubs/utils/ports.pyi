from typing import Dict, Union, Tuple, Optional, List

PORT_SPEC: Dict[str, Union[int, Tuple[int, int]]]

def add_port_mapping(
    port_bindings: Dict[str, Union[int, Tuple[int, int]]],
    internal_port: int,
    external: Union[int, Tuple[int, int]],
) -> None: ...
def add_port(
    port_bindings: Dict[str, Union[int, Tuple[int, int]]],
    internal_port_range: Union[int, Tuple[int, int]],
    external_range: Union[int, Tuple[int, int]],
) -> None: ...
def build_port_bindings(
    ports: Dict[str, Union[int, Tuple[int, int]]]
) -> Dict[str, Union[int, Tuple[int, int]]]: ...
def port_range(
    start: int, end: int, proto: str, randomly_available_port: bool = False
) -> List[int]: ...
def split_port(port: Union[int, Tuple[int, int]]) -> Tuple[int, int]: ...
