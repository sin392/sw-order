from abc import ABC, abstractmethod


class IAffiliateRepository(ABC):
    @abstractmethod
    def list(self):
        raise NotImplementedError()

    @abstractmethod
    def save(self, affiliate):
        raise NotImplementedError()
