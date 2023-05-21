from typing import List
from uuid import uuid4

from injector import inject

from domain.model import AffiliateDOM
from domain.repository import IAffiliateRepository
from interface.handler.affiliate import IAffiliateUsecase
from interface.handler.dto import CreateAffiliateRequest, UpdateAffiliateRequest, Affiliate
from .util import dom_to_dto, dom_list_to_dto_list


class AffiliateUsecase(IAffiliateUsecase):
    @inject
    def __init__(self, repo: IAffiliateRepository) -> None:
        self.repo = repo

    def find(self, affiliate_id: str) -> Affiliate:
        dom_affiliate = self.repo.find(affiliate_id)
        return dom_to_dto(Affiliate, dom_affiliate)

    def save(self, body: CreateAffiliateRequest) -> str:
        params = {**body.dict(), "id": uuid4()}
        affiliate = AffiliateDOM(**params)
        return self.repo.save(affiliate)

    def update(self, affiliate_id: str, body: UpdateAffiliateRequest) -> None:
        affiliate = self.repo.find(affiliate_id)
        if affiliate is None:
            raise Exception(f'Affiliateが存在しません: {affiliate_id}')
        affiliate.update(body.dict())
        return self.repo.update(affiliate)

    def delete(self, affiliate_id: str) -> None:
        affiliate = self.repo.find(affiliate_id)
        if affiliate is None:
            raise Exception(f'Affiliateが存在しません: {affiliate_id}')
        self.repo.delete(affiliate)

    def list(self) -> List[Affiliate]:
        dom_affiliates = self.repo.list()
        return dom_list_to_dto_list(Affiliate, dom_affiliates)
