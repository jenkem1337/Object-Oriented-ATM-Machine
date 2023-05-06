from view.abstract.IViewComponent import IViewComponent


class SucsessfullWithdrawViewComponent(IViewComponent):
    def __init__(self, transactionMessage) -> None:
        super().__init__()
        self._transactionMessage = transactionMessage
    
    def printView(self) -> None:
        print(
            """
               ***************************************
               | Son Yapılan Para Çekme İşlemin Özeti|
               ***************************************
               {}
            """.format(self._transactionMessage)

        )