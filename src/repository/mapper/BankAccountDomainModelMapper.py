from datetime import datetime
from models.abstract.ICard import ICard
from models.abstract.ITransaction import ITransaction
from models.factory.AbstractModelFactory import AbstractModelFactory
from models.abstract.IBankAccount import IBankAccount
from repository.mapper.IDomainModelMapper import IDomainModelMapper


class BankAccountDomainModelMapper(IDomainModelMapper[IBankAccount]):
    def mapFromDictToSingleModel(self, bankAccountJson: dict, **additionalParamaters) -> IBankAccount:
            
        bankAccountFactory: AbstractModelFactory[IBankAccount] = additionalParamaters.get("bankAccountFactory")
        cardFactory       : AbstractModelFactory[ICard]        = additionalParamaters.get("cardFactory")
        transactionFactory: AbstractModelFactory[ITransaction] = additionalParamaters.get("trasanctionFactory")
        
        bankAccountDomainObject = bankAccountFactory \
                                        .itCanBeNullable() \
                                        .createInstance(
                                            uuid           = bankAccountJson.get("uuid"),
                                            account_number = bankAccountJson.get("account_no"),
                                            iban           = bankAccountJson.get("iban"),
                                            customer_uuid  = bankAccountJson.get("customer_uuid"),
                                            password       = bankAccountJson.get("password"),
                                            balance        = bankAccountJson.get("balance")
                                        )
        for cardObject in bankAccountJson.get("cards"):
            cardDomainObject = cardFactory .itCanBeNullable() \
                                            .createInstance(
                                               uuid = cardObject["uuid"],
                                               owner_uuid = cardObject["owner_uuid"],
                                               card_number = cardObject["number"],
                                               pin = cardObject["pin"],
                                               expire_month = cardObject["card_exp_month"],
                                               expire_year = cardObject["card_exp_year"],
                                               cvv = cardObject["cvv"],
                                               brand = cardObject["brand"],
                                               holder_name = cardObject["holder_fullname"]
                                            )
            if cardDomainObject.isNone() is False:
                bankAccountDomainObject.addCard(cardDomainObject)

        for transactionObject in bankAccountJson.get("transactions"):
            
            if transactionObject["time_stampt"] is None:
                transactionObject["time_stampt"] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            
            transactionDomainObject = transactionFactory.itCanBeNullable() \
                                                        .createInstance(
                                                            uuid = transactionObject["uuid"],
                                                            owner_uuid = transactionObject["owner_uuid"],
                                                            event_type = transactionObject["event_type"],
                                                            description = transactionObject["description"],
                                                            time_stampt = datetime.strptime(transactionObject["time_stampt"], "%d/%m/%Y %H:%M:%S")
                                                        )
            if transactionDomainObject.isNone() is False:
                bankAccountDomainObject.addTransaction(transactionDomainObject)

        return bankAccountDomainObject
    
    def mapFromModelToDict(self, domainModel: IBankAccount, **additionalParamaters) -> dict:
        bankAccountDict = {
                    "uuid":domainModel.getUuid(),
                    "account_no":domainModel.getAccountNumber(),
                    "iban":domainModel.getIban(),
                    "customer_uuid": domainModel.getCustomerUuid(),
                    "password":domainModel.getPassword(),
                    "balance":domainModel.getPassword(),
                    "cards": domainModel.getCards().values(),
                    "transactions": domainModel.getTransactions()
                }
        return bankAccountDict