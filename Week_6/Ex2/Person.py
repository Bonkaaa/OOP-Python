class Person:
    def __init__(self, name: str, number: str, email: str):
        self._name = name
        self._phone_number = number
        self._email = email

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def email_address(self):
        """Get the person's email address."""
        return self._email_address
    
    @email_address.setter
    def email_address(self, value):
        """Set the person's email address."""
        self._email_address = value

    def toString(self):
        print("--------------------------------")
        print("Person Details:")
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email Address: {self.email_address}")

    