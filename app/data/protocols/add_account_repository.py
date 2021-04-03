import abc

from app.domain.models.account import AccountModel
from app.domain.usecases.add_account import AddAccountModel


class AddAccountRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, account_data: AddAccountModel) -> AccountModel:
        raise NotImplementedError(
            "Every AddAccountRepository must implement a add method."
        )  # pragma: no cover
