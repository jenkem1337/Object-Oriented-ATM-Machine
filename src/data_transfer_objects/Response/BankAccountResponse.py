from data_transfer_objects.AbstractResponseViewModel import AbstractResponseViewModel


class BankAccountResponse(AbstractResponseViewModel):
    def __init__(self, uuid=None, accountNumber=None, iban=None, customerUuid=None, password=None, balance=None, cards=None, transactions=None, lastTransactionMessage=None ) -> None:
        super().__init__("sucsess", self)
        self.uuid = uuid
        self.iban = iban
        self.accountNumber = accountNumber
        self.customerUuid = customerUuid
        self.password = password
        self.balance = balance
        self.cards = cards
        self.transactions = transactions
        self.lastTransactionMessage = lastTransactionMessage

    