from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from view.abstract.IViewComponent import IViewComponent


class AccountBalanceViewComponent(IViewComponent):
    def __init__(self, balance) -> None:
        self._balance = balance
    def printView(self) -> None:
        print(
                """
                    ****************
                    |Hesap Bakiyesi|
                    ****************
                    Hesap Bakiyeniz -> {}
                """.format(self._balance)
        )
        input("Geri dönemk için enter tuşuna basınız")