from view.Login.LoginView import LoginView
from view.Login.state.LoginBaseState import LoginViewBaseState
from view.view_components.SucsessLoginViewComponent import SucsessLoginViewComponent


class SucsessfullLoginState(LoginViewBaseState):
    def __init__(self, bankAccountUuid=None, fullname=None, accountNumber=None, iban=None, customerUuid=None, balance=None) ->None:
        super().__init__(bankAccountUuid, fullname, accountNumber, iban, customerUuid, balance)

    def login(self, viewInstance: LoginView):
        viewInstance.notifyMainView(
            SucsessLoginViewComponent(self._fullname)
        )