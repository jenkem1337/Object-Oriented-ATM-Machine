from data_transfer_objects.AbstractResponseViewModel import AbstractResponseViewModel


class LoginResponse(AbstractResponseViewModel):
    def __init__(self, bankAccountUuid=None, fullname=None, accountNumber=None, iban=None, customerUuid=None,  balance=None ) -> None:
        super().__init__("sucsess", self)
        self.bankAccountUuid = bankAccountUuid
        self.iban = iban
        self.accountNumber = accountNumber
        self.customerUuid = customerUuid
        self.balance = balance
        self.fullname = fullname
