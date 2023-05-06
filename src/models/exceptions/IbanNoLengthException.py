class IbanNoLengthException (Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("IBAN numarasının uzunluğu 26 karakter olmalıdır")