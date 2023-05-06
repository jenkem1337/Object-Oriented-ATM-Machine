from view.abstract.IViewComponent import IViewComponent


class SucsessLoginViewComponent(IViewComponent):

    def __init__(self, fullname) -> None:
        self.__fullname = fullname
    def printView(self) -> None:
        res = """
        --------------------------------------------------
            Sayın {} banka ATM'sine hoşgeldiniz.
        --------------------------------------------------
        """.format(self.__fullname)
        print(res)