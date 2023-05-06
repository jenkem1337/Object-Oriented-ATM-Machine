from view.MoneyTransfer.MoneyTransferView import MoneyTransferView
from view.MoneyTransfer.state.BaseTransferViewState import BaseTransferViewState
from view.view_components.UnsucsessfullMoneyTransferViewComponent import UnsucsessfullMoneyTransferViewComponent


class UnucsessfullMoneyTransferViewState(BaseTransferViewState):
    def __init__(self, errMsg) -> None:
        super().__init__(None, errMsg)
    def transferMoney(self, view:MoneyTransferView):
        view.notifyMainView(
            UnsucsessfullMoneyTransferViewComponent(self._errorMessage)
        )