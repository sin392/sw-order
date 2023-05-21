from typing import List, Optional

from sqlalchemy.orm import Session
from injector import inject

from domain.repository import IPurchaseRightRepository
from domain.model import PurchaseRightDOM
from infra.schema import PatchedPurchaseRight as PurchaseRight
from .util import orm_to_dom, orm_list_to_dom_list


class PurchaseRightRepository(IPurchaseRightRepository):
    @inject
    def __init__(self, db: Session) -> None:
        self.db = db

    def find(self, purchase_right_id: str) -> Optional[PurchaseRightDOM]:
        orm_purchase_right = self.db.query(
            PurchaseRight).get(purchase_right_id)
        return orm_to_dom(PurchaseRightDOM, orm_purchase_right) if orm_purchase_right else None

    def save(self, purchase_right: PurchaseRightDOM) -> str:
        orm_purchase_right = PurchaseRight(**purchase_right.to_rdb_dict())
        try:
            self.db.add(orm_purchase_right)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()
        return orm_purchase_right.id

    def update(self, purchase_right: PurchaseRightDOM) -> None:
        try:
            orm_purchase_right = self.db.query(
                PurchaseRight).get(purchase_right.id)
            for k, v in purchase_right.dict().items():
                setattr(orm_purchase_right, k, v)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def delete(self, purchase_right: PurchaseRightDOM) -> None:
        try:
            orm_purchase_right = self.db.query(
                PurchaseRight).get(purchase_right.id)
            self.db.delete(orm_purchase_right)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def list(self) -> List[PurchaseRightDOM]:
        orm_purchase_rights = self.db.query(PurchaseRight).all()
        return orm_list_to_dom_list(PurchaseRightDOM, orm_purchase_rights)
