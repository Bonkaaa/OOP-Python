# 20237451 - Nguyen Huu Kien

from Person import Person
from abc import abstractmethod, ABC
from datetime import datetime
from typing import Union

class Employee(Person, ABC):
    def __init__(self, name, number, email, department: str, salary: float, date_hired: Union[str, datetime]):
        """
        Initialize an Employee object.

        Args:
            name (str): The name of the employee.
            number (str): The phone number of the employee.
            email (str): The email address of the employee.
            department (str): The department of the employee.
            salary (float): The salary of the employee.
            date_hired (str | datetime): The date the employee was hired in "DD/MM/YYYY" format or a datetime.
        """
        super().__init__(name, number, email)
        self._department = department
        self._salary = None
        self.salary = salary  # use setter to validate
        # Use the property setter so parsing/validation happens
        self.date_hired = date_hired

    @property
    def department(self):
        """Get the employee's department."""
        return self._department

    @department.setter
    def department(self, value: str):
        """Set the employee's department."""
        if not isinstance(value, str):
            raise ValueError("Department must be a string")
        self._department = value

    @property
    def salary(self):
        """Get the employee's salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float):
        """Set the employee's salary."""
        if not isinstance(value, (int, float)):
            raise ValueError("Salary must be a number")
        if value <= 0:
            raise ValueError("Salary must be greater than 0")
        self._salary = float(value)

    @property
    def date_hired(self):
        """Get the employee's date hired as a datetime."""
        return self._date_hired

    @date_hired.setter
    def date_hired(self, value: Union[str, datetime]):
        """Set the employee's date hired.

        Accepts either a datetime object or a string in "DD/MM/YYYY" format.
        """
        if isinstance(value, datetime):
            self._date_hired = value
            return

        if not isinstance(value, str):
            raise ValueError("date_hired must be a datetime or a string in 'DD/MM/YYYY' format")

        date_hired_str = value.strip()
        try:
            self._date_hired = datetime.strptime(date_hired_str, "%d/%m/%Y")
        except ValueError as e:
            raise ValueError("date_hired string must be in 'DD/MM/YYYY' format") from e

    def years_of_service(self):
        """Calculate the years of service of the employee."""
        current_date = datetime.now()
        # ensure _date_hired is a datetime
        if not isinstance(self._date_hired, datetime):
            raise TypeError("Internal error: _date_hired is not a datetime")
        return (current_date - self._date_hired).days / 365.25

    @abstractmethod
    def calculateBonus(self):
        """Calculate the bonus for the employee."""
        pass

    @abstractmethod
    def calculateVacation(self):
        """Calculate the vacation weeks for the employee."""
        pass