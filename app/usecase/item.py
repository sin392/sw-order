from typing import List
from uuid import uuid4

from injector import inject

from domain.model import ItemDOM
from domain.repository import IItemRepository
from interface.handler.item import IItemUsecase
from interface.handler.dto import CreateItemRequest, UpdateItemRequest, Item
from .util import dom_to_dto, dom_list_to_dto_list


class ItemUsecase(IItemUsecase):
    @inject
    def __init__(self, repo: IItemRepository) -> None:
        self.repo = repo

    def find(self, item_id: str) -> Item:
        dom_item = self.repo.find(item_id)
        return dom_to_dto(Item, dom_item)

    def save(self, body: CreateItemRequest) -> None:
        params = {**body.dict(), "id": uuid4()}
        item = ItemDOM(**params)
        return self.repo.save(item)

    def update(self, item_id: str, body: UpdateItemRequest) -> None:
        item = self.repo.find(item_id)
        if item is None:
            raise Exception(f'Itemが存在しません: {item_id}')
        item.update(body.dict())
        return self.repo.update(item)

    def delete(self, item_id: str) -> None:
        item = self.repo.find(item_id)
        if item is None:
            raise Exception(f'Itemが存在しません: {item_id}')
        self.repo.delete(item)

    def list(self) -> List[Item]:
        dom_items = self.repo.list()
        return dom_list_to_dto_list(Item, dom_items)
