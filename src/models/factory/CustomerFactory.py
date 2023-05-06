from models.abstract.ICustomer import ICustomer
from models.factory.AbstractModelFactory import AbstractModelFactory
from models.Customer import Customer
from models.null_objects.NullCustomer import NullCustomer


class CustomerFactory(AbstractModelFactory[ICustomer]):
    def createInstance(self, **args) -> ICustomer:
        if self._isMustBeConcreate is True:
            return Customer(args.get("uuid"), args.get("name"), args.get("surname"))
        
        if self._isMustBeConcreate is False:
            try:
                return Customer(args.get("uuid"), args.get("name"), args.get("surname"))
            except Exception as err:
                return NullCustomer()
