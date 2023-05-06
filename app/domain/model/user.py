from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator
from pydantic.fields import ModelField

from .affiliate import AffiliateDOM


class UserDOM(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    tel: str
    email: Optional[str]
    created_at: Optional[datetime]  # server_default
    updated_at: Optional[datetime]  # server_default
    affiliate: Optional[AffiliateDOM]

    class Config:
        orm_mode = True

    @validator('first_name', 'last_name', 'tel')
    def prohibit_empty_str(cls, v: str, field: ModelField) -> str:
        if len(v) == 0:
            raise ValueError(f'{field}には1文字以上の文字列を指定してください')
        return v

    def update(self, obj_dict: dict):
        for k, v in obj_dict.items():
            if v is not None:
                setattr(self, k, v)

    def to_rdb_dict(self) -> dict:
        params = {**self.dict(), "affiliate_id": self.affiliate.id}
        params.pop('affiliate')
        return params
