from abc import ABC
from models.abstract.IEntity import IEntity
from models.Validator import Validator
class Entity(IEntity, ABC):
    def __init__(self, uuid: str) -> None:
        Validator.isNone(uuid.strip())
        Validator.isUUIDValid(uuid.strip())
        self.__uuid = uuid
    
    def getUuid(self) -> str:
        return self.__uuid
    
    def isNone(self) -> bool:
        return False