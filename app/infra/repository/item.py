from typing import List, Optional

from sqlalchemy.orm import Session

from domain.repository import IItemRepository
from domain.model import ItemDOM
from infra.schema import Item
from .util import orm_to_dom, orm_list_to_dom_list


class ItemRepository(IItemRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def find(self, item_id: str) -> Optional[ItemDOM]:
        orm_item = self.db.query(Item).get(item_id)
        return orm_to_dom(ItemDOM, orm_item) if orm_item else None

    def save(self, item: ItemDOM) -> None:
        orm_item = Item(**item.to_rdb_dict())
        try:
            self.db.add(orm_item)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def update(self, item: ItemDOM) -> None:
        try:
            orm_item = self.db.query(Item).get(item.id)
            for k, v in item.dict().items():
                setattr(orm_item, k, v)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def delete(self, item: ItemDOM) -> None:
        try:
            orm_item = self.db.query(Item).get(item.id)
            self.db.delete(orm_item)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def list(self) -> List[ItemDOM]:
        orm_items = self.db.query(Item).all()
        return orm_list_to_dom_list(ItemDOM, orm_items)
