from view.Login.LoginView import LoginView
from view.abstract.IViewFactory import IViewFactory
from models.factory.BankAccountFactory import BankAccountFactory
from models.factory.CardFactory import CardFactory
from models.factory.TransactionFactory import TransactionFactory
from presenter.LoginPresenter import LoginPresenter
from repository.BankAccountRepositoryImpl import BankAccountRepositoryImpl
from repository.mapper.BankAccountDomainModelMapper import BankAccountDomainModelMapper
from service.BankAccountServiceImpl import BankAccountServiceImpl
from service.CustomerServiceImpl import CustomerServiceImpl
from repository.CustomerRepositoryImpl import CustomerRepositoryImpl
from models.factory.CustomerFactory import CustomerFactory
from view.Login.LoginView import LoginView



class LoginViewFactory(IViewFactory[LoginView]):
    def create(self) -> LoginView:
        customerService = CustomerServiceImpl(CustomerRepositoryImpl(CustomerFactory()))
        bankAccountRepo = BankAccountRepositoryImpl(BankAccountFactory(), CardFactory(), TransactionFactory(), BankAccountDomainModelMapper())
        bankService = BankAccountServiceImpl(bankAccountRepo, customerService)
        loginPresenter = LoginPresenter(bankService)

        return LoginView(loginPresenter)

    