from models.abstract.ITransaction import ITransaction
from models.Validator import Validator
from datetime import datetime
from models.Entity import Entity
from models.exceptions.CustomerUUIDNoneException import CustomerUUIDNoneExcepetion
from models.exceptions.TransactionEventTypeNoneException import TransactionEventTypeNoneException
from models.exceptions.TransactionDescriptionNoneException import TransactionDescriptionNoneException
class Transaction(Entity, ITransaction):

    def __init__(self, uuid:str, ownerUuid:str, eventType:str, description:str, timeStampt: datetime) -> None:
        super().__init__(uuid)

        Validator.isNone(ownerUuid.strip(), lambda: CustomerUUIDNoneExcepetion())
        Validator.isNone(eventType.strip(), lambda: TransactionEventTypeNoneException())
        Validator.isNone(description.strip(), lambda: TransactionDescriptionNoneException)
        Validator.isNone(timeStampt)
        
        self.__ownerUuid = ownerUuid.strip()
        self.__eventType = eventType.strip()
        self.__description = description.strip()
        self.__timeStampt = timeStampt

    def getOwnerUuid(self) -> str:
        return self.__ownerUuid
    def getEventType(self) -> str:
        return self.__eventType
    def getDescription(self) -> str:
        return self.__description
    def getTimeStampt(self) -> str:
        return self.__timeStampt.strftime("%d/%m/%Y %H:%M:%S")
        
