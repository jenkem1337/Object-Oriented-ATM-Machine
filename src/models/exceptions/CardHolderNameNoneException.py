class CardHolderNameNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Kart sahibinin isim soyismi boş geçilemez")