from view.abstract.IViewComponent import IViewComponent
from models.abstract.ITransaction import ITransaction

class LastFiveTransactionViewComponent(IViewComponent):

    def __init__(self, transactions:list[ITransaction]) -> None:
        self._transactions = transactions
    
    def printView(self) -> None:
        print(
            """
                **************************
                |Yaptığınız Son Beş İşlem|
                **************************
            """
        )

        for i in self._transactions:
            print(
                """
                   ************************
                   * İşlem Açıklaması -> {}
                   * İşlemin Tipi     -> {}
                   * İşlem Tarihi     -> {}
                   ************************
                """.format(i.getDescription(), i.getEventType(), i.getTimeStampt())
            )
            print("")
        
        input("Çıkmak İçin Enter Tuşuna Basınız")