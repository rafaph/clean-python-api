from unittest import TestCase, mock

import pytest

from app.data.protocols.encrypter import Encrypter
from .bcrypt_adapter import BcryptAdapter

rounds = 12


def make_sut() -> Encrypter:
    return BcryptAdapter(rounds)


@pytest.mark.unit
class BcryptAdapterTests(TestCase):
    """
    Bcrypt Adapter
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.hashpw_patcher = mock.patch(
            "app.infra.cryptography.bcrypt_adapter.bcrypt.hashpw"
        )
        cls.gensalt_patcher = mock.patch(
            "app.infra.cryptography.bcrypt_adapter.bcrypt.gensalt"
        )

    def setUp(self) -> None:
        self.hashpw_stub = self.hashpw_patcher.start()
        self.hashpw_stub.return_value = "hash".encode("utf-8")

        self.gensalt_stub = self.gensalt_patcher.start()
        self.gensalt_stub.return_value = "salt".encode("utf-8")

    def tearDown(self) -> None:
        self.hashpw_patcher.stop()
        self.gensalt_patcher.stop()

    def test_call_gensalt_with_correct_value(self):
        """
        Should call bcrypt with correct values
        """
        sut = make_sut()
        value = "any_value"
        sut.encrypt(value)
        self.gensalt_stub.assert_called_once_with(rounds)

    def test_call_hashpw_with_correct_values(self):
        """
        Should call hashpw with correct values
        """
        sut = make_sut()
        value = "any_value"
        sut.encrypt(value)
        self.hashpw_stub.assert_called_once_with(
            value.encode("utf-8"), "salt".encode("utf-8")
        )

    def test_returns_hash_on_success(self):
        """
        Should returns a hash on success
        """
        sut = make_sut()
        value = "any_value"
        hashed_value = sut.encrypt(value)
        self.assertEqual(hashed_value, "hash")
