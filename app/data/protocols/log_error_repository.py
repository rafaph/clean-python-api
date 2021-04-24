import abc


class LogErrorRepository(abc.ABC):
    @abc.abstractmethod
    def log_error(self, stack: str) -> None:
        raise NotImplementedError(
            "Every LogErrorRepository must implement a log method."
        )  # pragma: no cover
