from models.Validator import Validator
from models.Entity import Entity
from models.abstract.ICustomer import ICustomer
from models.exceptions.CustomerNameNoneException import CustomerNameNoneException
from models.exceptions.CustomerSurnameNoneException import CustomerSurnameNoneException
class Customer(Entity, ICustomer):
    
    def __init__(self, uuid: str, name:str, surname:str) -> None:
        super().__init__(uuid)
        Validator.isNone(name.strip(), lambda: CustomerNameNoneException())
        Validator.isNone(surname.strip(), lambda: CustomerSurnameNoneException())
        self.__name = name.strip()
        self.__surname = surname.strip()
        self.__fullname = "{} {}".format(self.__name, self.__surname)

    def getName(self) -> str:
        return self.__name
    def getSurname(self) -> str:
        return self.__surname
    def getFullname(self) -> str:
        return self.__fullname
