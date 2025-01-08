from abc import ABC, abstractmethod

class RootedGraph(ABC):
    
    @abstractmethod
    def neighbors(self, v):
        pass

    @abstractmethod
    def roots(self):
        pass

