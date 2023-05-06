from abc import ABC
from typing import Any

class AbstractPresenter(ABC):
    
    
    def setView(self, view: Any) -> None:
        self.__view = view 

    def bind(self, viewState) -> None:
        self.__view.setState(viewState)