# 20237451 - Nguyen Huu Kien

from Person import Person

class Student(Person):
    def __init__(self, name: str, phone_number: str, email: str, program: str):
        """
        Initialize a Student object.
        Args:
            name (str): The name of the student.
            phone_number (str): The phone number of the student.
            email (str): The email address of the student.
            program (str): The program of the student.
        """
        super().__init__(name, phone_number, email)
        self._program = program

    @property
    def program(self):
        """Get the program of the student."""
        return self._program
    
    @program.setter
    def program(self, value: str):
        """Set the program of the student."""
        if not isinstance(value, str):
            raise ValueError("Program must be string format")
        
        self._program = value
