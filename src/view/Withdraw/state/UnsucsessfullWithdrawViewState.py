from view.Withdraw.WithdrawView import WithdrawView
from view.Withdraw.state.BaseWithdrawViewState import BaseWithdrawViewState
from view.view_components.UnsucsessfullWithdrawViewComponent import UnsucsessfullWithdrawViewComponent


class UnsucsessfullWithdrawViewState(BaseWithdrawViewState):
    def __init__(self, transactionMessage=None, errorMsg=None) -> None:
        super().__init__(transactionMessage, errorMsg)
        
    def withdrawMoney(self, view:WithdrawView):
        view.notifyMainView(
            UnsucsessfullWithdrawViewComponent(self._errorMessage)
        )