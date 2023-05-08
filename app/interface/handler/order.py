from typing import List
from abc import ABC, abstractmethod

from injector import inject

from .dto import CreateOrderRequest, UpdateOrderRequest, Order


class IOrderUsecase(ABC):
    @abstractmethod
    def find(self, order_id: str) -> Order:
        raise NotImplementedError()

    @abstractmethod
    def save(self, body: CreateOrderRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, order_id: str, body: UpdateOrderRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, order_id: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[Order]:
        raise NotImplementedError()


class OrderHandler:
    @inject
    def __init__(self, usecase: IOrderUsecase) -> None:
        self.usecase = usecase

    def get_orders_order_id(self, order_id: str) -> Order:
        return self.usecase.find(order_id)

    def post_orders(self, body: CreateOrderRequest) -> None:
        return self.usecase.save(body)

    def put_orders_order_id(self, order_id: str, body: CreateOrderRequest) -> None:
        return self.usecase.update(order_id, body)

    def delete_orders_order_id(self, order_id: str) -> None:
        return self.usecase.delete(order_id)

    def get_orders(self) -> List[Order]:
        return self.usecase.list()
