from abc import ABC, abstractmethod

class ProviderInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def send_data(self, data):
        pass
