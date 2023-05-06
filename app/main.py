# generated by fastapi-codegen:
#   filename:  openapi.yml
#   timestamp: 2023-05-06T06:30:48+00:00

from __future__ import annotations

from typing import List

from fastapi import FastAPI
from infra.database import SessionLocal
from infra.repository import *
from interface.handler import *
from usecase import *

from usecase.dto import Affiliate, AffiliatesPostRequest, User, UsersPostRequest

app = FastAPI(
    title='API Title',
    version='1.0',
    servers=[{'url': 'https://api.server.test/v1'}],
)

db = SessionLocal()

# repository
userRepository = UserRepository(db)
affiliateRepository = AffiliateRepository(db)
# service
# usecase
userUsecase = UserUsecase(userRepository)
affiliateUsecase = AffiliateUsecase(affiliateRepository)
# handler
userHandler = UserHandler(userUsecase)
affiliateHandler = AffiliateHandler(affiliateUsecase)


@app.get('/affiliates', response_model=List[Affiliate], tags=['Affiliate'])
async def get_affiliates() -> List[Affiliate]:
    return affiliateHandler.get_affiliates()


@app.post('/affiliates', response_model=str, tags=['Affiliate'])
async def post_affiliates(body: AffiliatesPostRequest) -> str:
    return affiliateHandler.post_affiliates(
        body=body,
    )


@app.get('/users', response_model=List[User], tags=['User'])
async def get_users() -> List[User]:
    return userHandler.get_users()


@app.post('/users', response_model=str, tags=['User'])
async def post_users(body: UsersPostRequest) -> str:
    return userHandler.post_users(
        body=body,
    )
