

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class PurchaseRightDOM(BaseModel):
    id: UUID
    created_at: Optional[datetime]  # server_default
    updated_at: Optional[datetime]  # server_default
    affiliate_id: UUID
    item_id: UUID

    class Config:
        orm_mode = True

    def update(self, obj_dict: dict):
        for k, v in obj_dict.items():
            if v is not None:
                setattr(self, k, v)

    def to_rdb_dict(self) -> dict:
        params = self.dict()
        return params
