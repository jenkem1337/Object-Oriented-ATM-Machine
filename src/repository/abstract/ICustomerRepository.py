from abc import ABC, abstractmethod

from models.abstract.ICustomer import ICustomer

class ICustomerRepository(ABC):
    @abstractmethod
    def findOneByUuid(self, uuid:str) -> ICustomer: pass