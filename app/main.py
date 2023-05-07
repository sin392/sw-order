# generated by fastapi-codegen:
#   filename:  openapi.yml
#   timestamp: 2023-05-07T06:13:11+00:00

from __future__ import annotations

from typing import List
from uuid import UUID

from fastapi import FastAPI
from infra.database import SessionLocal
from infra.repository import *
from interface.handler import *
from usecase import *

from interface.handler.dto import (
    Affiliate,
    CreateAffiliateRequest,
    CreateItemRequest,
    CreateOrderRequest,
    CreateUserRequest,
    Item,
    Order,
    UpdateAffiliateRequest,
    UpdateItemRequest,
    UpdateOrderRequest,
    UpdateUserRequest,
    User,
)

app = FastAPI(
    title='API Title',
    version='1.0',
    servers=[{'url': 'http://localhost:8000'}],
)

db = SessionLocal()

# repository
userRepository = UserRepository(db)
affiliateRepository = AffiliateRepository(db)
itemRepository = ItemRepository(db)
# service
# usecase
userUsecase = UserUsecase(userRepository, affiliateRepository)
affiliateUsecase = AffiliateUsecase(affiliateRepository)
itemUsecase = ItemUsecase(itemRepository)
# handler
userHandler = UserHandler(userUsecase)
affiliateHandler = AffiliateHandler(affiliateUsecase)
itemHandler = ItemHandler(itemUsecase)


@app.get('/affiliates', response_model=List[Affiliate], tags=['Affiliate'])
async def get_affiliates() -> List[Affiliate]:
    return affiliateHandler.get_affiliates()


@app.post('/affiliates', response_model=None, tags=['Affiliate'])
async def post_affiliates(body: CreateAffiliateRequest) -> None:
    return affiliateHandler.post_affiliates(
        body=body,
    )


@app.get('/affiliates/{affiliate_id}', response_model=Affiliate, tags=['Affiliate'])
async def get_affiliates_affiliate_id(affiliate_id: UUID) -> Affiliate:
    return affiliateHandler.get_affiliates_affiliate_id(
        affiliate_id=affiliate_id,
    )


@app.put('/affiliates/{affiliate_id}', response_model=None, tags=['Affiliate'])
async def put_affiliates_affiliate_id(
    affiliate_id: UUID, body: UpdateAffiliateRequest = ...
) -> None:
    return affiliateHandler.put_affiliates_affiliate_id(
        affiliate_id=affiliate_id,
        body=body,
    )


@app.delete('/affiliates/{affiliate_id}', response_model=None, tags=['Affiliate'])
async def delete_affiliates_affiliate_id(affiliate_id: UUID) -> None:
    return affiliateHandler.delete_affiliates_affiliate_id(
        affiliate_id=affiliate_id,
    )


@app.get('/items', response_model=List[Item], tags=['Item'])
async def get_items() -> List[Item]:
    return itemHandler.get_items()


@app.post('/items', response_model=None, tags=['Item'])
async def post_items(body: CreateItemRequest) -> None:
    return itemHandler.post_items(
        body=body,
    )


@app.get('/items/{item_id}', response_model=Item, tags=['Item'])
async def get_items_item_id(item_id: UUID) -> Item:
    return itemHandler.get_items_item_id(
        item_id=item_id,
    )


@app.put('/items/{item_id}', response_model=None, tags=['Item'])
async def put_items_item_id(item_id: UUID, body: UpdateItemRequest = ...) -> None:
    return itemHandler.put_items_item_id(
        item_id=item_id,
        body=body,
    )


@app.delete('/items/{item_id}', response_model=None, tags=['Item'])
async def delete_items_item_id(item_id: UUID) -> None:
    return itemHandler.delete_items_item_id(
        item_id=item_id,
    )


@app.get('/orders', response_model=List[Order], tags=['Order'])
async def get_orders() -> List[Order]:
    return orderHandler.get_orders()


@app.post('/orders', response_model=None, tags=['Order'])
async def post_orders(body: CreateOrderRequest) -> None:
    return orderHandler.post_orders(
        body=body,
    )


@app.get('/orders/{order_id}', response_model=Order, tags=['Order'])
async def get_orders_order_id(order_id: UUID) -> Order:
    return orderHandler.get_orders_order_id(
        order_id=order_id,
    )


@app.put('/orders/{order_id}', response_model=None, tags=['Order'])
async def put_orders_order_id(order_id: UUID, body: UpdateOrderRequest = ...) -> None:
    return orderHandler.put_orders_order_id(
        order_id=order_id,
        body=body,
    )


@app.delete('/orders/{order_id}', response_model=None, tags=['Order'])
async def delete_orders_order_id(order_id: UUID) -> None:
    return orderHandler.delete_orders_order_id(
        order_id=order_id,
    )


@app.get('/users', response_model=List[User], tags=['User'])
async def get_users() -> List[User]:
    return userHandler.get_users()


@app.post('/users', response_model=None, tags=['User'])
async def post_users(body: CreateUserRequest) -> None:
    return userHandler.post_users(
        body=body,
    )


@app.get('/users/{user_id}', response_model=User, tags=['User'])
async def get_users_user_id(user_id: UUID) -> User:
    return userHandler.get_users_user_id(
        user_id=user_id,
    )


@app.put('/users/{user_id}', response_model=None, tags=['User'])
async def put_users_user_id(user_id: UUID, body: UpdateUserRequest = ...) -> None:
    return userHandler.put_users_user_id(
        user_id=user_id,
        body=body,
    )


@app.delete('/users/{user_id}', response_model=None, tags=['User'])
async def delete_users_user_id(user_id: UUID) -> None:
    return userHandler.delete_users_user_id(
        user_id=user_id,
    )
