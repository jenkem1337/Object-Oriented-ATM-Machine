import datetime
from uuid import uuid4
from models.exceptions.CardPinNotEqualWithRequestException import CardPinNotEqualWithRequestException
from models.exceptions.CardHolderNameAndCustomerFullNameNotEqualException import CardHolderNameAndCustomerFullNameNotEqualException
from models.exceptions.CardIsNoneException import CardIsNoneException
from models.Transaction import Transaction
from models.TransactionEventType import TransactionEventType

from models.abstract.ICard import ICard
from models.abstract.ITransaction import ITransaction
from models.Validator import Validator
from models.Entity import Entity
from models.abstract.IBankAccount import IBankAccount
from models.exceptions.AccountNumberNotSameWithEachOtherException import AccountNumberNotSameWithEachOtherException
from models.exceptions.AccountNumberLengthException import AccountNumberLengthException
from models.exceptions.IbanNoControllCharacterException import IbanNoControllCharacterException
from models.exceptions.IbanNoNoneException import IbanNoNoneException
from models.exceptions.CustomerUUIDNoneException import CustomerUUIDNoneExcepetion
from models.exceptions.AccountNumberNoneException import AccountNumberNoneException
from models.exceptions.AccountBalanceNoneException import AccountBalanceNoneException
from models.exceptions.IbanNoLengthException import IbanNoLengthException
from models.exceptions.IbanNoMustBeAlphaNumericException import IbanNoMustBeAlphaNumericException
from models.exceptions.IbanNoCountryCodeException import IbanNoCountryCodeException
from models.exceptions.AccountBalanceEmptyOrNegativeCanNotTransferMoneyException import AccountBalanceEmptyOrNegativeCanNotTransferMoneyException
from models.exceptions.AccountBalanceEmptyOrNegativeException import AccountBalanceEmptyOrNegativeCanNotWithdrawException
from models.exceptions.CardNumberNoneException import CardNumberNoneException
from models.exceptions.CardPinLengthMustBeFourException import CardPinLengthMustBeFourException
from models.exceptions.CardPinNoneException import CardPinNoneException


