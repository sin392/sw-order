from domain.model import AffiliateDOM
from domain.repository import IAffiliateRepository
from interface.handler.affiliate import IAffiliateUsecase
from interface.handler.dto import AffiliatesPostRequest


class AffiliateUsecase(IAffiliateUsecase):
    def __init__(self, repo: IAffiliateRepository) -> None:
        self.repo = repo

    def list(self):
        return self.repo.list()

    def save(self, body: AffiliatesPostRequest):
        affiliate = AffiliateDOM.parse_obj(body)
        return self.repo.save(affiliate)
