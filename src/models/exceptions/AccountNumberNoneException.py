class AccountNumberNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Hesap numarası boş geçilemez")