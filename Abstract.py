from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def printinfo(self):
        print("This is a normal method in abstract class")

class square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        print("Area of Sqaure is ",self.side * self.side)

sq1 = square(5)
sq1.area()
sq1.printinfo()