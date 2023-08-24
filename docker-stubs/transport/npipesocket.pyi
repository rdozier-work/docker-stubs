import io
from _typeshed import Incomplete

cERROR_PIPE_BUSY: int
cSECURITY_SQOS_PRESENT: int
cSECURITY_ANONYMOUS: int
MAXIMUM_RETRY_COUNT: int

def check_closed(f): ...

class NpipeSocket:
    def __init__(self, handle: Incomplete | None = ...) -> None: ...
    def accept(self) -> None: ...
    def bind(self, address) -> None: ...
    def close(self) -> None: ...
    flags: Incomplete
    def connect(self, address, retry_count: int = ...): ...
    def connect_ex(self, address): ...
    def detach(self): ...
    def dup(self): ...
    def getpeername(self): ...
    def getsockname(self): ...
    def getsockopt(self, level, optname, buflen: Incomplete | None = ...) -> None: ...
    def ioctl(self, control, option) -> None: ...
    def listen(self, backlog) -> None: ...
    def makefile(self, mode: Incomplete | None = ..., bufsize: Incomplete | None = ...): ...
    def recv(self, bufsize, flags: int = ...): ...
    def recvfrom(self, bufsize, flags: int = ...): ...
    def recvfrom_into(self, buf, nbytes: int = ..., flags: int = ...): ...
    def recv_into(self, buf, nbytes: int = ...): ...
    def send(self, string, flags: int = ...): ...
    def sendall(self, string, flags: int = ...): ...
    def sendto(self, string, address): ...
    def setblocking(self, flag): ...
    def settimeout(self, value) -> None: ...
    def gettimeout(self): ...
    def setsockopt(self, level, optname, value) -> None: ...
    def shutdown(self, how): ...

class NpipeFileIOBase(io.RawIOBase):
    sock: Incomplete
    def __init__(self, npipe_socket) -> None: ...
    def close(self) -> None: ...
    def fileno(self): ...
    def isatty(self): ...
    def readable(self): ...
    def readinto(self, buf): ...
    def seekable(self): ...
    def writable(self): ...