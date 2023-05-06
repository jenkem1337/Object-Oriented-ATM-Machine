from view.abstract.IViewComponent import IViewComponent


class UnsucsessLoginViewComponent(IViewComponent):

    def __init__(self, errorMessage) -> None:
        self.__errorMessage = errorMessage

    def printView(self) -> None:
        res = """
                    -----------------------
                    |     Hatalı giriş    |
                    -----------------------
            Hata mesajı -> {}
            Lütfen tekrardan giriş yapmayı deneyim
        """.format(self.__errorMessage)
        print(res)
        