class CardHolderNameAndCustomerFullNameNotEqualException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Kartın üzerinde yazan isim ile müşteri isimleri aynı değil.")