# generated by fastapi-codegen:
#   filename:  openapi.yml
#   timestamp: 2023-05-21T07:12:16+00:00

from __future__ import annotations

from fastapi import FastAPI
from infra.database import SessionLocal
from interface.handler import *
from interface.handler.dto import *

app = FastAPI(
    title='API Title',
    version='1.0',
    license={
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html',
    },
    servers=[{'url': 'http://localhost:8000'}],
)


# NOTE: must import dependency after database
from dependency import Dependency  # type: ignore # noqa

injector = Dependency(db=SessionLocal())  # DI container


@app.get('/affiliates', response_model=List[Affiliate], tags=['Affiliate'])
async def read_affiliates() -> List[Affiliate]:
    """
    加盟組織一覧API
    """
    h = injector.resolve(AffiliateHandler)
    return h.read_affiliates()


@app.post('/affiliates', response_model=UUID, tags=['Affiliate'])
async def create_affiliate(body: CreateAffiliateRequest) -> UUID:
    """
    加盟組織作成API
    """
    h = injector.resolve(AffiliateHandler)
    return h.create_affiliate(
        body=body,
    )


@app.get('/affiliates/{affiliate_id}', response_model=Affiliate, tags=['Affiliate'])
async def read_affiliate(affiliate_id: UUID) -> Affiliate:
    """
    加盟組織取得API
    """
    h = injector.resolve(AffiliateHandler)
    return h.read_affiliate(
        affiliate_id=affiliate_id,
    )


@app.put('/affiliates/{affiliate_id}', response_model=None, tags=['Affiliate'])
async def update_affiliate(
    affiliate_id: UUID, body: UpdateAffiliateRequest = ...
) -> None:
    """
    加盟組織更新API
    """
    h = injector.resolve(AffiliateHandler)
    return h.update_affiliate(
        affiliate_id=affiliate_id,
        body=body,
    )


@app.delete('/affiliates/{affiliate_id}', response_model=None, tags=['Affiliate'])
async def delete_affiliate(affiliate_id: UUID) -> None:
    """
    加盟組織削除API
    """
    h = injector.resolve(AffiliateHandler)
    return h.delete_affiliate(
        affiliate_id=affiliate_id,
    )


@app.get('/items', response_model=List[Item], tags=['Item'])
async def read_items() -> List[Item]:
    """
    商品一覧API
    """
    h = injector.resolve(ItemHandler)
    return h.read_items()


@app.post('/items', response_model=UUID, tags=['Item'])
async def create_item(body: CreateItemRequest) -> UUID:
    """
    商品作成API
    """
    h = injector.resolve(ItemHandler)
    return h.create_item(
        body=body,
    )


@app.get('/items/{item_id}', response_model=Item, tags=['Item'])
async def read_item(item_id: UUID) -> Item:
    """
    商品取得API
    """
    h = injector.resolve(ItemHandler)
    return h.read_item(
        item_id=item_id,
    )


@app.put('/items/{item_id}', response_model=None, tags=['Item'])
async def update_item(item_id: UUID, body: UpdateItemRequest = ...) -> None:
    """
    商品更新API
    """
    h = injector.resolve(ItemHandler)
    return h.update_item(
        item_id=item_id,
        body=body,
    )


@app.delete('/items/{item_id}', response_model=None, tags=['Item'])
async def delete_item(item_id: UUID) -> None:
    """
    商品削除API
    """
    h = injector.resolve(ItemHandler)
    return h.delete_item(
        item_id=item_id,
    )


@app.get('/orders', response_model=List[Order], tags=['Order'])
async def read_orders() -> List[Order]:
    """
    注文一覧API
    """
    h = injector.resolve(OrderHandler)
    return h.read_orders()


@app.post('/orders', response_model=UUID, tags=['Order'])
async def create_order(body: CreateOrderRequest) -> UUID:
    """
    注文作成API
    """
    h = injector.resolve(OrderHandler)
    return h.create_order(
        body=body,
    )


@app.get('/orders/{order_id}', response_model=Order, tags=['Order'])
async def read_order(order_id: UUID) -> Order:
    """
    注文取得API
    """
    h = injector.resolve(OrderHandler)
    return h.read_order(
        order_id=order_id,
    )


@app.put('/orders/{order_id}', response_model=None, tags=['Order'])
async def update_order(order_id: UUID, body: UpdateOrderRequest = ...) -> None:
    """
    注文更新API
    """
    h = injector.resolve(OrderHandler)
    return h.update_order(
        order_id=order_id,
        body=body,
    )


@app.delete('/orders/{order_id}', response_model=None, tags=['Order'])
async def delete_order(order_id: UUID) -> None:
    """
    注文削除API
    """
    h = injector.resolve(OrderHandler)
    return h.delete_order(
        order_id=order_id,
    )


