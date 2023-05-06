from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from view.abstract.IViewComponent import IViewComponent


class DepositViewComponent(IViewComponent):
    def __init__(self, balance) -> None:
        self._balance = balance

    def printView(self) -> None:
        print(
            """
                        *********************            
                        |Para Yatırma Ekranı|
                        *********************
                Ana Ekrana Dönmek İçin 'G' Harfine Basınız
                Hesaptaki Bakiyeniz -> {}
            """.format(self._balance)
        )