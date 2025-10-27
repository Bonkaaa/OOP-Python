# 20237451 - Nguyen Huu Kien

from Employee import Employee

class Staff(Employee):
    def __init__(self, name, number, email, department, salary, date_hired, title: str):
        """
        Initialize a Staff object.
        Args:
            name (str): The name of the staff member.
            number (str): The phone number of the staff member.
            email (str): The email address of the staff member.
            department (str): The department of the staff member.
            salary (float): The salary of the staff member.
            date_hired (str): The date the staff member was hired in "DD/MM/YYYY" format.
            title (str): The title of the staff member.
        """
        super().__init__(name, number, email, department, salary, date_hired)
        self._title = title

    @property
    def title(self):
        """Get the title of the staff member."""
        return self._title

    @title.setter
    def title(self, value: str):
        """Set the title of the staff member."""
        if not isinstance(value, str):
            raise ValueError("Title must be in string format")
        self._title = value

    def calculateBonus(self):
        """Calculate the bonus for the staff member."""
        return 0.06 * self._salary
    
    def calculateVacation(self):
        """Calculate the vacation weeks for the staff member."""
        years_service = self.years_of_service()

        if years_service >= 5:
            vacation_weeks = 4
        else:
            vacation_weeks = 3

        return vacation_weeks