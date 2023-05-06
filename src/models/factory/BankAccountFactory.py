from models.BankAccount import BankAccount
from models.abstract.IBankAccount import IBankAccount
from models.factory.AbstractModelFactory import AbstractModelFactory
from models.null_objects.NullBankAccount import NullBankAccount


class BankAccountFactory(AbstractModelFactory[IBankAccount]):
    def createInstance(self, **args) -> IBankAccount:
        if self._isMustBeConcreate is True:
            return BankAccount(
                args.get("uuid"),
                args.get("account_number"),
                args.get("iban"),
                args.get("customer_uuid"),
                args.get("password"),
                args.get("balance")
            )
        
        if self._isMustBeConcreate is False:
            try:
                return BankAccount(
                        args.get("uuid"),
                        args.get("account_number"),
                        args.get("iban"),
                        args.get("customer_uuid"),
                        args.get("password"),
                        args.get("balance")
                    )
            except Exception as err:
                return NullBankAccount()
