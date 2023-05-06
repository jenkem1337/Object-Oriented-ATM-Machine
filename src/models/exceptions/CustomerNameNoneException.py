class CustomerNameNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Müşteri ismi boş geçilemez")