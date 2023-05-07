from typing import List
from abc import ABC, abstractmethod

from domain.model.order import OrderDOM


class IOrderRepository(ABC):
    @abstractmethod
    def find(self, user_id: str) -> OrderDOM:
        raise NotImplementedError()

    @abstractmethod
    def save(self, order) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, order) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, order) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[OrderDOM]:
        raise NotImplementedError()
