from data_transfer_objects.Response.BankAccountResponse import BankAccountResponse
from data_transfer_objects.Response.ErrorResponse import ErrorResponse
from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from presenter.AbstractPresenter import AbstractPresenter
from service.abstract.IBankAccountService import IBankAccountService
from view.MoneyTransfer.state.SucsessfullMoneyTransferViewState import SucsessfullMoneyTransferViewState
from view.MoneyTransfer.state.UnsucsessfullMoneyTransferViewState import UnucsessfullMoneyTransferViewState
from view.view_components.UnsucsessfullMoneyTransferViewComponent import UnsucsessfullMoneyTransferViewComponent

class TransferPresenter(AbstractPresenter):
    __bankAccountService: IBankAccountService

    def __init__(self, bankAccountService:IBankAccountService) -> None:
        self.__bankAccountService = bankAccountService

    def transferMoney(self, uuid:str, anotherAccountNumber:str, amount:int):
        def sucsessResponse(res: BankAccountResponse):
            SessionManager().setKeyValuePair("balance", res.balance)
            self.bind(
                SucsessfullMoneyTransferViewState(lastTransactionMessage = res.lastTransactionMessage)
            )
        
        def errorResponse(err: ErrorResponse):
            self.bind(
                UnucsessfullMoneyTransferViewState(errMsg=err.errorMessage)
            )
        
        response = self.__bankAccountService.transferMoneyToAnotherAccount(uuid, anotherAccountNumber, amount)
        response.onSucsess(sucsessResponse)\
                .onError(errorResponse)
    