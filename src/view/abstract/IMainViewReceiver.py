from abc import ABC, abstractmethod

from view.abstract.IViewComponent import IViewComponent


class IMainViewReceiver(ABC):
    @abstractmethod
    def update(self, obj: IViewComponent) -> None :pass