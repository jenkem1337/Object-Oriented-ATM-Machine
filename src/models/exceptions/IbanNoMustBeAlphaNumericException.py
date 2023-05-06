class IbanNoMustBeAlphaNumericException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Iban numarası alfa numerik olmalıdır")