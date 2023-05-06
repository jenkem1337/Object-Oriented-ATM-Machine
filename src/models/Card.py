from models.exceptions.CardPinLengthMustBeFourException import CardPinLengthMustBeFourException
from models.exceptions.CardPinNoneException import CardPinNoneException
from models.Validator import Validator
from models.Entity import Entity
from models.abstract.ICard import ICard
from models.exceptions.CustomerUUIDNoneException import CustomerUUIDNoneExcepetion
from models.exceptions.CardNumberNoneException import CardNumberNoneException
from models.exceptions.CardCVVNoneException import CardCVVNoneException
from models.exceptions.CardExpireMonthNoneException import CardExpireMonthNoneException
from models.exceptions.CardExpireYearNoneException import CardExpireYearNoneException
from models.exceptions.CardBrandNoneException import CardBrandNoneException
from models.exceptions.CardHolderNameNoneException import CardHolderNameNoneException

class Card(Entity, ICard):
    
    def __init__(self, uuid:str, ownerUuid:str, number:str, pin:str, expireMonth:str, expireYear:str, cvv:str, brand:str, holderName:str) -> None:
        super().__init__(uuid)
        
        Validator.isNone(ownerUuid.strip(), lambda: CustomerUUIDNoneExcepetion())
        Validator.isNone(number.strip(), lambda: CardNumberNoneException())
        Validator.isNone(pin.strip(), lambda: CardPinNoneException())
        Validator.isNone(expireMonth.strip(), lambda: CardExpireMonthNoneException())
        Validator.isNone(expireYear.strip(), lambda: CardExpireYearNoneException())
        Validator.isNone(cvv.strip(), lambda: CardCVVNoneException())
        Validator.isNone(brand.strip(), lambda: CardBrandNoneException())
        Validator.isNone(holderName.strip(), lambda: CardHolderNameNoneException())

        Validator.isUUIDValid(ownerUuid.strip())

        Validator.isStringLengthEqualTo(3, cvv.strip())
        Validator.isStringLengthEqualTo(4, pin.strip(), lambda: CardPinLengthMustBeFourException())

        self.__ownerUuid = ownerUuid.strip()
        self.__number = number.strip()
        self.__pin = pin.strip()
        self.__expireMonth = expireMonth.strip()
        self.__expireYear = expireYear.strip()
        self.__cvv = cvv.strip()
        self.__brand = brand.strip()
        self.__holderName = holderName.strip()
    
    def getOwnerUuid(self) -> str:
        return self.__ownerUuid
    def getNumber(self) -> str:
        return self.__number
    def getPin(self) -> str:
        return self.__pin
    def getExpireMonth(self) -> str:
        return self.__expireMonth
    def getExpireYear(self) -> str:
        return self.__expireYear
    def getCVV(self) -> str:
        return self.__cvv
    def getBrand(self) -> str:
        return self.__brand
    def getHolderName(self) -> str:
        return self.__holderName