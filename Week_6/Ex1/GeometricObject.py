from abc import ABC, abstractmethod

class GeometricObject(ABC):
    def __init__(self, color: str, weight: float):
        """
        Initialize a geometric object with color and weight.
        
        Args:
            color (str): The color of the object (default: "white")
            weight (float): The weight of the object (default: 1.0)
        """
        self._color = color
        self._weight = weight

    @property
    def color(self):
        """
        Get the color of the geometric object.
         Returns:
            str: The color of the object.
        """
        return self._color
    
    @color.setter
    def color(self, value: str):
        """
        Set the color of the geometric object.
        Args:
            value (str): The new color of the object.
        """
        if not isinstance(value, str):
            raise ValueError("Color must be a string.")
        self._color = value

    @property
    def weight(self):
        """
        Get the weight of the geometric object.
        Returns:
            float: The weight of the object.
        """
        return self._weight
    
    @weight.setter
    def weight(self, value: float):
        """
        Set the weight of the geometric object.
        Args:
            value (float): The new weight of the object.
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Weight must be a positive number.")
        self._weight = value

    @abstractmethod
    def find_area(self):
        """Abstract method to calculate the area of the geometric object."""
        pass

    @abstractmethod
    def find_perimeter(self):
        """Abstract method to calculate the perimeter of the geometric object."""
        pass
