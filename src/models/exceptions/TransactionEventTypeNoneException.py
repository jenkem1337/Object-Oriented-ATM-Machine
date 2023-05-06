class TransactionEventTypeNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("İşlem geçmişi olayının ne olduğu boş geçilemez")