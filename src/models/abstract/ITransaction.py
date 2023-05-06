from abc import ABC, abstractmethod
from datetime import datetime
from models.abstract.IEntity import IEntity

class ITransaction(IEntity, ABC):
    @abstractmethod
    def getOwnerUuid(self) -> str: pass
    @abstractmethod
    def getEventType(self) -> str: pass
    @abstractmethod
    def getDescription(self) -> str:pass
    @abstractmethod
    def getTimeStampt(self) -> str: pass
