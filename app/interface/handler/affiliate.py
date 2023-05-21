from typing import List
from abc import ABC, abstractmethod

from injector import inject

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
    def delete(self, affiliate_id: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[Affiliate]:
        raise NotImplementedError()


class AffiliateHandler:
    @inject
    def __init__(self, usecase: IAffiliateUsecase) -> None:
        self.usecase = usecase

    def read_affiliate(self, affiliate_id: str) -> Affiliate:
        return self.usecase.find(affiliate_id)

    def create_affiliate(self, body: CreateAffiliateRequest) -> None:
        return self.usecase.save(body)

    def update_affiliate(self, affiliate_id: str, body: CreateAffiliateRequest) -> None:
        return self.usecase.update(affiliate_id, body)

    def delete_affiliate(self, affiliate_id: str) -> None:
        return self.usecase.delete(affiliate_id)

    def read_affiliates(self) -> List[Affiliate]:
        return self.usecase.list()
