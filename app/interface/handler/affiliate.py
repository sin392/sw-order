from typing import List
from abc import ABC, abstractmethod

from .dto import CreateAffiliateRequest, UpdateAffiliateRequest, Affiliate


class IAffiliateUsecase(ABC):
    @abstractmethod
    def find(self, affiliate_id: str) -> Affiliate:
        raise NotImplementedError()

    @abstractmethod
    def save(self, body: CreateAffiliateRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, affiliate_id: str, body: UpdateAffiliateRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, affiliate) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[Affiliate]:
        raise NotImplementedError()


class AffiliateHandler:
    def __init__(self, usecase: IAffiliateUsecase) -> None:
        self.usecase = usecase

    def get_affiliate_affiliate_id(self, affiliate_id: str) -> Affiliate:
        return self.usecase.find(affiliate_id)

    def post_affiliates(self, body: CreateAffiliateRequest) -> None:
        return self.usecase.save(body)

    def put_affiliate(self, affiliate_id: str, body: CreateAffiliateRequest) -> None:
        return self.usecase.update(affiliate_id, body)

    def delete_affiliate(self, affiliate_id: str) -> None:
        return self.usecase.delete(affiliate_id)

    def get_affiliates(self) -> List[Affiliate]:
        return self.usecase.list()
