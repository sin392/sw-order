from typing import List
from abc import ABC, abstractmethod

from .dto import CreateUserRequest, UpdateUserRequest, User


class IUserUsecase(ABC):
    @abstractmethod
    def find(self, user_id: str) -> User:
        raise NotImplementedError()

    @abstractmethod
    def save(self, body: CreateUserRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, user_id: str, body: UpdateUserRequest) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, user) -> None:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> List[User]:
        raise NotImplementedError()


class UserHandler:
    def __init__(self, usecase: IUserUsecase) -> None:
        self.usecase = usecase

    def get_users_user_id(self, user_id: str) -> User:
        return self.usecase.find(user_id)

    def post_users(self, body: CreateUserRequest) -> None:
        return self.usecase.save(body)

    def put_users_user_id(self, user_id: str, body: CreateUserRequest) -> None:
        return self.usecase.update(user_id, body)

    def delete_users_user_id(self, user_id: str) -> None:
        return self.usecase.delete(user_id)

    def get_users(self) -> List[User]:
        return self.usecase.list()
