from models.exceptions.NullObjcetException import NullObjectException
from models.abstract.ICard import ICard


class NullCard(ICard):
    def getOwnerUuid(self) -> str:
        raise NullObjectException()
    def getNumber(self) -> str:
        raise NullObjectException()
    def getPin(self) -> str:
        raise NullObjectException()
    def getExpireMonth(self) -> str:
        raise NullObjectException()
    def getExpireYear(self) -> str:
        raise NullObjectException()
    def getCVV(self) -> str:
        raise NullObjectException()
    def getBrand(self) -> str:
        raise NullObjectException()
    def getHolderName(self) -> str:
        raise NullObjectException()
    def getUuid(self) -> str:
        raise NullObjectException()
    
    def isNone(self) -> bool:
        return True

