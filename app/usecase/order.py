from typing import List
from uuid import uuid4

from injector import inject

from domain.model import OrderDOM
from domain.repository import IOrderRepository, IOrderItemRepository, IAffiliateRepository, IUserRepository
from interface.handler.order import IOrderUsecase
from interface.handler.dto import CreateOrderRequest, UpdateOrderRequest, Order
from .util import dom_to_dto, dom_list_to_dto_list


class OrderUsecase(IOrderUsecase):
    @inject
    def __init__(self, orderRepo: IOrderRepository,
                 orderItemRepo: IOrderItemRepository,
                 userRepo: IUserRepository,
                 affiliateRepo: IAffiliateRepository) -> None:
        self.orderRepo = orderRepo
        self.orderItemRepo = orderItemRepo
        self.userRepo = userRepo
        self.affiliateRepo = affiliateRepo

    def find(self, order_id: str) -> Order:
        dom_order = self.orderRepo.find(order_id)
        return dom_to_dto(Order, dom_order)

    def save(self, body: CreateOrderRequest) -> None:
        params = {**body.dict(), "id": uuid4()}
        affiliate_id = params["affiliate_id"]
        user_id = params["user_id"]
        if affiliate_id is not None:
            affiliate = self.affiliateRepo.find(affiliate_id)
            if affiliate is None:
                raise Exception(f'Affiliateが存在しません: {affiliate_id}')
        if user_id is not None:
            user = self.userRepo.find(user_id)
            if user is None:
                raise Exception(f'Userが存在しません: {user_id}')
        # TODO: orderItemの追加処理, saveでid返すようにしないと?
        # order_items = []
        # for order_item_id in body.order_ids:
        #     order_item_id = self.OrderItemRepo.save(orderItem)
        #     order_items.append({"id": order_item_id})
        order = OrderDOM(**params)
        # order.items = order_items
        return self.orderRepo.save(order)

    def update(self, order_id: str, body: UpdateOrderRequest) -> None:
        order = self.orderRepo.find(order_id)
        if order is None:
            raise Exception(f'Orderが存在しません: {order_id}')
        order.update(body.dict())
        return self.orderRepo.update(order)

    def delete(self, order_id: str) -> None:
        order = self.orderRepo.find(order_id)
        if order is None:
            raise Exception(f'Orderが存在しません: {order_id}')
        self.orderRepo.delete(order)

    def list(self) -> List[Order]:
        dom_orders = self.orderRepo.list()
        return dom_list_to_dto_list(Order, dom_orders)
