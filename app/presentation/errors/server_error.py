from typing import Optional


class ServerError(Exception):
    def __init__(self, stack: Optional[str] = None):
        super().__init__("Internal Server Error")
        self.name = "ServerError"
        self.stack = stack

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return other.name == self.name and other.stack == self.stack
        return False  # pragma: no cover
