from typing import List

from domain.model import UserDOM
from domain.repository import IUserRepository
from interface.handler.user import IUserUsecase
from interface.handler.dto import CreateUserRequest, UpdateUserRequest, User
from .util import dom_to_dto, dom_list_to_dto_list


class UserUsecase(IUserUsecase):
    def __init__(self, repo: IUserRepository) -> None:
        self.repo = repo

    def find(self, user_id: str) -> User:
        dom_user = self.repo.find(user_id)
        return dom_to_dto(User, dom_user)

    def save(self, body: CreateUserRequest) -> None:
        user = UserDOM.parse_obj(body)
        return self.repo.save(user)

    def update(self, user_id: str, body: UpdateUserRequest) -> None:
        user = self.repo.find(user_id)
        if user is None:
            raise Exception(f'Userが存在しません: {user_id}')
        updated_user = user.update(body)
        return self.repo.update(updated_user)

    def delete(self, user_id: str) -> None:
        user = self.repo.find(user_id)
        if user is None:
            raise Exception(f'Userが存在しません: {user_id}')
        self.repo.delete(user)

    def list(self) -> List[User]:
        dom_users = self.repo.list()
        return dom_list_to_dto_list(User, dom_users)
