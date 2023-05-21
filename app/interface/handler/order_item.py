from typing import List
from abc import ABC, abstractmethod

from injector import inject

from .dto import CreateOrderItemRequest, UpdateOrderItemRequest, OrderItem


class IOrderItemUsecase(ABC):
    @abstractmethod
    def find(self, order_item_id: str) -> OrderItem:
        raise NotImplementedError()

    @abstractmethod
    def save(self, body: CreateOrderItemRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, order_item_id: str, body: UpdateOrderItemRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, order_item_id: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[OrderItem]:
        raise NotImplementedError()


class OrderItemHandler:
    @inject
    def __init__(self, usecase: IOrderItemUsecase) -> None:
        self.usecase = usecase

    def read_order_item(self, order_item_id: str) -> OrderItem:
        return self.usecase.find(order_item_id)

    def create_order_item(self, body: CreateOrderItemRequest) -> None:
        return self.usecase.save(body)

    def update_order_item(self, order_item_id: str, body: CreateOrderItemRequest) -> None:
        return self.usecase.update(order_item_id, body)

    def delete_order_item(self, order_item_id: str) -> None:
        return self.usecase.delete(order_item_id)

    def read_order_items(self) -> List[OrderItem]:
        return self.usecase.list()
