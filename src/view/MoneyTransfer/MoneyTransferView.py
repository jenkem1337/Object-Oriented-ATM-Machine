from view.abstract.AbstractView import AbstractView


class MoneyTransferView(AbstractView):

    def __init__(self, presenter) -> None:
        self.__presenter = presenter
        self.__presenter.setView(self)

    def transferMoneyToAnotherAccount(self, uuid:str, anotherAccountNumber:str, amount:int):
        self.__presenter.transferMoney(uuid, anotherAccountNumber, amount)
        self._state.transferMoney(self)