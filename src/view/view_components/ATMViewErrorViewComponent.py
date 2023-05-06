from view.abstract.IViewComponent import IViewComponent


class ATMViewErrorViewComponent(IViewComponent):
    def __init__(self, err) -> None:
        super().__init__()
        self._err = err
    def printView(self) -> None:
        print("""
                        ****************************
                        |ATM Makinesi Ön Yüz Hatası|
                        ****************************
              Galiba Sistemsel Bir Aksilik Oldu
              Hata Mesajı -> {}
        """.format(self._err))