from uuid import uuid4
from typing import List

from sqlalchemy.orm import Session

from domain.repository.affiliate import IAffiliateRepository
from domain.model.affiliate import AffiliateDOM
from infra.schema import Affiliate
from .util import orm_list_to_dom_list


class AffiliateRepository(IAffiliateRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self) -> List[AffiliateDOM]:
        orm_affiliates = self.db.query(Affiliate).all()
        return orm_list_to_dom_list(orm_affiliates)

    def save(self, affiliate: AffiliateDOM) -> None:
        params = {**affiliate.dict(), "id": uuid4()}
        orm_affiliate = Affiliate(**params)
        try:
            self.db.add(orm_affiliate)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()
