class IbanNoControllCharacterException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Iban no kontrol karakterleri kesinlikle sayı olmalı")