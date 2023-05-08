from typing import List, Optional

from sqlalchemy.orm import Session
from injector import inject

from domain.repository import IOrderItemRepository
from domain.model import OrderItemDOM
from infra.schema import OrderItem
from .util import orm_to_dom, orm_list_to_dom_list


class OrderItemRepository(IOrderItemRepository):
    @inject
    def __init__(self, db: Session) -> None:
        self.db = db

    def find(self, order_item_id: str) -> Optional[OrderItemDOM]:
        orm_order_item = self.db.query(OrderItem).get(order_item_id)
        return orm_to_dom(OrderItemDOM, orm_order_item) if orm_order_item else None

    def save(self, order_item: OrderItemDOM) -> None:
        orm_order_item = OrderItem(**order_item.to_rdb_dict())
        try:
            self.db.add(orm_order_item)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def update(self, order_item: OrderItemDOM) -> None:
        try:
            orm_order_item = self.db.query(OrderItem).get(order_item.id)
            for k, v in order_item.dict().items():
                setattr(orm_order_item, k, v)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def delete(self, order_item: OrderItemDOM) -> None:
        try:
            orm_order_item = self.db.query(OrderItem).get(order_item.id)
            self.db.delete(orm_order_item)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def list(self) -> List[OrderItemDOM]:
        orm_order_items = self.db.query(OrderItem).all()
        return orm_list_to_dom_list(OrderItemDOM, orm_order_items)
