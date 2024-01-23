from abc import ABC, abstractmethod

# Using an abstract class as interface so the sorting algo
# classes will be forced to implement these methods
class SortAlgoInterface(ABC):

    @abstractmethod
    def sort(self, arr):
        pass

    @abstractmethod
    def getName(self):
        pass