from typing import List
from abc import ABC, abstractmethod

from injector import inject

from .dto import CreateItemRequest, UpdateItemRequest, Item


class IItemUsecase(ABC):
    @abstractmethod
    def find(self, item_id: str) -> Item:
        raise NotImplementedError()

    @abstractmethod
    def save(self, body: CreateItemRequest) -> str:
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

    def read_item(self, item_id: str) -> Item:
        return self.usecase.find(item_id)

    def create_item(self, body: CreateItemRequest) -> str:
        return self.usecase.save(body)

    def update_item(self, item_id: str, body: CreateItemRequest) -> None:
        return self.usecase.update(item_id, body)

    def delete_item(self, item_id: str) -> None:
        return self.usecase.delete(item_id)

    def read_items(self) -> List[Item]:
        return self.usecase.list()
