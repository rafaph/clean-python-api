import os

from app.infra.db.mongodb.helpers.mongo_helper import MongoHelper
from app.main.config import make_app

app = make_app()


@app.on_event("startup")
def startup():
    MongoHelper.connect(url=os.environ["MONGO_URL"])


@app.on_event("shutdown")
def shutdown():
    MongoHelper.disconnect()


__all__ = ["app"]
