from abc import ABC, abstractmethod
from view.abstract.IMainViewReceiver import IMainViewReceiver
from view.abstract.IViewComponent import IViewComponent


class IViewNotifyier(ABC):
    
    @abstractmethod
    def setMainView(self, mainView: IMainViewReceiver) -> None:pass
    
    @abstractmethod
    def notifyMainView(self, obj: IViewComponent) -> None:pass
