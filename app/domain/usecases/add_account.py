import abc
from dataclasses import dataclass

from app.domain.models.account import AccountModel


@dataclass
class AddAccountModel:
    name: str
    email: str
    password: str


class AddAccount(abc.ABC):
    @abc.abstractmethod
    def add(self, account: AddAccountModel) -> AccountModel:
        raise NotImplementedError(
            "Every AddAccount must implement a add method."
        )  # pragma: no cover


__all__ = ["AddAccountModel", "AddAccount"]
