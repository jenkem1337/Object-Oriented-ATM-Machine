from view.abstract.IViewComponent import IViewComponent


class SucsessfullMoneyTransferViewComponent(IViewComponent):
    def __init__(self, transactionMessage) -> None:
        self.__transactionMessage = transactionMessage
    
    def printView(self) -> None:
        print(
            """
               ******************************************
               | Son Yapılan Para Transfer İşlemin Özeti |
               ******************************************
               {}
            """.format(self.__transactionMessage)
            
        )