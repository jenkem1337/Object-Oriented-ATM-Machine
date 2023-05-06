from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")
class IViewFactory(Generic[T], ABC):
    
    @abstractmethod
    def create(self) -> T:pass