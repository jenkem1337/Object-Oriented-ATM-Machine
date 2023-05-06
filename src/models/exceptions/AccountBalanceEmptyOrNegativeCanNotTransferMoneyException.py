class AccountBalanceEmptyOrNegativeCanNotTransferMoneyException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Banka hesabınızın bakiyesi yok veya negatif olduğu için başka bir hesaba para transfer edemezsiniz")