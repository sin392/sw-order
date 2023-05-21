from typing import List
from abc import ABC, abstractmethod

from domain.model.item import ItemDOM


class IItemRepository(ABC):
    @abstractmethod
    def find(self, item_id: str) -> ItemDOM:
        raise NotImplementedError()

    @abstractmethod
    def save(self, item: ItemDOM) -> str:
        raise NotImplementedError()

    @abstractmethod
    def update(self, item: ItemDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, item: ItemDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[ItemDOM]:
        raise NotImplementedError()
