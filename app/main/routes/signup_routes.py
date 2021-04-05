from typing import Any

from fastapi import APIRouter, Body


def register(router: APIRouter) -> None:
    @router.post("/signup")
    def signup(data: Any = Body(...)):
        return {"ok": "ok"}
