from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")

class IDomainModelMapper(Generic[T], ABC):
    @abstractmethod
    def mapFromDictToSingleModel(self, dict: dict, **additionalParamaters) -> T: pass
    
    @abstractmethod
    def mapFromModelToDict(self, domainModel: T, **additionalParamaters) -> dict: pass