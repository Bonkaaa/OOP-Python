# 20237451 - Nguyen Huu Kien

from Employee import Employee
from abc import ABC, abstractmethod

class Faculty(Employee, ABC):
    def __init__(self, name, number, email, department, salary, date_hired, office_hours: float, rank: int):
        """
        Initialize a Faculty object.
        Args:
            name (str): The name of the faculty member.
            number (str): The phone number of the faculty member.
            email (str): The email address of the faculty member.
            department (str): The department of the faculty member.
            salary (float): The salary of the faculty member.
            date_hired (str): The date the faculty member was hired in "DD/MM/YYYY" format.
            office_hours (float): The office hours of the faculty member.
            rank (str): The rank of the faculty member.
        """
        
        super().__init__(name, number, email, department, salary, date_hired)
        self._office_hours = office_hours
        self._rank = rank

    @property
    def office_hours(self):
        """Get the office hours of the faculty member."""
        return self._office_hours
    
    @office_hours.setter
    def office_hours(self, value: float):
        """Set the office hours of the faculty member."""
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Office hours must be a number and can not be negative")
        
        self._office_hours = value
        
    @property
    def rank(self):
        """Get the rank of the faculty member."""
        return self._rank
    
    @rank.setter
    def rank(self, value: str):
        """Set the rank of the faculty member."""
        if not isinstance(value, str):
            raise ValueError("Rank must be in string format")
        
        self._rank = value

    @abstractmethod
    def calculateBonus(self):
        """Calculate the bonus for the faculty member."""
        return 1000 + (0.05 * self._salary)
    
    @abstractmethod
    def calculateVacation(self):
        """Calculate the vacation weeks for the faculty member."""
        years_service = self.years_of_service()

        if years_service >= 3:
            vacation_weeks = 5
            if self._rank == "Senior Lecturer":
                vacation_weeks += 1
        else:
            vacation_weeks = 4

        return vacation_weeks

        