from abc import ABC, abstractmethod
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/   here the idea
/   http://www.dofactory.com/net/composite-design-pattern
/   The idea is to basically have one singler object
/   that can have copies of its self.
/   It sort of strays away from the complete idea but
/   this is where the idea came from
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
class Composite(ABC):
    @abstractmethod
    def getNeededItems(self):
        pass

    @abstractmethod
    def predict(self, data):
        pass
    