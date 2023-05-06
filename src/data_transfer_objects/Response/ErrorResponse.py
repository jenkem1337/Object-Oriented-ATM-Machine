from data_transfer_objects.AbstractResponseViewModel import AbstractResponseViewModel


class ErrorResponse(AbstractResponseViewModel):
    def __init__(self, message:str) -> None:
        super().__init__("error", self)
        self.errorMessage = message