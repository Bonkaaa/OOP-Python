# 20237451 - Nguyen Huu Kien
from GeometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius: float, color: str, weight: float):
        """
        Initialize a Circle object.
        
        Args:
            radius (float): The radius of the circle
            color (str): The color of the circle (default: "white")
            weight (float): The weight of the circle (default: 1.0)
        """

        super().__init__(color, weight)
        self.radius = radius

    @property
    def radius(self) -> float:
        """Get the radius of the circle."""
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        """Set the radius of the circle."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = value

    def find_area(self):
        """Calculate and return the area of the circle."""
        return math.pi * pow(self.radius, 2)

    def find_perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius
    
    def toString(self):
        """Return a string representation of the Circle object."""
        print("--------------------------------")
        print("Circle Details:")
        print(f"Radius: {self.radius}")
        print(f"Color: {self.color}")
        print(f"Weight: {self.weight}")
        print(f"Area: {self.find_area():.2f}")
        print(f"Perimeter: {self.find_perimeter():.2f}")