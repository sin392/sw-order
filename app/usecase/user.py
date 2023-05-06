from typing import List

from domain.model import UserDOM
from domain.repository import IUserRepository, IAffiliateRepository
from interface.handler.user import IUserUsecase
from interface.handler.dto import CreateUserRequest, UpdateUserRequest, User
from .util import dom_to_dto, dom_list_to_dto_list


class UserUsecase(IUserUsecase):
    def __init__(self, userRepository: IUserRepository, affiliateRepository: IAffiliateRepository) -> None:
        self.userRepository = userRepository
        self.affiliateRepository = affiliateRepository

    def find(self, user_id: str) -> User:
        dom_user = self.userRepository.find(user_id)
        return dom_to_dto(User, dom_user)

    def save(self, body: CreateUserRequest) -> None:
        user = UserDOM.parse_obj(body)
        affiliate_id = body.affiliate_id
        if affiliate_id is not None:
            affiliate = self.affiliateRepository.find(affiliate_id)
            if affiliate is None:
                raise Exception(f'Affiliateが存在しません: {affiliate_id}')
            user.affiliate = affiliate
        return self.userRepository.save(user)

    def update(self, user_id: str, body: UpdateUserRequest) -> None:
        user = self.userRepository.find(user_id)
        if user is None:
            raise Exception(f'Userが存在しません: {user_id}')
        user.update(body.dict())
        return self.userRepository.update(user)

    def delete(self, user_id: str) -> None:
        user = self.userRepository.find(user_id)
        if user is None:
            raise Exception(f'Userが存在しません: {user_id}')
        self.userRepository.delete(user)

    def list(self) -> List[User]:
        dom_users = self.userRepository.list()
        return dom_list_to_dto_list(User, dom_users)
