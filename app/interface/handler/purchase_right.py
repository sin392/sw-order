from typing import List
from abc import ABC, abstractmethod

from injector import inject

from .dto import CreatePurchaseRightRequest, UpdatePurchaseRightRequest, PurchaseRight


class IPurchaseRightUsecase(ABC):
    @abstractmethod
    def find(self, purchase_right_id: str) -> PurchaseRight:
        raise NotImplementedError()

    @abstractmethod
    def save(self, body: CreatePurchaseRightRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, purchase_right_id: str, body: UpdatePurchaseRightRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, purchase_right_id: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[PurchaseRight]:
        raise NotImplementedError()


class PurchaseRightHandler:
    @inject
    def __init__(self, usecase: IPurchaseRightUsecase) -> None:
        self.usecase = usecase

    def read_purchase_right(self, purchase_right_id: str) -> PurchaseRight:
        return self.usecase.find(purchase_right_id)

    def create_purchase_right(self, body: CreatePurchaseRightRequest) -> None:
        return self.usecase.save(body)

    def update_purchase_right(self, purchase_right_id: str, body: CreatePurchaseRightRequest) -> None:
        return self.usecase.update(purchase_right_id, body)

    def delete_purchase_right(self, purchase_right_id: str) -> None:
        return self.usecase.delete(purchase_right_id)

    def read_purchase_rights(self) -> List[PurchaseRight]:
        return self.usecase.list()
