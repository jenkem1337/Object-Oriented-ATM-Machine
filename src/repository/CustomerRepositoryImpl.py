import json
from models.factory.AbstractModelFactory import AbstractModelFactory
from models.abstract.ICustomer import ICustomer
from models.null_objects.NullCustomer import NullCustomer
from repository.abstract.ICustomerRepository import ICustomerRepository


class CustomerRepositoryImpl(ICustomerRepository):
    __customerFactory: AbstractModelFactory[ICustomer]
    def __init__(self, customerFactory: AbstractModelFactory[ICustomer]) -> None:
        self.__customerFactory = customerFactory
    
    def findOneByUuid(self, uuid: str) -> ICustomer:
        with open("src/db/bank_db_hash_table.json",mode="r",encoding="utf-8") as bankDBHashTable:
            try:
                hashTableData = json.load(bankDBHashTable)
                customerIndex = hashTableData["customers"]["uuid"][uuid]
            except:
                pass

        with open("src/db/bank_db.json",mode="r",encoding="utf-8")  as bankDB:
            try:
                bankDBJsonData = json.load(bankDB)
                customerJson = bankDBJsonData["customers"][customerIndex]
            except:
                customerJson = {
                    "uuid":None,
                    "name":None,
                    "surname":None
                }
        
        return self.__customerFactory.itCanBeNullable().createInstance(
            uuid = customerJson.get("uuid"),
            name = customerJson.get("name"),
            surname = customerJson.get("surname")
        )