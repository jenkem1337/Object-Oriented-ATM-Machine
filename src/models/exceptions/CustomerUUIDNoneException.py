class CustomerUUIDNoneExcepetion(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Müşteri UUID boş geçilemez")