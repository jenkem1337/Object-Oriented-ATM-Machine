class CardCVVNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Kartın 3 haneli CVV bölümü boş geçilemez")