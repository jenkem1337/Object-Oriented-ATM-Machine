from abc import ABC, abstractmethod
from models.abstract.ITransaction import ITransaction
from models.abstract.IBankAccount import IBankAccount
class IBankAccountRepository(ABC):
    @abstractmethod
    def findOneByUuid(self, uuid:str) -> IBankAccount: pass
    
    @abstractmethod
    def findOneByAccountNumber(self, accountNumber:str) -> IBankAccount: pass

    @abstractmethod
    def findOneByIBAN(self, iban:str) -> IBankAccount: pass

    @abstractmethod
    def findOneByCustomerUuid(self, uuid:str) -> IBankAccount: pass

    @abstractmethod
    def updateBalance(self, bankAcc:IBankAccount) -> None: pass

    @abstractmethod
    def persistTransaction(self, bankAccountDomainModel: IBankAccount) -> None: pass