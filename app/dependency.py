from typing import TypeVar, Type

from sqlalchemy.orm import Session
from injector import Injector, Binder

from domain.repository import *
from infra.repository import *
from interface.handler import *
from usecase import *

T = TypeVar("T")

repository_pairs = [
    (IUserRepository, UserRepository),
    (IAffiliateRepository, AffiliateRepository),
    (IItemRepository, ItemRepository),
    (IOrderRepository, OrderRepository),
    (IOrderItemRepository, OrderItemRepository),
    (IPurchaseRightRepository, PurchaseRightRepository),
]
service_pairs = []
usecase_pairs = [
    (IUserUsecase, UserUsecase),
    (IAffiliateUsecase, AffiliateUsecase),
    (IItemUsecase, ItemUsecase),
    (IOrderUsecase, OrderUsecase),
    (IOrderItemUsecase, OrderItemUsecase),
    (IPurchaseRightUsecase, PurchaseRightUsecase),
]


class Dependency():
    def __init__(self, db: Session) -> None:
        self.db = db
        self.injector = Injector(self.config)

    def config(self, binder: Binder) -> None:
        for interface, implement in repository_pairs:
            binder.bind(interface, implement(db=self.db))
        for pairs in (service_pairs, usecase_pairs):
            for interface, implement in pairs:
                binder.bind(interface, implement)

    def resolve(self, cls: Type[T]) -> T:
        return self.injector.get(cls)
