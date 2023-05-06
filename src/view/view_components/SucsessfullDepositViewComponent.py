from view.abstract.IViewComponent import IViewComponent


class SucsessfullDepositViewComponent(IViewComponent):
    def __init__(self, transactionMessage) -> None:
        super().__init__()
        self.__transactionMessage = transactionMessage
    
    def printView(self) -> None:
        print(
            """
               ******************************************
               | Son Yapılan Para Yatırma İşlemin Özeti |
               ******************************************
               {}
            """.format(self.__transactionMessage)
            
        )