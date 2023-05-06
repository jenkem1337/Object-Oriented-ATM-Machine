class TransactionDescriptionNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("İşlem geçmişinin açıklaması boş olamaz")