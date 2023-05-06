from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from view.abstract.IViewComponent import IViewComponent


class ATMLogoutViewComponent(IViewComponent):
    def __init__(self, customerName) -> None:
        self._customerName = customerName

    def printView(self) -> None:
        print("""

                                **************
                                |Çıkış Ekranı|
                                **************
                Sayın {} ATM'mize Daha Sonra Yine Görüşme Üzere
                               Lütfen Kartınız Alınız
        """.format(self._customerName)
        )
        input()