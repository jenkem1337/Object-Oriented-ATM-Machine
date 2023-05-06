from abc import ABC, abstractmethod

from view.Login.LoginView import LoginView


class LoginViewBaseState(ABC):

    def __init__(self, bankAccountUuid=None, fullname=None, accountNumber=None, iban=None, customerUuid=None,  balance=None, errorMessage=None) -> None:
        self._bankAccountUuid = bankAccountUuid
        self._iban = iban
        self._accountNumber = accountNumber
        self._customerUuid = customerUuid
        self._balance = balance
        self._fullname = fullname
        self._errorMessage = errorMessage

    @abstractmethod
    def login(self, viewInstance:LoginView):pass
