from abc import ABC, abstractmethod
class Shape(ABC) :

    @abstractmethod   
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return (self.width + self.height)*2


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius * self.radius * 3.14159
    
    def calculate_perimeter(self):
        return (self.radius + self.radius) * 3.14159
    
shapes = []

r1 = Rectangle(2,4)
c1 = Circle(7)

shapes.append(r1)
shapes.append(c1)

for Shape in shapes:
    print (" shape : ", Shape.__class__.__name__)
    print (" area : ", Shape.calculate_area())
    print (" perimeter : ", Shape.calculate_perimeter())
    print (25 * "-")
