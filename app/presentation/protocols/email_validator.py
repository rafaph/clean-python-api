import abc


class EmailValidator(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, email: str) -> bool:
        raise NotImplementedError(
            "Every EmailValidator must implement a is_valid."
        )  # pragma: no cover
