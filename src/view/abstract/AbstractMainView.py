from abc import ABC, abstractmethod
import time
from typing import Generic, TypeVar
from view.Commands.CommandContext import CommandContext
from view.abstract.IMainView import IMainView
from view.abstract.IViewComponent import IViewComponent

T = TypeVar("T")
class AbstractMainView(Generic[T],IMainView, ABC):
    _state: T
    _commandContext: CommandContext
    
    def __init__(self, initialState: T, commandContext:CommandContext) -> None:
        
        self.setState(initialState)
        self.__commandContext = commandContext
    
    
    def update(self, viewComponent: IViewComponent) -> None:
        self.__viewComponent = viewComponent
        self.printViewComponent(self.__viewComponent)
        time.sleep(1)
        
    def setState(self, state:T) -> None:
        self._state = state
    
    def printViewComponent(self, viewComponent: IViewComponent):
        viewComponent.printView()

    def executeCommand(self, commandKey:str, data:dict):
        command = self.__commandContext.getCommand(commandKey)
        command.execute(data)