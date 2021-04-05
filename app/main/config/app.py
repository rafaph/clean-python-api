from fastapi import FastAPI

from .middlewares import setup_middlewares

app = FastAPI(debug=True)

setup_middlewares(app)
