class CardExpireYearNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Kartın son kullanma tarihinin yıl bölümünü boş geçilemez")