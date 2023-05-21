

from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, validator
from pydantic.fields import ModelField

from .affiliate import AffiliateDOM
from .user import UserDOM


class _ID(BaseModel):
    id: UUID

    class Config:
        orm_mode = True


class OrderDOM(BaseModel):
    id: UUID
    postcode: str
    address: str
    approved_flag: bool
    created_at: Optional[datetime]  # server_default
    updated_at: Optional[datetime]  # server_default
    affiliate: AffiliateDOM
    user: UserDOM
    # 注文明細の持たせ方はもう少し検討が必要...
    order_items: Optional[List[_ID]]

    class Config:
        orm_mode = True

    @validator('postcode', 'address')
    def prohibit_empty_str(cls, v: str, field: ModelField) -> str:
        if len(v) == 0:
            raise ValueError(f'{field}には1文字以上の文字列を指定してください')
        return v

    def update(self, obj_dict: dict):
        for k, v in obj_dict.items():
            if v is not None:
                setattr(self, k, v)

    def to_rdb_dict(self) -> dict:
        params = {
            **self.dict(),
            "affiliate_id": self.affiliate.id,
            "user_id": self.user.id
        }
        params.pop('affiliate', None)
        params.pop('user', None)
        params.pop('items', None)
        return params
