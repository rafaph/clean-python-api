import validators

from app.presentation.protocols.email_validator import EmailValidator


class EmailValidatorAdapter(EmailValidator):
    def is_valid(self, email: str) -> bool:
        return validators.email(email)
