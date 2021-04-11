from dataclasses import dataclass
from http import HTTPStatus
from unittest import TestCase, mock

import pytest

from app.main.decorators.log import LogControllerDecorator
from app.presentation.protocols import Controller, HttpRequest, HttpResponse


@dataclass
class SutTypes:
    controller_stub: Controller
    sut: LogControllerDecorator


def make_controller() -> Controller:
    class ControllerStub(Controller):
        def handle(self, http_request: HttpRequest) -> HttpResponse:
            return HttpResponse(status=HTTPStatus.NOT_FOUND, body=None)

    return ControllerStub()


def make_sut() -> SutTypes:
    controller_stub = make_controller()
    sut = LogControllerDecorator(controller_stub)

    return SutTypes(controller_stub=controller_stub, sut=sut)


@pytest.mark.unit
class LogControllerDecoratorTests(TestCase):
    """
    LogControllerDecorator
    """

    def test_call_controller_handle(self):
        """
        Should call controller handle
        """
        sut_types = make_sut()
        sut, controller_stub = sut_types.sut, sut_types.controller_stub

        http_request = HttpRequest()

        with mock.patch.object(controller_stub, "handle") as handle_spy:
            sut.handle(http_request)
            handle_spy.assert_called_once_with(http_request)
