# generated by fastapi-codegen:
#   filename:  /home/docs/openapi.yml
#   timestamp: 2023-05-04T12:43:39+00:00

from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class User(BaseModel):
    id: Optional[UUID] = Field(None, description='ユーザID')
    first_name: str = Field(..., description='名', example='太郎')
    last_name: str = Field(..., description='姓', example='山田')
    tel: str = Field(..., description='電話番号', example='000-0000-0000')
    email: Optional[str] = Field(None, description='電話番号', example='sample@sample.com')
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')


class Affiliate(BaseModel):
    id: Optional[UUID] = Field(None, description='加盟組織ID')
    name: str = Field(..., description='組織名', example='株式会社サンプル')
    postcode: str = Field(..., description='郵便番号', example='000-0000')
    address: str = Field(..., description='住所', example='静岡県沼津市上土町36')
    tel: str = Field(..., description='電話番号', example='000-0000-0000')
    fax: Optional[str] = Field(None, description='FAX番号', example='000-0000-0000')
    email: Optional[str] = Field(None, description='電話番号', example='sample@sample.com')
    created_at: datetime = Field(..., description='作成日')
    updated_at: datetime = Field(..., description='更新日')
    user: Optional[User] = None


class UsersPostRequest(BaseModel):
    first_name: str = Field(..., description='名', example='太郎')
    last_name: str = Field(..., description='姓', example='山田')
    tel: Optional[str] = Field(None, description='電話番号', example='000-0000-0000')
    email: Optional[str] = Field(
        None, description='メールアドレス', example='sample@sample.com'
    )


class AffiliatesPostRequest(BaseModel):
    name: str = Field(..., description='組織名', example='株式会社サンプル')
    postcode: str = Field(..., description='郵便番号', example='000-0000')
    address: str = Field(..., description='住所', example='静岡県沼津市上土町36')
    tel: str = Field(..., description='電話番号', example='000-0000-0000')
    fax: Optional[str] = Field(None, description='FAX番号', example='000-0000-0000')
    email: Optional[str] = Field(None, description='電話番号', example='sample@sample.com')
