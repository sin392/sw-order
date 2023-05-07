from typing import List
from abc import ABC, abstractmethod

from domain.model.user import UserDOM


class IUserRepository(ABC):
    @abstractmethod
    def find(self, user_id: str) -> UserDOM:
        raise NotImplementedError()

    @abstractmethod
    def save(self, user: UserDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, user: UserDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, user: UserDOM) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[UserDOM]:
        raise NotImplementedError()
