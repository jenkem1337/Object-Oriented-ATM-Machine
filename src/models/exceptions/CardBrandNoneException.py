class CardBrandNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Kart markası boş geçilemez")