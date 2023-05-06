from view.abstract.IViewComponent import IViewComponent


class UnsucsessfullDepositViewComponent(IViewComponent):
    def __init__(self, err) -> None:
        self.__err = err

    def printView(self) -> None:
        print("""
                *********************************************************
                |Para Yatırma İşlemi Yapılırken Bir Hata İle Kaşılaşıldı|
                *********************************************************

                Hata Mesajı -> {}
        """.format(self.__err))