class IbanNoCountryCodeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Iban numarasının ilk iki karakteri büyük harfle başlamalı")