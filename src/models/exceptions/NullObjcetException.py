class NullObjectException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Null Object")