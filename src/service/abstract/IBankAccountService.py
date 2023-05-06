from abc import ABC, abstractmethod
from data_transfer_objects.AbstractResponseViewModel import AbstractResponseViewModel

class IBankAccountService(ABC):

    @abstractmethod
    def login(self, accountNumber:str, cardNumber:str, cardPin:str) -> AbstractResponseViewModel: pass
    
    @abstractmethod
    def depositMoney(self, uuid:str, amount:int) -> AbstractResponseViewModel: pass
    
    @abstractmethod
    def withdrawMoney(self, uuid:str, amount) -> AbstractResponseViewModel: pass

    @abstractmethod
    def transferMoneyToAnotherAccount(self, uuid:str, anotherAccountNumber:str, amount:int) -> AbstractResponseViewModel: pass

    @abstractmethod
    def getAccountBalance(self, uuid:str) -> AbstractResponseViewModel: pass

    @abstractmethod
    def getLastFiveTransactionHistory(self, uuid:str) -> AbstractResponseViewModel: pass