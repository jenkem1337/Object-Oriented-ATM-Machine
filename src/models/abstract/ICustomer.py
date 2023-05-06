from abc import ABC, abstractmethod

from models.abstract.IEntity import IEntity

class ICustomer(IEntity, ABC):
    @abstractmethod
    def getName(self) -> str:pass
    
    @abstractmethod
    def getSurname(self) -> str:pass
    
    @abstractmethod
    def getFullname(self) -> str:pass
