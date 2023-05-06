from typing import List
from abc import ABC, abstractmethod

from domain.model.item import ItemDOM


class IItemRepository(ABC):
    @abstractmethod
    def find(self, user_id: str) -> ItemDOM:
        raise NotImplementedError()

    @abstractmethod
    def save(self, item) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, item) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, item) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[ItemDOM]:
        raise NotImplementedError()
