import requests
from _typeshed import Incomplete

from docker.types.io import Response


class DockerException(Exception): ...

def create_api_error_from_http_exception(e) -> None: ...

class APIError(requests.exceptions.HTTPError, DockerException):
    response: Response
    explanation: Incomplete
    def __init__(
        self,
        message,
        response: Response | None = ...,
        explanation: Incomplete | None = ...,
    ) -> None: ...
    @property
    def status_code(self) -> Incomplete: ...
    def is_error(self) -> bool: ...
    def is_client_error(self) -> bool: ...
    def is_server_error(self) -> bool: ...

class NotFound(APIError): ...
class ImageNotFound(NotFound): ...
class InvalidVersion(DockerException): ...
class InvalidRepository(DockerException): ...
class InvalidConfigFile(DockerException): ...
class InvalidArgument(DockerException): ...
class DeprecatedMethod(DockerException): ...

class TLSParameterError(DockerException):
    msg: str
    def __init__(self, msg: str) -> None: ...

class NullResource(DockerException, ValueError): ...

class ContainerError(DockerException):
    container: Incomplete
    exit_status: Incomplete
    command: Incomplete
    image: Incomplete
    stderr: Incomplete
    def __init__(self, container, exit_status, command, image, stderr) -> None: ...

class StreamParseError(RuntimeError):
    msg: Incomplete
    def __init__(self, reason) -> None: ...

class BuildError(DockerException):
    msg: Incomplete
    build_log: Incomplete
    def __init__(self, reason, build_log) -> None: ...

class ImageLoadError(DockerException): ...

def create_unexpected_kwargs_error(name, kwargs): ...

class MissingContextParameter(DockerException):
    param: str
    def __init__(self, param) -> None: ...

class ContextAlreadyExists(DockerException):
    name: str
    def __init__(self, name) -> None: ...

class ContextException(DockerException):
    msg: str
    def __init__(self, msg) -> None: ...

class ContextNotFound(DockerException):
    name: str
    def __init__(self, name) -> None: ...
