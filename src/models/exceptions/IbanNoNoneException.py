class IbanNoNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Girilen IBAN numarası boş geçilemez")