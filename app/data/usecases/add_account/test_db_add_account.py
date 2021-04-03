from unittest import TestCase, mock

from app.domain.usecases.add_account import AddAccountModel
from .db_add_account import DbAddAccount
from ...protocols.encrypter import Encrypter


class DbAddAccountTests(TestCase):
    """
    DbAddAccount Usecase
    """

    def test_call_encrypter_with_correct_password(self):
        """
        Should call Encrypter with correct password
        """

        class EncrypterStub(Encrypter):
            def encrypt(self, value: str) -> str:
                return "hashed_password"

        encrypter_stub = EncrypterStub()
        sut = DbAddAccount(encrypter_stub)
        account_data = AddAccountModel(
            name="valid_name", email="valid_email@mail.com", password="valid_password"
        )

        with mock.patch.object(encrypter_stub, "encrypt") as encrypt_spy:
            sut.add(account_data)
            encrypt_spy.assert_called_once_with("valid_password")
