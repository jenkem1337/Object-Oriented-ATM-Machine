from abc import ABC, abstractmethod

from view.Withdraw.WithdrawView import WithdrawView


class BaseWithdrawViewState(ABC):
    def __init__(self, transactionMessage=None, errorMsg=None) -> None:
        self._transactionMessage = transactionMessage
        self._errorMessage = errorMsg
    
    @abstractmethod
    def withdrawMoney(self, view:WithdrawView):pass