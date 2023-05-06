class CustomerSurnameNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Müşteri soyismi boş geçilemez")