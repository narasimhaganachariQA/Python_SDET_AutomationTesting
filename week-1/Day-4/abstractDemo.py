from abc import ABC, abstractmethod

#abstract class
class Browser(ABC):
    @abstractmethod
    def lauch(self):
        pass
    