from abc import ABC, abstractmethod

from data_transfer_objects.AbstractResponseViewModel import AbstractResponseViewModel


class ICustomerService(ABC):
    @abstractmethod
    def findOneByUuid(self, uuid) -> AbstractResponseViewModel: pass