class BankAccount(Entity, IBankAccount):

    def __init__(self, uuid:str, accountNumber:str, iban:str, customerUuid:str, password:str, balance:int) -> None:
        super().__init__(uuid)
        
        Validator.isUUIDValid(customerUuid.strip())

        Validator.isNone(iban.strip(), lambda: IbanNoNoneException())
        Validator.isNone(customerUuid.strip(), lambda: CustomerUUIDNoneExcepetion())
        Validator.isNone(accountNumber.strip(), lambda: AccountNumberNoneException())
        Validator.isNone(password.strip())
        Validator.isNone(balance, lambda: AccountBalanceNoneException())

        Validator.isStringLengthLongerThan(6, password.strip())
        Validator.isStringLengthEqualTo(16, accountNumber.strip(), lambda: AccountNumberLengthException())
        
        self.isIbanNoValid(iban.strip(), accountNumber.strip())
        
        self.__iban = iban.strip()
        self.__accountNumber = accountNumber.strip()
        self.__customerUuid = customerUuid.strip()
        self.__password = password.strip()
        self.__balance = balance
        self.__cards = dict[str, ICard]()
        self.__transactions = list()
    
    def isIbanNoValid(self, ibanNo:str, accountNumber:str = None) -> bool:
        _ibanNo = ibanNo.strip()
        countryCode = _ibanNo[0:2]
        controlChracters = _ibanNo[2:4]
        accountNumberFromIbanNo = _ibanNo[10:]
        
        Validator.isStringLengthEqualTo(26, _ibanNo, lambda: IbanNoLengthException())
        Validator.isAlpaNumeric(_ibanNo, lambda: IbanNoMustBeAlphaNumericException())
        Validator.isUpperCase(countryCode, lambda: IbanNoCountryCodeException())
        Validator.isStringValueEqualToIntegerValue(controlChracters, lambda: IbanNoControllCharacterException())
        Validator.isStringLengthEqualTo(16, accountNumberFromIbanNo, lambda: AccountNumberLengthException())
        
        if accountNumber is None:
            Validator.areStringValuesSameWithEachOther(accountNumberFromIbanNo, self.__accountNumber, lambda: AccountNumberNotSameWithEachOtherException(accountNumberFromIbanNo, self.__accountNumber))
        else:
            Validator.areStringValuesSameWithEachOther(accountNumberFromIbanNo, accountNumber, lambda: AccountNumberNotSameWithEachOtherException(accountNumberFromIbanNo, accountNumber))
        return True

    def withdraw(self, amount: int) -> None:
        Validator.isIntegerValueZeroOrNegative(amount, lambda: AccountBalanceEmptyOrNegativeCanNotWithdrawException())
        self.__balance -= abs(amount)
        withdrawDescription = "Hesabınızdan {} TL çektiniz.".format("{:,.2f}".format(amount))
        self.addTransaction(
            Transaction(
                uuid        = str(uuid4()), 
                ownerUuid   = self.__customerUuid, 
                eventType   = TransactionEventType.WITHDRAW, 
                description = withdrawDescription,
                timeStampt  = datetime.datetime.now()
            )
        )

    
    def deposit(self, amount: int) -> None:
        self.__balance += abs(amount)
        depositDescription = "Hesabınıza {} TL para yatırdınız".format("{:,.2f}".format(amount))
        self.addTransaction(
            Transaction(
                uuid        = str(uuid4()), 
                ownerUuid   = self.__customerUuid, 
                eventType   = TransactionEventType.DEPOSIT, 
                description = depositDescription,
                timeStampt  = datetime.datetime.now()
            )
        )
        
    def depositFromTransfer(self, amount:int, sender: IBankAccount):
        self.__balance += abs(amount)
        transferDescription = "Hesabınıza {} numaralı banka hesabından {} TL para transfer edilmiştir.".format(sender.getAccountNumber(), "{:,.2f}".format(amount))
        self.addTransaction(
            Transaction(
                uuid        = str(uuid4()), 
                ownerUuid   = self.__customerUuid, 
                eventType   = TransactionEventType.TRANSFER, 
                description = transferDescription,
                timeStampt  = datetime.datetime.now()
            )
        )


    def moneyTransferToAnotherAccount(self, anotherAccount: IBankAccount, amount: int) -> None:
        Validator.isIntegerValueZeroOrNegative(amount, lambda: AccountBalanceEmptyOrNegativeCanNotTransferMoneyException())
        
        
        anotherAccount.depositFromTransfer(amount, self)
        
        self.__balance -= abs(amount)


        transferDescription = "Hesabınızdan {} numaralı banka hesabına {} TL para transfer edilmiştir.".format(anotherAccount.getAccountNumber(), "{:,.2f}".format(amount))
        self.addTransaction(
            Transaction(
                uuid        = str(uuid4()), 
                ownerUuid   = self.__customerUuid, 
                eventType   = TransactionEventType.TRANSFER, 
                description = transferDescription,
                timeStampt  = datetime.datetime.now()
            )
        )
    
    def isCardValid(self, customerFullName: str, cardNumber: str, cardPin: str) -> bool:
        Validator.isNone(cardNumber.strip(), lambda: CardNumberNoneException())
        Validator.isNone(cardPin.strip(), lambda: CardPinNoneException())
        Validator.isStringLengthEqualTo(4, cardPin.strip(), lambda: CardPinLengthMustBeFourException())

        card = self.getCards().get(cardNumber)
        
        Validator.isNone(card, lambda: CardIsNoneException())
        Validator.areStringValuesSameWithEachOther(card.getHolderName(), customerFullName, lambda: CardHolderNameAndCustomerFullNameNotEqualException())
        Validator.areStringValuesSameWithEachOther(card.getPin(), cardPin, lambda: CardPinNotEqualWithRequestException())
        return True
    
    def addTransaction(self, transaction: ITransaction) -> None:
        self.__transactions.append(transaction)
    
    def addCard(self, card: ICard) -> None:
        self.__cards[card.getNumber()] = card
    
    def getLastFiveTransactionHistory(self) -> list:
        return self.__transactions[-5:]
    
    def getAccountNumber(self) -> str:
        return self.__accountNumber
    
    def getIban(self) -> str:
        return self.__iban
    
    def getCustomerUuid(self) -> str:
        return self.__customerUuid
    
    def getPassword(self) -> str:
        return self.__password
    
    def getBalance(self) -> int:
        return self.__balance
    
    def getBalanceAsString(self) -> str:
        return "{:,.2f} TL".format(self.__balance)


    def getCards(self) -> dict[str, ICard]:
        return self.__cards
    
    def getTransactions(self) -> dict[str, ITransaction]:
        return self.__transactions