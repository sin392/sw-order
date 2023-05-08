from typing import List
from uuid import uuid4

from injector import inject

from domain.model import OrderItemDOM
from domain.repository import IOrderRepository, IOrderItemRepository, IItemRepository
from interface.handler.order_item import IOrderItemUsecase
from interface.handler.dto import CreateOrderItemRequest, UpdateOrderItemRequest, OrderItem
from .util import dom_to_dto, dom_list_to_dto_list


class OrderItemUsecase(IOrderItemUsecase):
    @inject
    def __init__(self, orderItemRepo: IOrderItemRepository,
                 orderRepo: IOrderRepository,
                 itemRepo: IItemRepository) -> None:
        self.orderItemRepo = orderItemRepo
        self.orderRepo = orderRepo
        self.itemRepo = itemRepo

    def find(self, order_item_id: str) -> OrderItem:
        dom_order = self.orderItemRepo.find(order_item_id)
        return dom_to_dto(OrderItem, dom_order)

    def save(self, body: CreateOrderItemRequest) -> None:
        params = {**body.dict(), "id": uuid4()}
        order_id = params["order_id"]
        item_id = params["item_id"]
        if order_id is not None:
            order = self.orderRepo.find(order_id)
            if order is None:
                raise Exception(f'Orderが存在しません: {order_id}')
        if item_id is not None:
            item = self.itemRepo.find(item_id)
            if item is None:
                raise Exception(f'Itemが存在しません: {item_id}')
        orderItem = OrderItemDOM(**params)
        return self.orderItemRepo.save(orderItem)

    def update(self, order_item_id: str, body: UpdateOrderItemRequest) -> None:
        orderItem = self.orderItemRepo.find(order_item_id)
        if orderItem is None:
            raise Exception(f'OrderItemが存在しません: {order_item_id}')
        orderItem.update(body.dict())
        return self.orderItemRepo.update(orderItem)

    def delete(self, order_item_id: str) -> None:
        orderItem = self.orderItemRepo.find(order_item_id)
        if orderItem is None:
            raise Exception(f'OrderItemが存在しません: {order_item_id}')
        self.orderItemRepo.delete(orderItem)

    def list(self) -> List[OrderItem]:
        dom_order_items = self.orderRepo.list()
        return dom_list_to_dto_list(OrderItem, dom_order_items)
