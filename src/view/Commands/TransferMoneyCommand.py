
from view.MoneyTransfer.MoneyTransferView import MoneyTransferView
from view.abstract.ICommand import ICommand


class TransferMoneyCommand(ICommand):
    __transferView: MoneyTransferView
    def __init__(self, transferView:MoneyTransferView) -> None:
        self.__transferView = transferView
    
    def execute(self, data: dict) -> None:
        self.__transferView.transferMoneyToAnotherAccount(data.get("BANK_ACCOUNT_UUID"), data.get("ANOTHER_ACCOUNT_UUID"), data.get("AMOUNT"))