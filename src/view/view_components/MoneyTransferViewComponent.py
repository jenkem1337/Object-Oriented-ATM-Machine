from view.abstract.IViewComponent import IViewComponent


class MoneyTransferViewComponent(IViewComponent):
    def printView(self) -> None:
        print(
            """
                            *******************************
                            |Hesaplar Arası Para Transferi|
                            *******************************
                Para Göndereceğiniz Hesabın Hesap Numarasını Ve Miktarı Giriniz 
            """
        )