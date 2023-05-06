from abc import ABC, abstractmethod
from models.abstract.IEntity import IEntity

class ICard(IEntity, ABC):
    @abstractmethod
    def getOwnerUuid(self) -> str:
        pass
    @abstractmethod
    def getNumber(self) -> str:
        pass
    @abstractmethod
    def getPin(self) -> str:
        pass
    @abstractmethod
    def getExpireMonth(self) -> str:
        pass
    @abstractmethod
    def getExpireYear(self) -> str:
        pass
    @abstractmethod
    def getCVV(self) -> str:
        pass
    @abstractmethod
    def getBrand(self) -> str:
        pass
    @abstractmethod
    def getHolderName(self) -> str:
        pass