import abc

from pydantic import BaseModel

from app.domain.models.account import AccountModel


class AddAccountModel(BaseModel):
    name: str
    email: str
    password: str


class AddAccount(abc.ABC):
    @abc.abstractmethod
    def add(self, account_data: AddAccountModel) -> AccountModel:
        raise NotImplementedError(
            "Every AddAccount must implement a add method."
        )  # pragma: no cover


__all__ = ["AddAccountModel", "AddAccount"]
