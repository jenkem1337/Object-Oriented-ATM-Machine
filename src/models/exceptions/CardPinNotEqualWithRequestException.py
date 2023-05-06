class CardPinNotEqualWithRequestException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Kart şifresi girdiğiniz şifre ile aynı değil.")