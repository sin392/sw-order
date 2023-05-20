# generated by fastapi-codegen:
#   filename:  openapi.yml
#   timestamp: 2023-05-20T18:42:46+00:00

from __future__ import annotations

from fastapi import FastAPI
from infra.database import SessionLocal
from interface.handler import *
from interface.handler.dto import *

app = FastAPI(
    title='API Title',
    version='1.0',
    servers=[{'url': 'http://localhost:8000'}],
)


# NOTE: must import dependency after database
from dependency import Dependency  # type: ignore # noqa

injector = Dependency(db=SessionLocal())  # DI container
