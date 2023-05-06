from abc import ABC, abstractmethod


class IUserRepository(ABC):
    @abstractmethod
    def list(self):
        raise NotImplementedError()

    @abstractmethod
    def save(self, user):
        raise NotImplementedError()
