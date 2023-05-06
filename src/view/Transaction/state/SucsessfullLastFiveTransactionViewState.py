from view.Transaction.state.BaseTransactionState import BaseTransactionViewState
from view.abstract.AbstractView import AbstractView
from view.view_components.LastFiveTransactionViewComponent import LastFiveTransactionViewComponent


class SucsessfullLastFiveTransactionViewState(BaseTransactionViewState):
    def __init__(self, transactions) -> None:
        super().__init__(transactions, None)

    def getLastFiveTransaction(self, view: AbstractView):
        view.notifyMainView(
            LastFiveTransactionViewComponent(self._transactions)
        )