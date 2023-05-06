from uuid import uuid4
from typing import List

from sqlalchemy.orm import Session

from domain.repository import IUserRepository
from domain.model import UserDOM
from infra.schema import User
from .util import orm_list_to_dom_list


class UserRepository(IUserRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self) -> List[UserDOM]:
        orm_users = self.db.query(User).all()
        return orm_list_to_dom_list(orm_users)

    def save(self, user: UserDOM) -> None:
        params = {**user.dict(), "id": uuid4()}
        orm_user = User(**params)
        try:
            self.db.add(orm_user)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()
