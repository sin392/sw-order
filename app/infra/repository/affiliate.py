from domain.repository import IAffiliateRepository


class AffiliateRepository(IAffiliateRepository):
    def __init__(self, db):
        self.db = db

    def list(self):
        pass

    def save(self, affiliate):
        pass
