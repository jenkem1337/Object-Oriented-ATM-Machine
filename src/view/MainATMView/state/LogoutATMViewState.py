from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from view.MainATMView.state.BaseATMViewState import BaseAtmViewState
import view.MainATMView.state.CardNotInsertedState  as state
from view.abstract.IMainView import IMainView
from view.view_components.ATMLogoutViewComponent import ATMLogoutViewComponent


class ATMLogoutViewState(BaseAtmViewState):
    def run(self, atmView:IMainView):
        atmView.printViewComponent(ATMLogoutViewComponent(SessionManager().getValue("customer_fullname")))
        SessionManager().clear()
        #when i use from view.MainATMView.state.CardNotInsertedState import CardNotInsertedState
        #it couse ciruculer dependency error
        atmView.setState(state.CardNotInsertedState())