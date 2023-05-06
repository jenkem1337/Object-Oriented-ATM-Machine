class AccountNumberLengthException(Exception):
    def __init__(self, *args: object) -> None:
        
        super().__init__("Banka hesap numarasının uzunluğu 16 karakter olmalı")