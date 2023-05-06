from abc import ABC, abstractmethod


class IViewComponent(ABC):
    @abstractmethod
    def printView(self) -> None: pass