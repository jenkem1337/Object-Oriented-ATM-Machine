import uuid
import re
class Validator:
    
    @staticmethod
    def isUUIDValid(_uuid:str, customException = None):

        try:
            uuid.UUID(_uuid)
            return True
        except ValueError:
            if customException is not None:
                raise customException()

            raise Exception("UUID geçersiz")

    @staticmethod
    def isNone(input, customException = None):
        if input is None:
            if customException is not None:
                raise customException()
            raise Exception("Girilen değer None tipinde olamaz")
    


    @staticmethod
    def isStringLengthLongerThan(leastLength:int, input:str, customException = None):
        if len(input) < abs(leastLength):
            if customException is not None:
                raise customException()
            errorMessage = "Girdiğiniz değerin uzunluğu en az {} olmalıdır".format(leastLength + 1)
            raise Exception(errorMessage)

    @staticmethod
    def isIntegerValueNegative(integer:int, customException = None):
        if integer < 0:
            if customException is not None:
                raise customException()

            raise Exception("Girilen değer negatif olamaz")
    @staticmethod
    def isIntegerValueZeroOrNegative(integer: int, customException = None):
        if integer <= 0:
            if customException is not None:
                raise customException()
            raise Exception("Girilen değer 0 veya negatif olamaz")
    @staticmethod
    def isStringLengthEqualTo(length: int, string:str, customException = None):
        if len(string) != length:
            if customException is not None:
                raise customException()

            errorMessage = "Girilen değerin uzunluğu {} sayısına eşit olmalı".format(length)
            raise Exception(errorMessage)

    @staticmethod
    def isAlpaNumeric(string:str, customException = None):
        if string.isalnum() is False:
            if customException is not None:
                raise customException()

            errorMessage = "Girilen {} değeri alfa nümerik değil".format(string)
            raise Exception(errorMessage)

    @staticmethod
    def isUpperCase(string: str, customException = None):
        if string.isupper() is False:
            if customException is not None:
                raise customException()

            errorMessage = "Girilen {} değeri büyük harf olmalı".format(string)
            raise Exception(errorMessage)

    @staticmethod
    def isStringValueEqualToIntegerValue(string:str, customException = None):
        try:
            int(string)
        except:
            if customException is not None:
                raise customException()

            errorMessage = "Girilen {} değeri bir sayı olmalı".format(string)
            raise Exception(errorMessage)
        
    @staticmethod
    def areStringValuesSameWithEachOther(str1:str, str2:str, customException = None):
        if str1 != str2:
            if customException is not None:
                raise customException()
            errorMessage = "{} değeri {} değeriyle aynı değil".format(str1, str2)
            raise Exception(errorMessage)
