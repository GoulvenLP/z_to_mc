from abc import ABC, abstractmethod

class RootedRelation(ABC):
    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self, configuration):
        pass

    @abstractmethod
    def execute(self, configuration, action):
        pass
    