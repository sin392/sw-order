from typing import List, Optional

from sqlalchemy.orm import Session

from domain.repository.affiliate import IAffiliateRepository
from domain.model.affiliate import AffiliateDOM
from infra.schema import Affiliate
from .util import orm_to_dom, orm_list_to_dom_list


class AffiliateRepository(IAffiliateRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def find(self, affiliate_id: str) -> Optional[AffiliateDOM]:
        orm_affiliate = self.db.query(Affiliate).get(affiliate_id)
        return orm_to_dom(AffiliateDOM, orm_affiliate) if orm_affiliate else None

    def save(self, affiliate: AffiliateDOM) -> None:
        print(affiliate.to_rdb_dict())
        orm_affiliate = Affiliate(**affiliate.to_rdb_dict())
        try:
            self.db.add(orm_affiliate)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def update(self, affiliate: AffiliateDOM) -> None:
        try:
            orm_affiliate = self.db.query(Affiliate).get(affiliate.id)
            for k, v in affiliate.dict().items():
                setattr(orm_affiliate, k, v)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def delete(self, affiliate: AffiliateDOM) -> None:
        try:
            orm_affiliate = self.db.query(Affiliate).get(affiliate.id)
            self.db.delete(orm_affiliate)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def list(self) -> List[AffiliateDOM]:
        orm_affiliates = self.db.query(Affiliate).all()
        print(orm_affiliates)
        return orm_list_to_dom_list(AffiliateDOM, orm_affiliates)
