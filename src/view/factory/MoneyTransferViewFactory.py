from presenter.TransferPresenter import TransferPresenter
from view.MoneyTransfer.MoneyTransferView import MoneyTransferView
from view.abstract.IViewFactory import IViewFactory

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

class MoneyTransferViewFactory(IViewFactory[MoneyTransferView]):

    def create(self) -> MoneyTransferView:

        customerService = CustomerServiceImpl(CustomerRepositoryImpl(CustomerFactory()))
        bankAccountRepo = BankAccountRepositoryImpl(BankAccountFactory(), CardFactory(), TransactionFactory(), BankAccountDomainModelMapper())
        bankService = BankAccountServiceImpl(bankAccountRepo, customerService)
        transferPresenter = TransferPresenter(bankService)
        return MoneyTransferView(transferPresenter)