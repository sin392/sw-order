from typing import List
from abc import ABC, abstractmethod

from injector import inject

from .dto import CreateItemRequest, UpdateItemRequest, Item


class IItemUsecase(ABC):
    @abstractmethod
    def find(self, item_id: str) -> Item:
        raise NotImplementedError()

    @abstractmethod
    def save(self, body: CreateItemRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, item_id: str, body: UpdateItemRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, item_id: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[Item]:
        raise NotImplementedError()


class ItemHandler:
    @inject
    def __init__(self, usecase: IItemUsecase) -> None:
        self.usecase = usecase

    def get_items_item_id(self, item_id: str) -> Item:
        return self.usecase.find(item_id)

    def post_items(self, body: CreateItemRequest) -> None:
        return self.usecase.save(body)

    def put_items_item_id(self, item_id: str, body: CreateItemRequest) -> None:
        return self.usecase.update(item_id, body)

    def delete_items_item_id(self, item_id: str) -> None:
        return self.usecase.delete(item_id)

    def get_items(self) -> List[Item]:
        return self.usecase.list()
