from view.MoneyTransfer.MoneyTransferView import MoneyTransferView
from view.MoneyTransfer.state.BaseTransferViewState import BaseTransferViewState
from view.view_components.SucsessfullMoneyTransferViewComponent import SucsessfullMoneyTransferViewComponent


class SucsessfullMoneyTransferViewState(BaseTransferViewState):
    def __init__(self, lastTransactionMessage) -> None:
        super().__init__(lastTransactionMessage, None)
    def transferMoney(self, view:MoneyTransferView):
        view.notifyMainView(
            SucsessfullMoneyTransferViewComponent(self._lastTransactionMessage)
        )