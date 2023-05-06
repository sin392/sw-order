from ..domain.model import UserDOM
from ..domain.repository import IUserRepository
from ..interface.handler.user import IUserUsecase
from .dto import UsersPostRequest


class UserUsecase(IUserUsecase):
    def __init__(self, repo: IUserRepository) -> None:
        self.repo = repo

    def list(self):
        return self.repo.list()

    def save(self, body: UsersPostRequest):
        user = UserDOM.parse_obj(body)
        return self.repo.save(user)
