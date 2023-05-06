from abc import ABC, abstractmethod

from view.abstract.AbstractView import AbstractView


class BaseTransactionViewState(ABC):
    def __init__(self, transactions:list= None, err:str = None) -> None:
        self._transactions = transactions
        self._errorMessage = err
    @abstractmethod
    def getLastFiveTransaction(self, view:AbstractView): pass