from view.Transaction.TransactionView import TransactionView
from view.abstract.ICommand import ICommand


class LastFiveTransactionCommand(ICommand):
    __transactionView: TransactionView
    def __init__(self,transactionView:TransactionView) -> None:
        self.__transactionView = transactionView
    def execute(self, data: dict) -> None:
        self.__transactionView.getLastFiveTransaction(data.get("BANK_ACCOUNT_UUID"))