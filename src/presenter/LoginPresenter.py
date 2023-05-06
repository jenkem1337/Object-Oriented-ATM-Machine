from data_transfer_objects.Response.ErrorResponse import ErrorResponse
from data_transfer_objects.Response.LoginResponse import LoginResponse
from data_transfer_objects.SessionManeger.SessionManager import SessionManager
from presenter.AbstractPresenter import AbstractPresenter
from service.abstract.IBankAccountService import IBankAccountService
from view.Login.state.SucsessfullLoginState import SucsessfullLoginState
from view.Login.state.UnsucsessfullLoginState import UnsucsessfullLoginState


class LoginPresenter(AbstractPresenter):
    __bankAccountService: IBankAccountService

    def __init__(self, bankAccountService:IBankAccountService) -> None:
        self.__bankAccountService = bankAccountService
    
    def login(self, accountNumber:str, cardNumber:str, cardPin:str):
        def sucsessResponse(loginResponse: LoginResponse):
            sessionMeneger = SessionManager()
            
            sessionMeneger.setKeyValuePair("bank_account_uuid", loginResponse.bankAccountUuid) \
                            .setKeyValuePair("customer_fullname", loginResponse.fullname) \
                            .setKeyValuePair("is_logged_in", True) \
                            .setKeyValuePair("balance", loginResponse.balance)

            self.bind(
                SucsessfullLoginState(
                    fullname=loginResponse.fullname
                )
            )
        
        def errorResponse(err: ErrorResponse):
            self.bind(
                UnsucsessfullLoginState(err.errorMessage)
            )
        response = self.__bankAccountService.login(accountNumber, cardNumber, cardPin)
        
        response.onSucsess(sucsessResponse)\
                .onError(errorResponse)
        