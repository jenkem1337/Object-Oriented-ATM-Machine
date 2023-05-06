from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from view.MainATMView.state.BaseATMViewState import BaseAtmViewState
from view.abstract.IMainView import IMainView
from view.view_components.MoneyWasTakenViewComponent import MoneyWasTakenViewComponent
import view.MainATMView.state.CardNotInsertedState as state


class MoneyWasTakenState(BaseAtmViewState):
    def run(self, atmView: IMainView):
        atmView.printViewComponent(MoneyWasTakenViewComponent())
        SessionManager().clear()
        #when i use from view.MainATMView.state.CardNotInsertedState import CardNotInsertedState
        #it couse ciruculer dependency error
        atmView.setState(state.CardNotInsertedState())