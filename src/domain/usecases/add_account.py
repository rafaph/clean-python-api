import abc
from typing import TypedDict

from src.domain.models.account import AccountModel


class AddAccountModel(TypedDict):
    name: str
    email: str
    password: str


class AddAccount(abc.ABC):
    @abc.abstractmethod
    def add(self, account: AddAccountModel) -> AccountModel:
        raise NotImplementedError("Every AddAccount must implement a add method.")
