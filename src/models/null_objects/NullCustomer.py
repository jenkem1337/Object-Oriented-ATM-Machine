from models.abstract.ICustomer import ICustomer
from models.exceptions.NullObjcetException import NullObjectException


class NullCustomer(ICustomer):
    def getName(self) -> str:     raise NullObjectException()

    def getSurname(self) -> str:  raise NullObjectException()

    def getFullname(self) -> str: raise NullObjectException()

    def getUuid(self) -> str:     raise NullObjectException()
    
    def isNone(self) -> bool:
        return True


