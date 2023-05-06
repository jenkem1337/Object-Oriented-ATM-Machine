from abc import ABC, abstractmethod

from view.MoneyTransfer.MoneyTransferView import MoneyTransferView


class BaseTransferViewState(ABC):
    def __init__(self, lastTransactionMessage=None, errMsg=None) -> None:
        self._lastTransactionMessage = lastTransactionMessage
        self._errorMessage = errMsg
    @abstractmethod
    def transferMoney(self, view:MoneyTransferView):pass
