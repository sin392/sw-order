from typing import List
from abc import ABC, abstractmethod

from injector import inject

from .dto import CreateUserRequest, UpdateUserRequest, User


class IUserUsecase(ABC):
    @abstractmethod
    def find(self, user_id: str) -> User:
        raise NotImplementedError()

    @abstractmethod
    def save(self, body: CreateUserRequest) -> str:
        raise NotImplementedError()

    @abstractmethod
    def update(self, user_id: str, body: UpdateUserRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, user_id: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[User]:
        raise NotImplementedError()


class UserHandler:
    @inject
    def __init__(self, usecase: IUserUsecase) -> None:
        self.usecase = usecase

    def read_user(self, user_id: str) -> User:
        return self.usecase.find(user_id)

    def create_user(self, body: CreateUserRequest) -> str:
        return self.usecase.save(body)

    def update_users(self, user_id: str, body: CreateUserRequest) -> None:
        return self.usecase.update(user_id, body)

    def delete_user(self, user_id: str) -> None:
        return self.usecase.delete(user_id)

    def read_users(self) -> List[User]:
        return self.usecase.list()
