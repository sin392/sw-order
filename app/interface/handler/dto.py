# generated by fastapi-codegen:
#   filename:  /home/docs/openapi/openapi.yml
#   timestamp: 2023-05-21T04:06:58+00:00

from __future__ import annotations

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, conint, constr


class UUIDModel(BaseModel):
    __root__: UUID


class OrderID(BaseModel):
    id: UUIDModel = Field(..., description='注文ID')


class Item(BaseModel):
    id: UUID = Field(..., description='商品ID')
    name: constr(min_length=1, max_length=255) = Field(
        ..., description='商品名', example='○○商店缶バッジ'
    )
    description: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description='商品説明', example='○○商店の缶バッジです！！'
    )
    img_src: Optional[constr(min_length=1, max_length=255)] = Field(
        None, example='http://localhost:8000/static/no-image.png'
    )
    category: conint(ge=-1) = Field(..., description='カテゴリ(0:缶バッジ, -1:その他)', example=0)
    type: conint(ge=-1) = Field(..., description='タイプ(0:通常, 1:限定, -1:その他)', example=0)
    unit_price: conint(ge=0) = Field(..., description='単価', example=300)
    sales_start: Optional[datetime] = Field(None, description='作成日')
    sales_end: Optional[datetime] = Field(None, description='作成日')
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')


class OrderItemID(BaseModel):
    id: UUIDModel = Field(..., description='注文明細ID')


class PurchaseRight(BaseModel):
    id: UUID = Field(..., description='購入権ID')
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')
    affiliate_id: UUID
    item_id: UUID


