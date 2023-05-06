from typing import List
from uuid import uuid4

from domain.model import UserDOM
from domain.repository import IUserRepository, IAffiliateRepository
from interface.handler.user import IUserUsecase
from interface.handler.dto import CreateUserRequest, UpdateUserRequest, User
from .util import dom_to_dto, dom_list_to_dto_list


class UserUsecase(IUserUsecase):
    def __init__(self, userRepo: IUserRepository, affiliateRepo: IAffiliateRepository) -> None:
        self.userRepo = userRepo
        self.affiliateRepo = affiliateRepo

    def find(self, user_id: str) -> User:
        dom_user = self.userRepo.find(user_id)
        return dom_to_dto(User, dom_user)

    def save(self, body: CreateUserRequest) -> None:
        params = {**body.dict(), "id": uuid4()}
        user = UserDOM(**params)
        affiliate_id = body.affiliate_id
        if affiliate_id is not None:
            affiliate = self.affiliateRepo.find(affiliate_id)
            if affiliate is None:
                raise Exception(f'Affiliateが存在しません: {affiliate_id}')
            user.affiliate = affiliate
        return self.userRepo.save(user)

    def update(self, user_id: str, body: UpdateUserRequest) -> None:
        user = self.userRepo.find(user_id)
        if user is None:
            raise Exception(f'Userが存在しません: {user_id}')
        user.update(body.dict())
        return self.userRepo.update(user)

    def delete(self, user_id: str) -> None:
        user = self.userRepo.find(user_id)
        if user is None:
            raise Exception(f'Userが存在しません: {user_id}')
        self.userRepo.delete(user)

    def list(self) -> List[User]:
        dom_users = self.userRepo.list()
        return dom_list_to_dto_list(User, dom_users)
