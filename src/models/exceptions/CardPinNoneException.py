class CardPinNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Kart şifresi boş geçilemez.")