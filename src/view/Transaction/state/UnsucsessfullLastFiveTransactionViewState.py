from view.Transaction.state.BaseTransactionState import BaseTransactionViewState
from view.abstract.AbstractView import AbstractView
from view.view_components.UnsucsessfullLastFiveTransactionViewComponent import UnsucsessfullLastFiveTransactionViewComponent


class UnsucsessfullLastFiveTransactionViewState(BaseTransactionViewState):
    def __init__(self, err) -> None:
        super().__init__(None, err)

    def getLastFiveTransaction(self, view: AbstractView):
        view.notifyMainView(
            UnsucsessfullLastFiveTransactionViewComponent(self._errorMessage)
        )