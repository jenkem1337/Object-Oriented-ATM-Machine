class CardIsNoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Aradığınız kriterlerde bir kart yok")