from abc import ABC, abstractmethod

from ...usecase.dto import AffiliatesPostRequest
from fastapi.responses import Response


class IAffiliateUsecase(ABC):
    @abstractmethod
    def list(self):
        NotImplementedError()

    @abstractmethod
    def save(self, body: AffiliatesPostRequest):
        NotImplementedError()


class AffiliateHandler:
    def __init__(self, usecase: IAffiliateUsecase) -> None:
        self.usecase = usecase

    def get_affiliates(self):
        res = self.usecase.list()
        return Response()

    def post_affiliates(self, body: AffiliatesPostRequest):
        res = self.usecase.save(body)
        return Response()
