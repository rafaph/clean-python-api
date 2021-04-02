class ServerError(Exception):
    def __init__(self):
        super().__init__("Internal server error")
        self.name = "ServerError"

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return other.name == self.name
        return False
