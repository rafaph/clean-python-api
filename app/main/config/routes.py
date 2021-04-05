import importlib
from glob import iglob
from pathlib import Path

from fastapi import APIRouter, FastAPI

_routes_glob = f"{str(Path(__file__).parent.parent / 'routes')}/*_routes.py"


def setup_routes(app: FastAPI) -> None:
    router = APIRouter()

    for item in iglob(_routes_glob):
        importlib.import_module(f"app.main.routes.{Path(item).stem}").register(router)

    app.include_router(
        router, prefix="/api", responses={404: {"description": "Not found"}}
    )
