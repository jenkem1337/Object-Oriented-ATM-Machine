from abc import ABC, abstractmethod



class BaseAtmViewState(ABC):
    @abstractmethod
    def run(self, atmView):pass
