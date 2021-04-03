from unittest import TestCase, mock

from app.utils.email_validator import EmailValidatorAdapter


class EmailValidatorAdapterTests(TestCase):
    """
    EmailValidator Adapter
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.is_email_patcher = mock.patch("app.utils.email_validator.validators.email")

    def setUp(self) -> None:
        self.is_email = self.is_email_patcher.start()
        self.is_email.return_value = True

    def tearDown(self) -> None:
        self.is_email_patcher.stop()

    def test_return_false_if_validator_returns_false(self):
        """
        Should return false if validator returns false
        """
        self.is_email.return_value = False
        sut = EmailValidatorAdapter()
        is_valid = sut.is_valid("invalid_email@mail.com")
        self.assertFalse(is_valid)

    def test_return_true_if_validattor_returns_true(self):
        """
        Should return true if validator returns true
        """
        sut = EmailValidatorAdapter()
        is_valid = sut.is_valid("valid_email@mail.com")
        self.assertTrue(is_valid)
