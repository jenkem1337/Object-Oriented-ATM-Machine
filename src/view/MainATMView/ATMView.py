import time
from view.Commands.CommandContext import CommandContext
from view.MainATMView.state.BaseATMViewState import BaseAtmViewState
from view.abstract.AbstractMainView import AbstractMainView
from view.abstract.IMainView import IMainView
from view.abstract.IViewComponent import IViewComponent


class ATMView(AbstractMainView[BaseAtmViewState]):
    def __init__(self, initialState: BaseAtmViewState, commandContext:CommandContext) -> None:
        super().__init__(initialState, commandContext)
        
    def run(self) -> None:
        while True:
            self._state.run(self)
    
