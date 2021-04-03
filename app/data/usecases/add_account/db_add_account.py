from app.data.protocols.encrypter import Encrypter
from app.domain.models.account import AccountModel
from app.domain.usecases.add_account import AddAccount, AddAccountModel


class DbAddAccount(AddAccount):
    def __init__(self, encrypter: Encrypter):
        self._encrypter = encrypter

    def add(self, account: AddAccountModel) -> AccountModel:
        self._encrypter.encrypt(account.password)
        pass
