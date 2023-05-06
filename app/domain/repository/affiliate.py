from typing import List
from abc import ABC, abstractmethod

from domain.model.affiliate import AffiliateDOM


class IAffiliateRepository(ABC):
    @abstractmethod
    def find(self, user_id: str) -> AffiliateDOM:
        raise NotImplementedError()

    @abstractmethod
    def save(self, user) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, user) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, user) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[AffiliateDOM]:
        raise NotImplementedError()
