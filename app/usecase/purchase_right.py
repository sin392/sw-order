from typing import List
from uuid import uuid4

from injector import inject

from domain.model import PurchaseRightDOM
from domain.repository import IPurchaseRightRepository, IAffiliateRepository, IItemRepository
from interface.handler.purchase_right import IPurchaseRightUsecase
from interface.handler.dto import CreatePurchaseRightRequest, UpdatePurchaseRightRequest, PurchaseRight
from .util import dom_to_dto, dom_list_to_dto_list


class PurchaseRightUsecase(IPurchaseRightUsecase):
    @inject
    def __init__(self, purchaseRightRepo: IPurchaseRightRepository,
                 affiliateRepo: IAffiliateRepository,
                 itemRepo: IItemRepository) -> None:
        self.purchaseRightRepo = purchaseRightRepo
        self.affiliateRepo = affiliateRepo
        self.itemRepo = itemRepo

    def find(self, order_id: str) -> PurchaseRight:
        dom_order = self.purchaseRightRepo.find(order_id)
        return dom_to_dto(PurchaseRight, dom_order)

    def save(self, body: CreatePurchaseRightRequest) -> None:
        params = {**body.dict(), "id": uuid4()}
        affiliate_id = params["affiliate_id"]
        item_id = params["item_id"]
        if affiliate_id is not None:
            affiliate = self.affiliateRepo.find(affiliate_id)
            if affiliate is None:
                raise Exception(f'Affiliateが存在しません: {affiliate_id}')
        if item_id is not None:
            item = self.itemRepo.find(item_id)
            if item is None:
                raise Exception(f'Itemが存在しません: {item_id}')
        purchase_right = PurchaseRightDOM(**params)
        return self.purchaseRightRepo.save(purchase_right)

    def update(self, purchase_right_id: str, body: UpdatePurchaseRightRequest) -> None:
        purchase_right = self.purchaseRightRepo.find(purchase_right_id)
        if purchase_right is None:
            raise Exception(f'PurchaseRightが存在しません: {purchase_right_id}')
        purchase_right.update(body.dict())
        return self.purchaseRightRepo.update(purchase_right)

    def delete(self, purchase_right_id: str) -> None:
        purchase_right = self.purchaseRightRepo.find(purchase_right_id)
        if purchase_right is None:
            raise Exception(f'PurchaseRightが存在しません: {purchase_right_id}')
        self.purchaseRightRepo.delete(purchase_right)

    def list(self) -> List[PurchaseRight]:
        dom_purchase_rights = self.purchaseRightRepo.list()
        return dom_list_to_dto_list(PurchaseRight, dom_purchase_rights)
