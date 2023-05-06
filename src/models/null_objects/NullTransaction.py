from datetime import datetime
from models.abstract.ITransaction import ITransaction
from models.exceptions.NullObjcetException import NullObjectException

class NullTransaction(ITransaction):
    def getOwnerUuid(self) -> str: raise NullObjectException()

    def getEventType(self) -> str: raise NullObjectException()

    def getDescription(self) -> str:raise NullObjectException()

    def getTimeStampt(self) -> str: raise NullObjectException()

    def getUuid(self) -> str: raise NullObjectException()

    def isNone(self) -> bool: 
        return True
