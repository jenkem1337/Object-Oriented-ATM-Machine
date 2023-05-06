from abc import ABC, abstractmethod

class IEntity(ABC):
    
    @abstractmethod
    def getUuid(self) -> str:
        pass
    
    @abstractmethod
    def isNone(self) -> bool:
        pass
