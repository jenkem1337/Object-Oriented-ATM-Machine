from data_transfer_objects.Response.BankAccountResponse import BankAccountResponse
from data_transfer_objects.Response.ErrorResponse import ErrorResponse
from data_transfer_objects.Response.LoginResponse import LoginResponse
from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from presenter.AbstractPresenter import AbstractPresenter
from service.abstract.IBankAccountService import IBankAccountService
from view.Login.state.SucsessfullLoginState import SucsessfullLoginState
from view.Login.state.UnsucsessfullLoginState import UnsucsessfullLoginState
from view.Transaction.state.SucsessfullLastFiveTransactionViewState import SucsessfullLastFiveTransactionViewState
from view.view_components.UnsucsessfullLastFiveTransactionViewComponent import UnsucsessfullLastFiveTransactionViewComponent


class TransactionPresenter(AbstractPresenter):
    __bankAccountService: IBankAccountService

    def __init__(self, bankAccountService:IBankAccountService) -> None:
        self.__bankAccountService = bankAccountService
    
    def getLastFiveTransaction(self, uuid):
        def sucsessResponse(res: BankAccountResponse):

            self.bind(
                SucsessfullLastFiveTransactionViewState(
                    transactions=res.transactions
                )
            )
        
        def errorResponse(err: ErrorResponse):
            self.bind(
                UnsucsessfullLastFiveTransactionViewComponent(err.errorMessage)
            )
        response = self.__bankAccountService.getLastFiveTransactionHistory(uuid)
        
        response.onSucsess(sucsessResponse)\
                .onError(errorResponse)
        