from typing import List
from abc import ABC, abstractmethod

from domain.model.affiliate import AffiliateDOM


class IAffiliateRepository(ABC):
    @abstractmethod
    def find(self, affiliate_id: str) -> AffiliateDOM:
        raise NotImplementedError()

    @abstractmethod
    def save(self, affiliate: AffiliateDOM) -> str:
        raise NotImplementedError()

    @abstractmethod
    def update(self, affiliate: AffiliateDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, affiliate: AffiliateDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[AffiliateDOM]:
        raise NotImplementedError()
