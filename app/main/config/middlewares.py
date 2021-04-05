from fastapi import FastAPI

from ..middlewares import cors


def setup_middlewares(app: FastAPI) -> None:
    app.add_middleware(cors.middleware_class, **cors.params)
