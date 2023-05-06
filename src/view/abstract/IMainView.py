from abc import ABC, abstractmethod

from view.abstract.IMainViewReceiver import IMainViewReceiver
from view.abstract.IViewComponent import IViewComponent


class IMainView(IMainViewReceiver, ABC):
    @abstractmethod
    def run(self) -> None: pass

    @abstractmethod
    def setState(self, state) -> None:pass

    @abstractmethod
    def printViewComponent(self, viewComponent:IViewComponent):pass

    @abstractmethod
    def executeCommand(self, commandKey:str, data:dict): pass
