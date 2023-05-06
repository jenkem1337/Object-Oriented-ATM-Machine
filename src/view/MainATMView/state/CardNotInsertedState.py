from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from view.MainATMView.ATMView import ATMView
from view.MainATMView.state.BaseATMViewState import BaseAtmViewState
from view.MainATMView.state.CardInsertedState import CardInsertedState
from view.view_components.LoginViewComponent import LoginViewComponent


class CardNotInsertedState(BaseAtmViewState):

    def run(self, atmView: ATMView):
        atmView.printViewComponent(LoginViewComponent())
        accountNumber = str(input("Hesap Numarası: "))
        cardNumber    = str(input("Kart Numarası: "))
        cardPin       = str(input("Kart Şifresi: "))

        commandData = {
            "ACCOUNT_NUMBER": accountNumber,
            "CARD_NUMBER":cardNumber,
            "CARD_PIN": cardPin
        }
        atmView.executeCommand("LOGIN_COMMAND", commandData)
        
        if SessionManager().getValue("is_logged_in"):
            atmView.setState(CardInsertedState())
        return
