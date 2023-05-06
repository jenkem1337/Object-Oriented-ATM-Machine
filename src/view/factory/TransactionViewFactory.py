from presenter.TransactionPresenter import TransactionPresenter
from view.Transaction.TransactionView import TransactionView
from view.abstract.IViewFactory import IViewFactory
from models.factory.BankAccountFactory import BankAccountFactory
from models.factory.CardFactory import CardFactory
from models.factory.TransactionFactory import TransactionFactory
from repository.BankAccountRepositoryImpl import BankAccountRepositoryImpl
from repository.mapper.BankAccountDomainModelMapper import BankAccountDomainModelMapper
from service.BankAccountServiceImpl import BankAccountServiceImpl
from service.CustomerServiceImpl import CustomerServiceImpl
from repository.CustomerRepositoryImpl import CustomerRepositoryImpl
from models.factory.CustomerFactory import CustomerFactory


class TransactionViewFactory(IViewFactory[TransactionView]):

    def create(self) -> TransactionView:
        customerService = CustomerServiceImpl(CustomerRepositoryImpl(CustomerFactory()))
        bankAccountRepo = BankAccountRepositoryImpl(BankAccountFactory(), CardFactory(), TransactionFactory(), BankAccountDomainModelMapper())
        bankService = BankAccountServiceImpl(bankAccountRepo, customerService)
        transactionPresenter = TransactionPresenter(bankService)
        return TransactionView(transactionPresenter)
