import abc


class Encrypter(abc.ABC):
    @abc.abstractmethod
    def encrypt(self, value: str) -> str:
        raise NotImplementedError(
            "Every Encrypter must implement a encrypt method."
        )  # pragma: no cover
