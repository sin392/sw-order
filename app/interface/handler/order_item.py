from typing import List
from abc import ABC, abstractmethod

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
    def delete(self, order) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[OrderItem]:
        raise NotImplementedError()


class OrderItemHandler:
    def __init__(self, usecase: IOrderItemUsecase) -> None:
        self.usecase = usecase

    def get_orders_order_id_items_order_item_id(self, order_item_id: str) -> OrderItem:
        return self.usecase.find(order_item_id)

    def post_orders_order_id_items(self, body: CreateOrderItemRequest) -> None:
        return self.usecase.save(body)

    def put_orders_order_id_items_order_item_id(self, order_item_id: str, body: CreateOrderItemRequest) -> None:
        return self.usecase.update(order_item_id, body)

    def delete_orders_order_id_items_order_item_id(self, order_item_id: str) -> None:
        return self.usecase.delete(order_item_id)

    def get_orders_order_id_items(self) -> List[OrderItem]:
        return self.usecase.list()
