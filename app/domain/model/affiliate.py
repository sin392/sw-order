from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, validator
from pydantic.fields import ModelField

# 以下をコメントインすると循環参照になる
# from .user import BaseUserDOM


class _UserID(BaseModel):
    id: str

    class Config:
        orm_mode = True


class AffiliateDOM(BaseModel):
    id: Optional[UUID]
    name: str
    postcode: str
    address: str
    tel: str
    fax: Optional[str]
    email: Optional[str]
    created_at: Optional[datetime]  # server_default
    updated_at: Optional[datetime]  # server_default
    users: Optional[List[_UserID]]

    class Config:
        orm_mode = True

    @validator('name', 'postcode', 'address', 'tel')
    def prohibit_empty_str(cls, v: str, field: ModelField) -> str:
        if len(v) == 0:
            raise ValueError(f'{field}には1文字以上の文字列を指定してください')
        return v

    def update(self, obj_dict: dict):
        for k, v in obj_dict.items():
            if v is not None:
                setattr(self, k, v)

    def to_rdb_dict(self) -> dict:
        params = {**self.dict()}
        params.pop('users')
        return params
