from presenter.WithdrawPresenter import WithdrawPresenter
from view.Withdraw.WithdrawView import WithdrawView
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

class WithdrawViewFactory(IViewFactory[WithdrawView]):

    def create(self) -> WithdrawView:
        customerService = CustomerServiceImpl(CustomerRepositoryImpl(CustomerFactory()))
        bankAccountRepo = BankAccountRepositoryImpl(BankAccountFactory(), CardFactory(), TransactionFactory(), BankAccountDomainModelMapper())
        bankService = BankAccountServiceImpl(bankAccountRepo, customerService)
        withdrawPresenter = WithdrawPresenter(bankService)
        return WithdrawView(withdrawPresenter)