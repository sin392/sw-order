

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from .order import OrderDOM
from .item import ItemDOM


class OrderItemDOM(BaseModel):
    id: UUID
    quantity: int
    created_at: Optional[datetime]  # server_default
    updated_at: Optional[datetime]  # server_default
    order: OrderDOM
    item: ItemDOM

    class Config:
        orm_mode = True

    def update(self, obj_dict: dict):
        for k, v in obj_dict.items():
            if v is not None:
                setattr(self, k, v)

    def to_rdb_dict(self) -> dict:
        params = {
            **self.dict(),
            "order_id": self.order.id,
            "item_id": self.item.id
        }
        params.pop('order', None)
        params.pop('item', None)
        return params
