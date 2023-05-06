from data_transfer_objects.Response.BankAccountResponse import BankAccountResponse
from data_transfer_objects.Response.ErrorResponse import ErrorResponse
from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from presenter.AbstractPresenter import AbstractPresenter
from service.abstract.IBankAccountService import IBankAccountService
from view.Withdraw.state.SucsessfullWithdrawViewState import SucsessfullWithdrawViewState
from view.Withdraw.state.UnsucsessfullWithdrawViewState import UnsucsessfullWithdrawViewState

class WithdrawPresenter(AbstractPresenter):
    __bankAccountService: IBankAccountService

    def __init__(self, bankAccountService:IBankAccountService) -> None:
        self.__bankAccountService = bankAccountService

    def withdrawMoney(self, uuid:str, amount:int):
        def sucsessResponse(res: BankAccountResponse):
            SessionManager().setKeyValuePair("balance", res.balance)
            self.bind(
                SucsessfullWithdrawViewState(transactionMessage = res.lastTransactionMessage)
            )
        
        def errorResponse(err: ErrorResponse):
            self.bind(
                UnsucsessfullWithdrawViewState(errorMsg = err.errorMessage)
            )
        
        response = self.__bankAccountService.withdrawMoney(uuid, amount)
        response.onSucsess(sucsessResponse)\
                .onError(errorResponse)