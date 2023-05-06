class CardPinLengthMustBeFourException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Kart şifresi 4 karakter olmalı")