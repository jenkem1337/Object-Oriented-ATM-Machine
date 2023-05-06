class CardNumberNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Kart numarası boş geçilemez")