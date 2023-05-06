# generated by fastapi-codegen:
#   filename:  /home/docs/openapi.yml
#   timestamp: 2023-05-06T14:35:46+00:00

from __future__ import annotations

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, constr


class BaseUser(BaseModel):
    id: UUID = Field(..., description='ユーザID')


class Affiliate(BaseModel):
    id: UUID = Field(..., description='加盟組織ID')
    name: constr(max_length=255) = Field(..., description='組織名', example='株式会社サンプル')
    postcode: constr(max_length=8) = Field(..., description='郵便番号', example='000-0000')
    address: constr(max_length=255) = Field(
        ..., description='住所', example='静岡県沼津市上土町36'
    )
    tel: constr(max_length=13) = Field(..., description='電話番号', example='000-0000-0000')
    fax: Optional[constr(max_length=13)] = Field(
        None, description='FAX番号', example='000-0000-0000'
    )
    email: Optional[constr(max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')
    users: Optional[List[BaseUser]] = None


class Item(BaseModel):
    id: UUID = Field(..., description='商品ID')
    name: constr(max_length=255) = Field(..., description='商品名', example='○○商店缶バッジ')
    description: Optional[constr(max_length=255)] = Field(
        None, description='商品名', example='○○商店の缶バッジです！！'
    )
    img_src: Optional[constr(max_length=255)] = Field(
        None, example='http://localhost:8000/static/no-image.png'
    )
    category: int = Field(..., description='カテゴリ(0:缶バッジ, -1:その他)', example=0)
    type: int = Field(..., description='タイプ(0:通常, 1:限定, -1:その他)', example=0)
    unit_price: int = Field(..., description='単価', example=300)
    sales_start: Optional[datetime] = Field(None, description='作成日')
    sales_end: Optional[datetime] = Field(None, description='作成日')
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')


class CreateUserRequest(BaseModel):
    first_name: constr(max_length=255) = Field(..., description='名', example='太郎')
    last_name: constr(max_length=255) = Field(..., description='姓', example='山田')
    tel: Optional[constr(max_length=255)] = Field(
        None, description='電話番号', example='000-0000-0000'
    )
    email: Optional[constr(max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )
    affiliate_id: Optional[UUID] = Field(None, description='加盟組織ID')


class UpdateUserRequest(BaseModel):
    first_name: Optional[constr(max_length=255)] = Field(
        None, description='名', example='太郎'
    )
    last_name: Optional[constr(max_length=255)] = Field(
        None, description='姓', example='山田'
    )
    tel: Optional[constr(max_length=255)] = Field(
        None, description='電話番号', example='000-0000-0000'
    )
    email: Optional[constr(max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )


class CreateAffiliateRequest(BaseModel):
    name: constr(max_length=255) = Field(..., description='組織名', example='株式会社サンプル')
    postcode: constr(max_length=8) = Field(..., description='郵便番号', example='000-0000')
    address: constr(max_length=255) = Field(
        ..., description='住所', example='静岡県沼津市上土町36'
    )
    tel: constr(max_length=13) = Field(..., description='電話番号', example='000-0000-0000')
    fax: Optional[constr(max_length=13)] = Field(
        None, description='FAX番号', example='000-0000-0000'
    )
    email: Optional[constr(max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )


class UpdateAffiliateRequest(BaseModel):
    name: Optional[constr(max_length=255)] = Field(
        None, description='組織名', example='株式会社サンプル'
    )
    postcode: Optional[constr(max_length=8)] = Field(
        None, description='郵便番号', example='000-0000'
    )
    address: Optional[constr(max_length=255)] = Field(
        None, description='住所', example='静岡県沼津市上土町36'
    )
    tel: Optional[constr(max_length=13)] = Field(
        None, description='電話番号', example='000-0000-0000'
    )
    fax: Optional[constr(max_length=13)] = Field(
        None, description='FAX番号', example='000-0000-0000'
    )
    email: Optional[constr(max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )


class CreateItemRequest(BaseModel):
    name: constr(max_length=255) = Field(..., description='商品名', example='○○商店缶バッジ')
    description: Optional[constr(max_length=255)] = Field(
        None, description='商品名', example='○○商店の缶バッジです！！'
    )
    img_src: Optional[constr(max_length=255)] = Field(
        None, example='http://localhost:8000/static/no-image.png'
    )
    category: Optional[int] = Field(None, description='カテゴリ(0:缶バッジ, -1:その他)', example=0)
    type: Optional[int] = Field(None, description='タイプ(0:通常, 1:限定, -1:その他)', example=0)
    unit_price: int = Field(..., description='単価', example=300)
    sales_start: Optional[datetime] = Field(None, description='作成日')
    sales_end: Optional[datetime] = Field(None, description='作成日')


class UpdateItemRequest(BaseModel):
    name: Optional[constr(max_length=255)] = Field(
        None, description='商品名', example='○○商店缶バッジ'
    )
    description: Optional[constr(max_length=255)] = Field(
        None, description='商品名', example='○○商店の缶バッジです！！'
    )
    img_src: Optional[constr(max_length=255)] = Field(
        None, example='http://localhost:8000/static/no-image.png'
    )
    category: Optional[int] = Field(None, description='カテゴリ(0:缶バッジ, -1:その他)', example=0)
    unit_price: Optional[int] = Field(None, description='単価', example=300)
    sales_start: Optional[datetime] = Field(None, description='作成日')
    sales_end: Optional[datetime] = Field(None, description='作成日')


class User(BaseModel):
    id: UUID = Field(..., description='ユーザID')
    first_name: constr(max_length=255) = Field(..., description='名', example='太郎')
    last_name: constr(max_length=255) = Field(..., description='姓', example='山田')
    tel: constr(max_length=13) = Field(..., description='電話番号', example='000-0000-0000')
    email: Optional[constr(max_length=255)] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')
    affiliate: Optional[Affiliate] = None
