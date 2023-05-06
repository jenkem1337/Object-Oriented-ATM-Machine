from view.abstract.IViewComponent import IViewComponent


class MoneyTransferDeniedViewComponent(IViewComponent):

    def printView(self) -> None:
        print(
            """             ********************
                            |İşlem İptal Edildi|
                            ********************
                Transfer İşlemi İsteğiniz Üzerine İptal Edildi
            """
        )