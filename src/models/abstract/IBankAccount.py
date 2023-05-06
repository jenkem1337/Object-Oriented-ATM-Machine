from abc import ABC, abstractmethod
from models.abstract.ICard import ICard
from models.abstract.ITransaction import ITransaction
from models.abstract.IEntity import IEntity

class IBankAccount(IEntity, ABC):
    
    @abstractmethod
    def isCardValid(self, customerFullName:str, cardNumber:str, cardPin:str) -> bool:pass

    @abstractmethod
    def deposit(self, amount:int) -> None: pass
    
    @abstractmethod
    def withdraw(self, amount:int) -> None: pass
    
    @abstractmethod
    def moneyTransferToAnotherAccount(self, anotherAccount, amount:int) -> None: pass
    
    @abstractmethod
    def isIbanNoValid(self, ibanNo:str, accountNumber:str = None) -> bool: pass
    
    @abstractmethod
    def addTransaction(self, transaction: ITransaction) -> None: pass
    
    @abstractmethod
    def addCard(self, card: ICard) -> None: pass

    @abstractmethod
    def depositFromTransfer(self, amount:int, sender):pass

    @abstractmethod
    def getLastFiveTransactionHistory(self) -> list: pass
    
    @abstractmethod
    def getAccountNumber(self) -> str: pass
    
    @abstractmethod
    def getIban(self) -> str: pass
    
    @abstractmethod
    def getCustomerUuid(self) -> str: pass
    
    @abstractmethod
    def getPassword(self) -> str: pass
    
    @abstractmethod
    def getBalanceAsString(self) -> str: pass

    @abstractmethod
    def getBalance(self) -> str: pass
    
    @abstractmethod
    def getCards(self) -> dict[str, ICard]: pass
    
    @abstractmethod
    def getTransactions(self) -> list[ITransaction]: pass