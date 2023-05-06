from uuid import uuid4
from typing import List

from sqlalchemy.orm import Session

from domain.repository import IUserRepository
from domain.model import UserDOM
from infra.schema import User
from .util import orm_to_dom, orm_list_to_dom_list


class UserRepository(IUserRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def find(self, user_id: str) -> UserDOM:
        orm_user = self.db.query(User).get(user_id)
        return orm_to_dom(UserDOM, orm_user)

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

    def update(self, user: UserDOM) -> None:
        try:
            orm_user = self.db.query(User).get(user.id)
            for k, v in user.dict():
                setattr(orm_user, k, v)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def delete(self, user: UserDOM) -> None:
        try:
            orm_user = self.db.query(User).get(user.id)
            self.db.delete(orm_user)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()

    def list(self) -> List[UserDOM]:
        orm_users = self.db.query(User).all()
        return orm_list_to_dom_list(UserDOM, orm_users)
