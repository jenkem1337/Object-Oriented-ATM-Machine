from view.abstract.IViewComponent import IViewComponent


class MoneyWasTakenViewComponent(IViewComponent):
    def printView(self) -> None:
        print("""
                          ******************
                          |Kartınızı Alınız|
                          ******************
            Paranızı Alabilmeniz İçin Kartınızı Makineden Çıkarın
        """)
        input()