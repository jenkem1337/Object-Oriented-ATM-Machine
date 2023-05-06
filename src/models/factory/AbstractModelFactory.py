from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")

class AbstractModelFactory(Generic[T], ABC):
    _isMustBeConcreate:bool
    @abstractmethod
    def createInstance(self, **args) -> T:
        pass

    def mustBeConcreate(self):
        self._isMustBeConcreate = True
        return self
    def itCanBeNullable(self):
        self._isMustBeConcreate = False
        return self

