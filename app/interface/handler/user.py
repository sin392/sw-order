from abc import ABC, abstractmethod

from ...usecase.dto import UsersPostRequest
from fastapi.responses import Response


class IUserUsecase(ABC):
    @abstractmethod
    def list(self):
        NotImplementedError()

    @abstractmethod
    def save(self, body: UsersPostRequest):
        NotImplementedError()


class UserHandler:
    def __init__(self, usecase: IUserUsecase) -> None:
        self.usecase = usecase

    def get_users(self):
        res = self.usecase.list()
        return Response()

    def post_users(self, body: UsersPostRequest):
        res = self.usecase.save(body)
        return Response()
