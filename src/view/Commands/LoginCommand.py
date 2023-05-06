from view.Login.LoginView import LoginView
from view.abstract.ICommand import ICommand


class LoginCommand(ICommand):
    __loginView: LoginView
    def __init__(self, loginView) -> None:
        self.__loginView = loginView
    def execute(self, data: dict) -> None:
        self.__loginView.login(data.get("ACCOUNT_NUMBER"), data.get("CARD_NUMBER"), data.get("CARD_PIN")) 