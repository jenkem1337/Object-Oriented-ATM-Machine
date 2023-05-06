from view.abstract.AbstractView import AbstractView


class LoginView(AbstractView):

    def __init__(self, loginPresenter) -> None:
        super().__init__()
        self.__loginPresenter = loginPresenter
        self.__loginPresenter.setView(self)
    
    def login(self, accountNumber:str, cardNumber:str, cardPin:str):
        self.__loginPresenter.login(accountNumber, cardNumber, cardPin)
        self._state.login(self)