class CustomerNotFoundException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Aradığını müşteri bulunamadı.")