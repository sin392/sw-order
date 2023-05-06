from ...domain.repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, db):
        self.db = db

    def list(self):
        pass

    def save(self, user):
        pass
