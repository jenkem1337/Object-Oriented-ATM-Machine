from view.abstract.AbstractView import AbstractView


class WithdrawView(AbstractView):
    def __init__(self, presenter) -> None:
        self.__presenter = presenter
        self.__presenter.setView(self)

    def withdrawMoney(self, uuid:str, amount:int):
        self.__presenter.withdrawMoney(uuid, amount)
        self._state.withdrawMoney(self)