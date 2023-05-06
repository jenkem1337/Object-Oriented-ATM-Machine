from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from view.abstract.IViewComponent import IViewComponent


class ATMHomeViewComponent(IViewComponent):
    def __init__(self, customerName) -> None:
        self._customerName = customerName
    def printView(self) -> None:
        res = """
            Sayın {} aşağıdan istediğiniz işlemleri yapabilirsiniz

            1 - Para Çek
            2 - Para Yatır
            3 - Para Transfer Et
            4 - Bakiye Sorgula
            5 - Yapılan son 5 işlem
            6 - Çıkış yap
        """.format(self._customerName)
        print(res)