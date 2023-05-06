from abc import ABC, abstractmethod

from view.Deposit.DepositView import DepositView


class BaseDepositViewState(ABC):
    def __init__(self, transactionMessage=None, errorMsg=None) -> None:
        self.transactionMessage = transactionMessage
        self.errorMessage = errorMsg
    
    @abstractmethod
    def depositMoney(self, depositView:DepositView):pass