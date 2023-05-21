from typing import List, Optional

from sqlalchemy.orm import Session
from injector import inject

from domain.repository import IOrderRepository
from domain.model import OrderDOM
from infra.schema import Order
from .util import orm_to_dom, orm_list_to_dom_list


class OrderRepository(IOrderRepository):
    @inject
    def __init__(self, db: Session) -> None:
        self.db = db

    def find(self, order_id: str) -> Optional[OrderDOM]:
        orm_order = self.db.query(Order).get(order_id)
        return orm_to_dom(OrderDOM, orm_order) if orm_order else None

    def save(self, order: OrderDOM) -> str:
        orm_order = Order(**order.to_rdb_dict())
        try:
            self.db.add(orm_order)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()
        return orm_order.id

    def update(self, order: OrderDOM) -> None:
        try:
            orm_order = self.db.query(Order).get(order.id)
            for k, v in order.dict().items():
                setattr(orm_order, k, v)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def delete(self, order: OrderDOM) -> None:
        try:
            orm_order = self.db.query(Order).get(order.id)
            self.db.delete(orm_order)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def list(self) -> List[OrderDOM]:
        orm_orders = self.db.query(Order).all()
        return orm_list_to_dom_list(OrderDOM, orm_orders)
