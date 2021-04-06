from fastapi import APIRouter

from app.main.adapters import adapt_route
from app.main.factories import make_sign_up_controller


def register(router: APIRouter) -> None:
    router.post("/signup")(adapt_route(make_sign_up_controller()))
