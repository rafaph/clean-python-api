from .db_add_account_protocols import (
    Encrypter,
    AddAccountModel,
    AccountModel,
    AddAccountRepository,
    AddAccount,
)


class DbAddAccount(AddAccount):
    def __init__(
        self, encrypter: Encrypter, add_account_repository: AddAccountRepository
    ):
        self._encrypter = encrypter
        self._add_account_repository = add_account_repository

    def add(self, account_data: AddAccountModel) -> AccountModel:
        hashed_password = self._encrypter.encrypt(account_data.password)
        account_data = account_data.copy(update={"password": hashed_password})
        return self._add_account_repository.add(account_data)
