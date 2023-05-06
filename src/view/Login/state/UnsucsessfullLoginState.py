from view.Login.LoginView import LoginView
from view.view_components.UnsucsessLoginViewComponent import UnsucsessLoginViewComponent
from view.Login.state.LoginBaseState import LoginViewBaseState


class UnsucsessfullLoginState(LoginViewBaseState):
    def __init__(self, errorMessage) -> None:
        super().__init__(errorMessage=errorMessage)
    
    def login(self, viewInstance: LoginView):
        viewInstance.notifyMainView(
            UnsucsessLoginViewComponent(self._errorMessage)
        )