class BankAccountNotFoundException(Exception):
    def __init__(self, *args: object) -> None:
        self.errorMessage = "Aradığınız banka hesabı bulunamadı."
        super().__init__(self.errorMessage)