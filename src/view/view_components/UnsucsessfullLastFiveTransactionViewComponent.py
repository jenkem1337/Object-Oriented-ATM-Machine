

from view.abstract.IViewComponent import IViewComponent


class UnsucsessfullLastFiveTransactionViewComponent(IViewComponent):
    def __init__(self, err) -> None:
        self._err = err
    def printView(self) -> None:
        print(
            """     
                    *****************************************************
                    |İşlem Geçmişini Getirirken Bir Hata İle Kaşılaşıldı|      
                    *****************************************************
                    Hata Mesajı -> {}
            """.format(self._err)
        )
