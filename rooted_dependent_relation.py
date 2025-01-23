from abc import ABC, abstractmethod

class RootedDependentRelation(ABC):

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self, input, config):
        pass

    @abstractmethod
    def execute(self, a, i, c):
        pass