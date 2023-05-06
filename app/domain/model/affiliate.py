from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator
from pydantic.fields import ModelField

from .user import UserDOM


# エンティティ
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
    user: Optional[UserDOM]

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
