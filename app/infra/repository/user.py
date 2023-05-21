from typing import List, Optional

from sqlalchemy.orm import Session
from injector import inject

from domain.repository import IUserRepository
from domain.model import UserDOM
from infra.schema import User
from .util import orm_to_dom, orm_list_to_dom_list


class UserRepository(IUserRepository):
    @inject
    def __init__(self, db: Session) -> None:
        self.db = db

    def find(self, user_id: str) -> Optional[UserDOM]:
        orm_user = self.db.query(User).get(user_id)
        return orm_to_dom(UserDOM, orm_user) if orm_user else None

    def save(self, user: UserDOM) -> str:
        orm_user = User(**user.to_rdb_dict())
        try:
            self.db.add(orm_user)
            self.db.flush()
        except Exception as e:
            self.db.rollback()
            raise e

        self.db.commit()
        return orm_user.id

    def update(self, user: UserDOM) -> None:
        try:
            orm_user = self.db.query(User).get(user.id)
            for k, v in user.dict().items():
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
