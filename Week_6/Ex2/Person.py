# 20237451 - Nguyen Huu Kien

class Person:
    def __init__(self, name: str, number: str, email: str):
        """
        Initialize a Person object.
        Args:
            name (str): The name of the person.
            number (str): The phone number of the person.
            email (str): The email address of the person.
        """
        self._name = name
        self._phone_number = number
        self._email = email

    @property
    def name(self):
        """Get the person's name."""
        return self._name
    
    @name.setter
    def name(self, value: str):
        """Set the person's name."""
        self._name = value

    @property
    def phone_number(self):
        """Get the person's phone number."""
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value: str):
        """Set the person's phone number."""
        self._phone_number = value

    @property
    def email(self):
        """Get the person's email address."""
        return self._email

    @email.setter
    def email(self, value):
        """Set the person's email address."""
        self._email = value

    def toString(self):
        print("--------------------------------")
        print("Person Details:")
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email Address: {self.email}")

    