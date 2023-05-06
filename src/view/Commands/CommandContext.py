from view.abstract.ICommand import ICommand


class CommandContext:
    def __init__(self) -> None:
        self.__dict = dict[str, ICommand]()

    def getCommand(self, key:str) -> ICommand:
        if self.__dict[key] is None:
            raise Exception("CommandContext için böyle bir anahtar kelime yok")
        return self.__dict.get(key)
    
    def setCommand(self, key:str, value:ICommand):
        self.__dict[key] = value
        return self