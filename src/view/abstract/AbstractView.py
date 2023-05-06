from abc import ABC
from typing import Any
from view.abstract.IMainViewReceiver import IMainViewReceiver
from view.abstract.IViewComponent import IViewComponent

from view.abstract.IViewNotifier import IViewNotifyier


class AbstractView(IViewNotifyier, ABC):
    __mainView: IMainViewReceiver
    
    def notifyMainView(self, obj: IViewComponent) -> None:
        self.__mainView.update(obj)
    
    def setMainView(self, mainView: IMainViewReceiver) -> None:
        self.__mainView = mainView
    
    def setState(self, state):
        self._state = state

