# generated by fastapi-codegen:
#   filename:  openapi.yml
#   timestamp: 2023-05-04T12:53:09+00:00

from __future__ import annotations

from fastapi import APIRouter

from ..dependencies import *

router = APIRouter(tags=['User'])


@router.get('/users', response_model=List[User], tags=['User'])
def get_users() -> List[User]:
    pass


@router.post('/users', response_model=str, tags=['User'])
def post_users(body: UsersPostRequest) -> str:
    pass
