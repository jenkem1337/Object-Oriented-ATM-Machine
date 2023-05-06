from data_transfer_objects.AbstractResponseViewModel import AbstractResponseViewModel
from data_transfer_objects.Response.CustomerResponse import CustomerResponse
from data_transfer_objects.Response.ErrorResponse import ErrorResponse
from models.exceptions.CustomerNotFoundException import CustomerNotFoundException
from repository.abstract.ICustomerRepository import ICustomerRepository
from service.abstract.ICustomerService import ICustomerService


class CustomerServiceImpl(ICustomerService):
    __customerRepository: ICustomerRepository
    def __init__(self, customerRepository: ICustomerRepository) -> None:
        self.__customerRepository = customerRepository
    
    def findOneByUuid(self, uuid:str) -> AbstractResponseViewModel:
        try:
            customer = self.__customerRepository.findOneByUuid(uuid)
            
            if customer.isNone() is True:
                raise CustomerNotFoundException()
            
            return CustomerResponse(customer.getUuid(), customer.getFullname())
        except Exception as err:
            return ErrorResponse(err.args[0])