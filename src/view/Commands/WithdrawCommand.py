from view.Withdraw.WithdrawView import WithdrawView
from view.abstract.ICommand import ICommand


class WithdrawCommand(ICommand):
    __withdrawView: WithdrawView
    def __init__(self, withdrawView: WithdrawView) -> None:
        super().__init__()
        self.__withdrawView = withdrawView
    def execute(self, data: dict) -> None:
        self.__withdrawView.withdrawMoney(data.get("BANK_ACCOUNT_UUID"), data.get("AMOUNT"))