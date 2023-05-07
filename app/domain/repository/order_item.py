from typing import List
from abc import ABC, abstractmethod

from domain.model.order_item import OrderItemDOM


class IOrderItemRepository(ABC):
    @abstractmethod
    def find(self, order_item_id: str) -> OrderItemDOM:
        raise NotImplementedError()

    @abstractmethod
    def save(self, order: OrderItemDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, order: OrderItemDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, order: OrderItemDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[OrderItemDOM]:
        raise NotImplementedError()
