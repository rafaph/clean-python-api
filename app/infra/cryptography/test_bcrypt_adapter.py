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
        cls.value = "any_value"
        cls.salt = "salt"
        cls.hash = "hash"

    def setUp(self) -> None:
        self.hashpw_stub = self.hashpw_patcher.start()
        self.hashpw_stub.return_value = self.hash.encode("utf-8")

        self.gensalt_stub = self.gensalt_patcher.start()
        self.gensalt_stub.return_value = self.salt.encode("utf-8")

    def tearDown(self) -> None:
        self.hashpw_patcher.stop()
        self.gensalt_patcher.stop()

    def test_call_gensalt_with_correct_value(self):
        """
        Should call bcrypt with correct values
        """
        sut = make_sut()
        sut.encrypt(self.value)
        self.gensalt_stub.assert_called_once_with(rounds)

    def test_call_hashpw_with_correct_values(self):
        """
        Should call hashpw with correct values
        """
        sut = make_sut()
        sut.encrypt(self.value)
        self.hashpw_stub.assert_called_once_with(
            self.value.encode("utf-8"), self.salt.encode("utf-8")
        )

    def test_returns_hash_on_success(self):
        """
        Should returns a hash on success
        """
        sut = make_sut()
        hashed_value = sut.encrypt(self.value)
        self.assertEqual(hashed_value, self.hash)

    def test_throw_if_hashpw_throws(self):
        """
        Should throw if hashpw throws
        """
        self.hashpw_stub.side_effect = ValueError()

        sut = make_sut()
        with self.assertRaises(ValueError):
            sut.encrypt(self.value)

    def test_throw_if_gensalt_throws(self):
        """
        Should throw if gensalt throws
        """
        self.gensalt_stub.side_effect = TypeError()

        sut = make_sut()
        with self.assertRaises(TypeError):
            sut.encrypt(self.value)