class CreateUserRequest(BaseModel):
    first_name: constr(min_length=1, max_length=255) = Field(
        ..., description='名', example='太郎'
    )
    last_name: constr(min_length=1, max_length=255) = Field(
        ..., description='姓', example='山田'
    )
    tel: Optional[constr(min_length=13, max_length=13)] = Field(
        None, description='電話番号', example='000-0000-0000'
    )
    email: Optional[constr(min_length=3, max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )
    affiliate_id: Optional[UUID] = Field(None, description='加盟組織ID')


class UpdateUserRequest(BaseModel):
    first_name: Optional[constr(min_length=1, max_length=255)] = Field(
        None, description='名', example='太郎'
    )
    last_name: Optional[constr(min_length=1, max_length=255)] = Field(
        None, description='姓', example='山田'
    )
    tel: Optional[constr(min_length=13, max_length=13)] = Field(
        None, description='電話番号', example='000-0000-0000'
    )
    email: Optional[constr(min_length=3, max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )


class CreateAffiliateRequest(BaseModel):
    name: constr(min_length=1, max_length=255) = Field(
        ..., description='組織名', example='株式会社サンプル'
    )
    postcode: constr(min_length=8, max_length=8) = Field(
        ..., description='郵便番号', example='000-0000'
    )
    address: constr(min_length=1, max_length=255) = Field(
        ..., description='住所', example='静岡県沼津市上土町36'
    )
    tel: constr(min_length=13, max_length=13) = Field(
        ..., description='電話番号', example='000-0000-0000'
    )
    fax: Optional[constr(min_length=13, max_length=13)] = Field(
        None, description='FAX番号', example='000-0000-0000'
    )
    email: Optional[constr(min_length=3, max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )


class UpdateAffiliateRequest(BaseModel):
    name: Optional[constr(min_length=1, max_length=255)] = Field(
        None, description='組織名', example='株式会社サンプル'
    )
    postcode: Optional[constr(min_length=8, max_length=8)] = Field(
        None, description='郵便番号', example='000-0000'
    )
    address: Optional[constr(min_length=1, max_length=255)] = Field(
        None, description='住所', example='静岡県沼津市上土町36'
    )
    tel: Optional[constr(min_length=13, max_length=13)] = Field(
        None, description='電話番号', example='000-0000-0000'
    )
    fax: Optional[constr(min_length=13, max_length=13)] = Field(
        None, description='FAX番号', example='000-0000-0000'
    )
    email: Optional[constr(min_length=3, max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )


class CreateItemRequest(BaseModel):
    name: constr(min_length=1, max_length=255) = Field(
        ..., description='商品名', example='○○商店缶バッジ'
    )
    description: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description='商品説明', example='○○商店の缶バッジです！！'
    )
    img_src: Optional[constr(min_length=1, max_length=255)] = Field(
        None, example='http://localhost:8000/static/no-image.png'
    )
    category: Optional[conint(ge=-1)] = Field(
        None, description='カテゴリ(0:缶バッジ, -1:その他)', example=0
    )
    type: Optional[conint(ge=-1)] = Field(
        None, description='タイプ(0:通常, 1:限定, -1:その他)', example=0
    )
    unit_price: conint(ge=0) = Field(..., description='単価', example=300)
    sales_start: Optional[datetime] = Field(None, description='作成日')
    sales_end: Optional[datetime] = Field(None, description='作成日')


class UpdateItemRequest(BaseModel):
    name: Optional[constr(min_length=1, max_length=255)] = Field(
        None, description='商品名', example='○○商店缶バッジ'
    )
    description: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description='商品説明', example='○○商店の缶バッジです！！'
    )
    img_src: Optional[constr(min_length=1, max_length=255)] = Field(
        None, example='http://localhost:8000/static/no-image.png'
    )
    category: Optional[conint(ge=-1)] = Field(
        None, description='カテゴリ(0:缶バッジ, -1:その他)', example=0
    )
    unit_price: Optional[conint(ge=0)] = Field(None, description='単価', example=300)
    sales_start: Optional[datetime] = Field(None, description='作成日')
    sales_end: Optional[datetime] = Field(None, description='作成日')


class CreateOrderRequest(BaseModel):
    postcode: constr(min_length=8, max_length=8) = Field(
        ..., description='届け先郵便番号', example='000-0000'
    )
    address: constr(min_length=1, max_length=255) = Field(
        ..., description='届け先住所', example='静岡県沼津市上土町36'
    )
    approved_flag: Optional[bool] = Field(False, description='承認フラグ', example=False)
    affiliate_id: UUID = Field(..., description='加盟組織ID')
    user_id: UUID = Field(..., description='ユーザID')


class UpdateOrderRequest(BaseModel):
    postcode: Optional[constr(min_length=8, max_length=8)] = Field(
        None, description='届け先郵便番号', example='000-0000'
    )
    address: Optional[constr(min_length=1, max_length=255)] = Field(
        None, description='届け先住所', example='静岡県沼津市上土町36'
    )
    approved_flag: Optional[bool] = Field(False, description='承認フラグ', example=False)


class CreateOrderItemRequest(BaseModel):
    quantity: conint(ge=1) = Field(..., description='個数', example=1)
    order_id: UUID = Field(..., description='注文ID')
    item_id: UUID = Field(..., description='商品ID')


class UpdateOrderItemRequest(BaseModel):
    quantity: Optional[conint(ge=1)] = Field(None, description='個数', example=1)


class CreatePurchaseRightRequest(BaseModel):
    affiliate_id: UUID = Field(..., description='加盟組織ID')
    item_id: UUID = Field(..., description='商品ID')


class UpdatePurchaseRightRequest(BaseModel):
    affiliate_id: Optional[UUID] = Field(None, description='加盟組織ID')
    item_id: Optional[UUID] = Field(None, description='商品ID')


class UserID(BaseModel):
    id: UUIDModel = Field(..., description='ユーザID')


class Affiliate(BaseModel):
    id: UUID = Field(..., description='加盟組織ID')
    name: constr(min_length=1, max_length=255) = Field(
        ..., description='組織名', example='株式会社サンプル'
    )
    postcode: constr(min_length=8, max_length=8) = Field(
        ..., description='郵便番号', example='000-0000'
    )
    address: constr(min_length=1, max_length=255) = Field(
        ..., description='住所', example='静岡県沼津市上土町36'
    )
    tel: constr(min_length=13, max_length=13) = Field(
        ..., description='電話番号', example='000-0000-0000'
    )
    fax: Optional[constr(min_length=13, max_length=13)] = Field(
        None, description='FAX番号', example='000-0000-0000'
    )
    email: Optional[constr(min_length=3, max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')
    users: Optional[List[UserID]] = None
    orders: Optional[List[OrderID]] = None


class User(BaseModel):
    id: UUID = Field(..., description='ユーザID')
    first_name: constr(min_length=1, max_length=255) = Field(
        ..., description='名', example='太郎'
    )
    last_name: constr(min_length=1, max_length=255) = Field(
        ..., description='姓', example='山田'
    )
    tel: constr(min_length=13, max_length=13) = Field(
        ..., description='電話番号', example='000-0000-0000'
    )
    email: Optional[constr(min_length=3, max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')
    affiliate: Optional[Affiliate] = None
    orders: Optional[List[OrderID]] = None


class Order(BaseModel):
    id: UUID = Field(..., description='注文ID')
    postcode: constr(min_length=8, max_length=8) = Field(
        ..., description='届け先郵便番号', example='000-0000'
    )
    address: constr(min_length=1, max_length=255) = Field(
        ..., description='届け先住所', example='静岡県沼津市上土町36'
    )
    approved_flag: bool = Field(..., description='承認フラグ', example=False)
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')
    affiliate: Affiliate
    user: User
    order_items: Optional[List[OrderItemID]] = None


class OrderItem(BaseModel):
    id: UUID = Field(..., description='注文明細ID')
    quantity: conint(ge=1) = Field(..., description='個数', example=1)
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')
    order: Order
    item: Item
