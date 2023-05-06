from models.abstract.ICard import ICard
from models.abstract.ITransaction import ITransaction
from models.abstract.IBankAccount import IBankAccount
from models.exceptions.NullObjcetException import NullObjectException
class NullBankAccount(IBankAccount):
    
    def deposit(self, amount: int) -> None:
        raise NullObjectException()
    
    def withdraw(self, amount: int) -> None:
        raise NullObjectException()

    def moneyTransferToAnotherAccount(self, anotherAccount: IBankAccount, amount: int) -> None:
        raise NullObjectException()
    
    def isIbanNoValid(self, ibanNo:str, accountNumber:str = None) -> bool:
        raise NullObjectException()
    def addTransaction(self, transaction: ITransaction) -> None:
        pass
    def addCard(self, card: ICard) -> None:
        pass
    def getAccountNumber(self) -> str:
        raise NullObjectException()
    
    def getIban(self) -> str:
        raise NullObjectException()
    
    def getCustomerUuid(self) -> str:
        raise NullObjectException()
    
    def getPassword(self) -> str:
        raise NullObjectException()
    
    def getBalance(self) -> int:
        raise NullObjectException()
    
    def getBalanceAsString(self) -> str:
        raise NullObjectException()
    
    def getCards(self) -> dict[str, ICard]:
        raise NullObjectException()
    
    def getTransactions(self) -> list:
        raise NullObjectException()

    def getUuid(self) -> str:
        raise NullObjectException()
    
    def isNone(self) -> bool:
        return True

    def depositFromTransfer(self, amount: int, sender):
        raise NullObjectException()
    
    def getLastFiveTransactionHistory(self) -> list:
        raise NullObjectException()

    def isCardValid(self, customerFullName:str, cardNumber:str, cardPin:str) -> bool:
        raise NullObjectException()
