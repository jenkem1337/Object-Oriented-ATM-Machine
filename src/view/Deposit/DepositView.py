from view.abstract.AbstractView import AbstractView


class DepositView(AbstractView):
    def __init__(self, presenter) -> None:
        self.__presenter = presenter
        self.__presenter.setView(self)

    def depositMoney(self, uuid:str, amount:int):
        self.__presenter.depositMoney(uuid, amount)
        self._state.depositMoney(self)