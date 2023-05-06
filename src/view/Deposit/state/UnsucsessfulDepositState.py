from view.Deposit.DepositView import DepositView
from view.Deposit.state.BaseDepositViewState import BaseDepositViewState
from view.view_components.UnsucsessfullDepositView import UnsucsessfullDepositViewComponent


class UnsucsessfulDepositState(BaseDepositViewState):
    def __init__(self, transactionMessage=None, errorMsg=None) -> None:
        super().__init__(transactionMessage, errorMsg)
    
    def depositMoney(self, depositView: DepositView):
        depositView.notifyMainView(
            UnsucsessfullDepositViewComponent(self.errorMessage)
        )