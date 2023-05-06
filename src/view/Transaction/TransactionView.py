from view.abstract.AbstractView import AbstractView


class TransactionView(AbstractView):

    def __init__(self, presenter) -> None:
        self.__presenter = presenter
        self.__presenter.setView(self)
    
    def getLastFiveTransaction(self, uuid:str):
        self.__presenter.getLastFiveTransaction(uuid)
        self._state.getLastFiveTransaction(self)