@app.get('/orders/{order_id}/items', response_model=List[OrderItem], tags=['OrderItem'])
async def read_order_items(order_id: UUID) -> List[OrderItem]:
    """
    注文明細一覧API
    """
    h = injector.resolve(OrderItemHandler)
    return h.read_order_items(
        order_id=order_id,
    )


@app.post('/orders/{order_id}/items', response_model=UUID, tags=['OrderItem'])
async def create_order_item(order_id: UUID, body: CreateOrderItemRequest = ...) -> UUID:
    """
    注文明細作成API
    """
    h = injector.resolve(OrderItemHandler)
    return h.create_order_item(
        order_id=order_id,
        body=body,
    )


@app.get(
    '/orders/{order_id}/items/{order_item_id}',
    response_model=OrderItem,
    tags=['OrderItem'],
)
async def read_order_item(order_id: UUID, order_item_id: UUID = ...) -> OrderItem:
    """
    商品明細取得API
    """
    h = injector.resolve(OrderItemHandler)
    return h.read_order_item(
        order_id=order_id,
        order_item_id=order_item_id,
    )


@app.put(
    '/orders/{order_id}/items/{order_item_id}', response_model=None, tags=['OrderItem']
)
async def update_order_item(
    order_id: UUID, order_item_id: UUID = ..., body: UpdateOrderItemRequest = ...
) -> None:
    """
    商品明細更新API
    """
    h = injector.resolve(OrderItemHandler)
    return h.update_order_item(
        order_id=order_id,
        order_item_id=order_item_id,
        body=body,
    )


@app.delete(
    '/orders/{order_id}/items/{order_item_id}', response_model=None, tags=['OrderItem']
)
async def delete_order_item(order_id: UUID, order_item_id: UUID = ...) -> None:
    """
    商品明細削除API
    """
    h = injector.resolve(OrderItemHandler)
    return h.delete_order_item(
        order_id=order_id,
        order_item_id=order_item_id,
    )


@app.get('/purchase_rights', response_model=List[PurchaseRight], tags=['PurchaseRight'])
async def read_purchase_rights() -> List[PurchaseRight]:
    """
    購入権一覧API
    """
    h = injector.resolve(PurchaseRightHandler)
    return h.read_purchase_rights()


@app.post('/purchase_rights', response_model=UUID, tags=['PurchaseRight'])
async def create_purchase_right(body: CreatePurchaseRightRequest) -> UUID:
    """
    購入権作成API
    """
    h = injector.resolve(PurchaseRightHandler)
    return h.create_purchase_right(
        body=body,
    )


@app.get(
    '/purchase_rights/{purchase_right_id}', response_model=UUID, tags=['PurchaseRight']
)
async def read_purchase_right(purchase_right_id: UUID) -> UUID:
    """
    購入権取得API
    """
    h = injector.resolve(PurchaseRightHandler)
    return h.read_purchase_right(
        purchase_right_id=purchase_right_id,
    )


@app.put(
    '/purchase_rights/{purchase_right_id}', response_model=None, tags=['PurchaseRight']
)
async def update_purchase_right(
    purchase_right_id: UUID, body: UpdatePurchaseRightRequest = ...
) -> None:
    """
    購入権更新API
    """
    h = injector.resolve(PurchaseRightHandler)
    return h.update_purchase_right(
        purchase_right_id=purchase_right_id,
        body=body,
    )


@app.delete(
    '/purchase_rights/{purchase_right_id}', response_model=None, tags=['PurchaseRight']
)
async def delete_purchase_right(purchase_right_id: UUID) -> None:
    """
    購入権削除API
    """
    h = injector.resolve(PurchaseRightHandler)
    return h.delete_purchase_right(
        purchase_right_id=purchase_right_id,
    )


@app.get('/users', response_model=List[User], tags=['User'])
async def read_users() -> List[User]:
    """
    ユーザ一覧API
    """
    h = injector.resolve(UserHandler)
    return h.read_users()


@app.post('/users', response_model=UUID, tags=['User'])
async def create_user(body: CreateUserRequest) -> UUID:
    """
    ユーザ作成API
    """
    h = injector.resolve(UserHandler)
    return h.create_user(
        body=body,
    )


@app.get('/users/{user_id}', response_model=User, tags=['User'])
async def read_user(user_id: UUID) -> User:
    """
    ユーザ取得API
    """
    h = injector.resolve(UserHandler)
    return h.read_user(
        user_id=user_id,
    )


@app.put('/users/{user_id}', response_model=None, tags=['User'])
async def update_user(user_id: UUID, body: UpdateUserRequest = ...) -> None:
    """
    ユーザ更新API
    """
    h = injector.resolve(UserHandler)
    return h.update_user(
        user_id=user_id,
        body=body,
    )


@app.delete('/users/{user_id}', response_model=None, tags=['User'])
async def delete_user(user_id: UUID) -> None:
    """
    ユーザ削除API
    """
    h = injector.resolve(UserHandler)
    return h.delete_user(
        user_id=user_id,
    )
