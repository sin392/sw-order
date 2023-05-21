from typing import List
from abc import ABC, abstractmethod

from domain.model.purchase_right import PurchaseRightDOM


class IPurchaseRightRepository(ABC):
    @abstractmethod
    def find(self, purchase_right_id: str) -> PurchaseRightDOM:
        raise NotImplementedError()

    @abstractmethod
    def save(self, purchase: PurchaseRightDOM) -> str:
        raise NotImplementedError()

    @abstractmethod
    def update(self, purchase: PurchaseRightDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, purchase: PurchaseRightDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[PurchaseRightDOM]:
        raise NotImplementedError()
