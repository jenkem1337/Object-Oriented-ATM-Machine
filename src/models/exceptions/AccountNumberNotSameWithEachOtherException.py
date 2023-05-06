class AccountNumberNotSameWithEachOtherException(Exception):
    def __init__(self, *args: object) -> None:
        self.__errorMessage = "{} banka hesap numarası ile {} banka hesap numaras aynı değil".format(args[0], args[1])
        super().__init__(self.__errorMessage)