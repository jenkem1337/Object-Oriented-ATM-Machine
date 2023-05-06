from datetime import datetime
from models.abstract.ICard import ICard
from models.abstract.ITransaction import ITransaction
from models.factory.AbstractModelFactory import AbstractModelFactory
from models.abstract.IBankAccount import IBankAccount
from repository.abstract.IBankAccountRepository import IBankAccountRepository
import json

from repository.mapper.IDomainModelMapper import IDomainModelMapper

class BankAccountRepositoryImpl(IBankAccountRepository):
    
    __bankAccountFactory: AbstractModelFactory[IBankAccount]
    __cardFactory       : AbstractModelFactory[ICard]
    __transactionFactory: AbstractModelFactory[ITransaction]
    __bankAccountDomainMapper : IDomainModelMapper[IBankAccount]
    
    def __init__(
            self,
            bankAccountFactory:AbstractModelFactory[IBankAccount],
            cardFactory:AbstractModelFactory[ICard], 
            transactionFactory: AbstractModelFactory[ITransaction],
            bankAccountDomainMapper: IDomainModelMapper[IBankAccount]) -> None:
        self.__bankAccountFactory = bankAccountFactory
        self.__cardFactory        = cardFactory
        self.__transactionFactory = transactionFactory
        self.__bankAccountDomainMapper = bankAccountDomainMapper
    
    def findOneByUuid(self, uuid:str) -> IBankAccount:
            bankAccountJson: dict = self.__readFromJsonFileWithHashTable("uuid", key = uuid)            
            return self.__bankAccountDomainMapper.mapFromDictToSingleModel(
                                                    bankAccountJson, 
                                                    bankAccountFactory = self.__bankAccountFactory,
                                                    cardFactory        = self.__cardFactory,
                                                    trasanctionFactory = self.__transactionFactory
                                                )    
    def findOneByAccountNumber(self, accountNumber:str) -> IBankAccount: 
        bankAccountJson = self.__readFromJsonFileWithHashTable("account_no", key = accountNumber)
        return self.__bankAccountDomainMapper.mapFromDictToSingleModel(                                                    
                                                    bankAccountJson, 
                                                    bankAccountFactory = self.__bankAccountFactory,
                                                    cardFactory        = self.__cardFactory,
                                                    trasanctionFactory = self.__transactionFactory
                                                )
    
    def findOneByIBAN(self, iban:str) -> IBankAccount:
        bankAccountJson = self.__readFromJsonFileWithHashTable("iban_no", key = iban)
        return self.__bankAccountDomainMapper.mapFromDictToSingleModel(                                                    
                                                    bankAccountJson, 
                                                    bankAccountFactory = self.__bankAccountFactory,
                                                    cardFactory        = self.__cardFactory,
                                                    trasanctionFactory = self.__transactionFactory
                                                )


    
    def findOneByCustomerUuid(self, uuid:str) -> IBankAccount:
        bankAccountJson = self.__readFromJsonFileWithHashTable("customer_uuid", key = uuid)
        return self.__bankAccountDomainMapper.mapFromDictToSingleModel(                                                    
                                                    bankAccountJson, 
                                                    bankAccountFactory = self.__bankAccountFactory,
                                                    cardFactory        = self.__cardFactory,
                                                    trasanctionFactory = self.__transactionFactory
                                                )
  

    
    def updateBalance(self, bankAcc:IBankAccount) -> None: 
        
        def callback(bankAccountJson):
            bankAccountJson["balance"] = bankAcc.getBalance()
             
        self.__update("uuid", hash_key = bankAcc.getUuid(), what_will_update = "balance", callback_function = callback)
    
    def persistTransaction(self, bankAccountDomainModel: IBankAccount) -> None:
        newTransaction: ITransaction = bankAccountDomainModel.getTransactions()[-1]
        transactionDict = {
                            "uuid":newTransaction.getUuid(),
                            "owner_uuid":newTransaction.getOwnerUuid(),
                            "event_type":newTransaction.getEventType(),
                            "description":newTransaction.getDescription(),
                            "time_stampt":newTransaction.getTimeStampt()
                        }
        self.__append("uuid", hash_key=bankAccountDomainModel.getUuid(), where_to_append="transactions", new_transaction=transactionDict)

    def __readFromJsonFileWithHashTable(self, hashTableKey, **kwargs) -> dict:
        with open("src/db/bank_db_hash_table.json", mode="r", encoding="utf-8") as bankDBHashTable:
            try:
                hashTableData = json.load(bankDBHashTable)
                bankAccountIndex = hashTableData["bank_accounts"][hashTableKey][kwargs.get("key")]
            except:
                pass

        with open("src/db/bank_db.json", mode="r", encoding="utf-8") as bankDB:
                try:
                    bankDBJsonData = json.load(bankDB)
                    bankAccountJson:dict = bankDBJsonData["bank_accounts"][bankAccountIndex]
                except:
                    bankAccountJson:dict = self.__nullBankAccountDict()
        return bankAccountJson

    def __update(self, hashTableKey, **kwargs):

        with open("src/db/bank_db_hash_table.json", mode="r", encoding="utf-8") as bankDBHashTable:
            try:
                hashTableData = json.load(bankDBHashTable)
                bankAccountIndex = hashTableData["bank_accounts"][hashTableKey][kwargs.get("hash_key")]
            except:
                pass

        with open("src/db/bank_db.json", mode="r", encoding="utf-8") as bankDB:
                try:
                    bankDBJsonData = json.load(bankDB)
                    bankAccountJson:dict = bankDBJsonData["bank_accounts"][bankAccountIndex]
                except:
                    bankAccountJson:dict = self.__nullBankAccountDict()
        callbackFunction = kwargs.get("callback_function")
        callbackFunction(bankAccountJson)
        #bankAccountJson[kwargs.get("what_will_update")] = kwargs.get("new_data")
        
        with open("src/db/bank_db.json", mode="r", encoding="utf-8") as bankDB2:
                oldBankDbJsonData = json.load(bankDB2)
                oldBankDbJsonData["bank_accounts"][bankAccountIndex][kwargs.get("what_will_update")] = bankAccountJson[kwargs.get("what_will_update")]
                
        with open("src/db/bank_db.json", mode="w", encoding="utf-8") as bankDB3:
            bankDB3.write(json.dumps(oldBankDbJsonData, indent=4))
    
    def __append(self, hashTableKey, **kwargs):
        with open("src/db/bank_db_hash_table.json", mode="r", encoding="utf-8") as bankDBHashTable:
            try:
                hashTableData = json.load(bankDBHashTable)
                bankAccountIndex = hashTableData["bank_accounts"][hashTableKey][kwargs.get("hash_key")]
            except:
                pass

        
        with open("src/db/bank_db.json", mode="r", encoding="utf-8") as bankDB2:
                BankDbJsonData = json.load(bankDB2)
                
        
        BankDbJsonData["bank_accounts"][bankAccountIndex][kwargs.get("where_to_append")].append(kwargs.get("new_transaction"))
    
        with open("src/db/bank_db.json", mode="w", encoding="utf-8") as bankDB3:
            bankDB3.write(json.dumps(BankDbJsonData, indent=4))

    def __nullBankAccountDict(self) -> dict :
        nullBankAccountJson = {
                    "uuid":None,
                    "account_no":None,
                    "iban":None,
                    "customer_uuid": None,
                    "password":None,
                    "balance":None,
                    "cards": [{
                            "uuid":None,
                            "owner_uuid":None,
                            "number":None,
                            "brand":None,
                            "card_exp_month":None,
                            "card_exp_year":None,
                            "cvv":None,
                            "pin":None,
                            "holder_fullname":None
                        }],
                    "transactions": [{
                                        "uuid":None,
                                        "owner_uuid":None,
                                        "event_type":None,
                                        "description":None,
                                        "time_stampt":None

                    }]
                }
        return nullBankAccountJson
