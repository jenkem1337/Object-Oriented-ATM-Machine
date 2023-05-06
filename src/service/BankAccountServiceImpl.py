from data_transfer_objects.AbstractResponseViewModel import AbstractResponseViewModel
from data_transfer_objects.Response.BankAccountResponse import BankAccountResponse
from data_transfer_objects.Response.CustomerResponse import CustomerResponse
from data_transfer_objects.Response.ErrorResponse import ErrorResponse
from data_transfer_objects.Response.LoginResponse import LoginResponse
from models.exceptions.CustomerNotFoundException import CustomerNotFoundException
from models.exceptions.BankAccountNotFoundException import BankAccountNotFoundException
from repository.abstract.IBankAccountRepository import IBankAccountRepository
from service.abstract.IBankAccountService import IBankAccountService
from service.abstract.ICustomerService import ICustomerService


class BankAccountServiceImpl(IBankAccountService):
    
    __bankAccountRepository: IBankAccountRepository
    __customerService      : ICustomerService
    
    def __init__(self, bankAccountRepository: IBankAccountRepository, customerService: ICustomerService) -> None:
        super().__init__()
        self.__bankAccountRepository = bankAccountRepository
        self.__customerService       = customerService

    def login(self, accountNumber:str, cardNumber:str, cardPin:str) -> AbstractResponseViewModel:
        try:
            bankAccount = self.__bankAccountRepository.findOneByAccountNumber(accountNumber)

            if bankAccount.isNone() is True:
                raise BankAccountNotFoundException()
                            
            abstractCustomerResponseModel = self.__customerService.findOneByUuid(bankAccount.getCustomerUuid())
            
            if abstractCustomerResponseModel.isEventEqualToError():
                raise CustomerNotFoundException()
            
            customerResponseModel: CustomerResponse = abstractCustomerResponseModel.justGetResponseModel()
            bankAccount.isCardValid(customerResponseModel.fullName, cardNumber, cardPin)
            return LoginResponse(
                accountNumber=bankAccount.getAccountNumber(),
                balance=bankAccount.getBalanceAsString(),
                bankAccountUuid=bankAccount.getUuid(),
                customerUuid=customerResponseModel.uuid,
                fullname=customerResponseModel.fullName,
                iban=bankAccount.getIban()
            )
        except Exception as err:
            return ErrorResponse(err)


    
    def depositMoney(self, uuid:str, amount:int) -> AbstractResponseViewModel:
        try:
            bankAccount = self.__bankAccountRepository.findOneByUuid(uuid)

            if bankAccount.isNone() is True:
                raise BankAccountNotFoundException()

            bankAccount.deposit(amount)
            
            self.__bankAccountRepository.updateBalance(bankAccount)
            self.__bankAccountRepository.persistTransaction(bankAccount)
            
            return BankAccountResponse(
                lastTransactionMessage=bankAccount.getTransactions()[-1].getDescription(),
                balance=bankAccount.getBalanceAsString()
            )
        except Exception as err:
            return ErrorResponse(err)

    def withdrawMoney(self, uuid:str, amount:int) -> AbstractResponseViewModel:
        try:
            bankAccount = self.__bankAccountRepository.findOneByUuid(uuid)

            if bankAccount.isNone() is True:
                raise BankAccountNotFoundException()

            bankAccount.withdraw(amount)
            
            self.__bankAccountRepository.updateBalance(bankAccount)
            self.__bankAccountRepository.persistTransaction(bankAccount)
            
            return BankAccountResponse(
                lastTransactionMessage=bankAccount.getTransactions()[-1].getDescription(),
                balance= bankAccount.getBalanceAsString()
            )
        except Exception as err:
            return ErrorResponse(err)


    def transferMoneyToAnotherAccount(self, uuid:str, anotherBankAccountNumber:str, amount:int) -> AbstractResponseViewModel: 
        try:    
            bankAccount = self.__bankAccountRepository.findOneByUuid(uuid)
            anotherBankAccount = self.__bankAccountRepository.findOneByAccountNumber(anotherBankAccountNumber)
            
            if bankAccount.isNone() is True:
                raise BankAccountNotFoundException()

            if anotherBankAccount.isNone() is True:
                raise BankAccountNotFoundException()

            bankAccount.moneyTransferToAnotherAccount(anotherBankAccount, amount)
            
            self.__bankAccountRepository.updateBalance(bankAccount)
            self.__bankAccountRepository.updateBalance(anotherBankAccount)


            self.__bankAccountRepository.persistTransaction(bankAccount)
            self.__bankAccountRepository.persistTransaction(anotherBankAccount)
            
            return BankAccountResponse(
                lastTransactionMessage=bankAccount.getTransactions()[-1].getDescription(),
                balance= bankAccount.getBalanceAsString()
            )

        except Exception as err:
            return ErrorResponse(err)


    def getAccountBalance(self, uuid:str) -> AbstractResponseViewModel: 
        try:
            bankAccount = self.__bankAccountRepository.findOneByUuid(uuid)

            if bankAccount.isNone() is True:
                raise BankAccountNotFoundException()
            return BankAccountResponse(balance=bankAccount.getBalanceAsString())
        except Exception as err:
            return ErrorResponse(err)

    def getLastFiveTransactionHistory(self, uuid:str) -> AbstractResponseViewModel:
        try:
            bankAccount = self.__bankAccountRepository.findOneByUuid(uuid)

            if bankAccount.isNone() is True:
                raise BankAccountNotFoundException()
            return BankAccountResponse(transactions=bankAccount.getLastFiveTransactionHistory())
        except Exception as err:
            return ErrorResponse(err)
