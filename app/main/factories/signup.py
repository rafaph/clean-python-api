from app.data.usecases.add_account.db_add_account import DbAddAccount
from app.infra.cryptography.bcrypt_adapter import BcryptAdapter
from app.infra.db.mongodb.account_repository.account import AccountMongoRepository
from app.infra.db.mongodb.log_repository.log import LogErrorMongoRepository
from app.main.decorators.log import LogControllerDecorator
from app.presentation.controllers.signup.controller import SignUpController
from app.presentation.protocols import Controller
from app.utils.email_validator_adapter import EmailValidatorAdapter


def make_sign_up_controller() -> Controller:
    emil_validator = EmailValidatorAdapter()
    encrypter = BcryptAdapter(rounds=12)
    add_account_repository = AccountMongoRepository()
    add_account = DbAddAccount(encrypter, add_account_repository)

    sign_up_controller = SignUpController(emil_validator, add_account)
    log_error_repository = LogErrorMongoRepository()

    return LogControllerDecorator(sign_up_controller, log_error_repository)
