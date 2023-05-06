from models.factory.BankAccountFactory import BankAccountFactory
from models.factory.CardFactory import CardFactory
from models.factory.CustomerFactory import CustomerFactory
from models.factory.TransactionFactory import TransactionFactory
from presenter.DepositPresenter import DepositPresenter
from repository.BankAccountRepositoryImpl import BankAccountRepositoryImpl
from repository.CustomerRepositoryImpl import CustomerRepositoryImpl
from repository.mapper.BankAccountDomainModelMapper import BankAccountDomainModelMapper
from service.BankAccountServiceImpl import BankAccountServiceImpl
from service.CustomerServiceImpl import CustomerServiceImpl
from view.Deposit.DepositView import DepositView
from view.abstract.IViewFactory import IViewFactory


class DepositViewFactory(IViewFactory[DepositView]):
    def create(self) -> DepositView:
        customerService = CustomerServiceImpl(CustomerRepositoryImpl(CustomerFactory()))
        bankAccountRepo = BankAccountRepositoryImpl(BankAccountFactory(), CardFactory(), TransactionFactory(), BankAccountDomainModelMapper())
        bankService = BankAccountServiceImpl(bankAccountRepo, customerService)
        depositPresenter = DepositPresenter(bankService)
        return DepositView(depositPresenter)