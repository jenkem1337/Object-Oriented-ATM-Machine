from view.Deposit.DepositView import DepositView
from view.abstract.ICommand import ICommand


class DepositCommand(ICommand):
    __depositView: DepositView
    def __init__(self, depositView: DepositView) -> None:
        super().__init__()
        self.__depositView = depositView
    def execute(self, data: dict) -> None:
        self.__depositView.depositMoney(data.get("BANK_ACCOUNT_UUID"), data.get("AMOUNT"))