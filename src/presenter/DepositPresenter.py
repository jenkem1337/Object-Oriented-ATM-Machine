from data_transfer_objects.Response.BankAccountResponse import BankAccountResponse
from data_transfer_objects.Response.ErrorResponse import ErrorResponse
from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from presenter.AbstractPresenter import AbstractPresenter
from service.abstract.IBankAccountService import IBankAccountService
from view.Deposit.state.SucsessfullDepositState import SucsessfullDepositState
from view.Deposit.state.UnsucsessfulDepositState import UnsucsessfulDepositState


class DepositPresenter(AbstractPresenter):
    __bankAccountService: IBankAccountService

    def __init__(self, bankAccountService:IBankAccountService) -> None:
        self.__bankAccountService = bankAccountService

    def depositMoney(self, uuid:str, amount:int):
        def sucsessResponse(res: BankAccountResponse):
            SessionManager().setKeyValuePair("balance", res.balance)
            self.bind(
                SucsessfullDepositState(transactionMessage = res.lastTransactionMessage)
            )
        
        def errorResponse(err: ErrorResponse):
            self.bind(
                UnsucsessfulDepositState(errorMsg = err.errorMessage)
            )
        
        response = self.__bankAccountService.depositMoney(uuid, amount)
        response.onSucsess(sucsessResponse)\
                .onError(errorResponse)