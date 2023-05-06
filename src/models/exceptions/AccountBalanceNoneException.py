class AccountBalanceNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Hesap bakiyesi boş geçilemez")