class MissingParamError(Exception):
    def __init__(self, param_name: str):
        self.param_name = param_name
        super().__init__(f"Missing param: {param_name}")

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return other.param_name == self.param_name
        return False
