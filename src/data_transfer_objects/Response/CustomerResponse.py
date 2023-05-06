from data_transfer_objects.AbstractResponseViewModel import AbstractResponseViewModel


class CustomerResponse(AbstractResponseViewModel):
    def __init__(self, uuid:str, fullName:str) -> None:
        super().__init__("sucsess", self)
        self.uuid = uuid
        self.fullName = fullName