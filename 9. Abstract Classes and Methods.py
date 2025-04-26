from abc import ABC, abstractmethod

class Shape(ABC):  # Inherit from ABC (Abstract Base Class)
    @abstractmethod
    def area(self):
        pass  # No implementation in abstract method

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):  # Must implement the abstract method
        return self.length * self.width

# Usage
rect = Rectangle(5, 3)
print("Rectangle area:", rect.area())  # Output: 15

# This will raise an error because Shape is abstract:
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape