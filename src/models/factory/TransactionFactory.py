from models.abstract.ITransaction import ITransaction
from models.factory.AbstractModelFactory import AbstractModelFactory
from models.Transaction import Transaction
from models.null_objects.NullTransaction import NullTransaction

class TransactionFactory(AbstractModelFactory[ITransaction]):
    def createInstance(self, **args) -> ITransaction:
        if self._isMustBeConcreate is True:
            return Transaction(
                args.get("uuid"),
                args.get("owner_uuid"), 
                args.get("event_type"), 
                args.get("description"), 
                args.get("time_stampt")
            )
        
        if self._isMustBeConcreate is False:
            try:
                return Transaction(
                        args.get("uuid"),
                        args.get("owner_uuid"), 
                        args.get("event_type"), 
                        args.get("description"), 
                        args.get("time_stampt")
                    )

            except Exception as err:
                return NullTransaction()
