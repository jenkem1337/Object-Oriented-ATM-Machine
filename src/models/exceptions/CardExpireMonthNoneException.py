class CardExpireMonthNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Kartın son kullanma tarihinin ay bölümünü boş geçilemez")