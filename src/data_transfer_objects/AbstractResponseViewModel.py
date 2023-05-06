from abc import ABC, abstractmethod

class AbstractResponseViewModel(ABC):
    
    def __init__(self,  event, responseObject) -> None:
        self.__event = event
        self.__responseObject = responseObject
    
    def isEventEqualToError(self):
        if self.__event == "error":
            return True

    def justGetResponseModel(self):
        return self.__responseObject

    def onSucsess(self, callback):
        if self.__event != "sucsess":
            return self
        callback(self.__responseObject) 
        return self
    
    def onError(self, callback):
        if self.__event != "error":
            return
        callback(self.__responseObject)