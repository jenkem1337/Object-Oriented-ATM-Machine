from models.factory.AbstractModelFactory import AbstractModelFactory
from models.abstract.ICard import ICard
from models.Card import Card
from models.null_objects.NullCard import NullCard

class CardFactory(AbstractModelFactory[ICard]):
    def createInstance(self, **args) -> ICard:
        if self._isMustBeConcreate is True:
            return Card(
                args.get("uuid"), 
                args.get("owner_uuid"), 
                args.get("card_number"),
                args.get("pin"),
                args.get("expire_month"), 
                args.get("expire_year"), 
                args.get("cvv"), 
                args.get("brand"),
                args.get("holder_name")
            )
        
        if self._isMustBeConcreate is False:
            try:
                return Card(                
                    args.get("uuid"), 
                    args.get("owner_uuid"), 
                    args.get("card_number"),
                    args.get("pin"),
                    args.get("expire_month"), 
                    args.get("expire_year"), 
                    args.get("cvv"), 
                    args.get("brand"),
                    args.get("holder_name")
                )
            except Exception as err:
                print(err.args)
                return NullCard()
