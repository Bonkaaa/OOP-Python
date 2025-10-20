class Employee:
    def __init__(self, firstName: str, lastName: str, address: str, sin: float, salary: float):
        """
        Initializes an Employee object.

        Args:
            firstName (str): The first name of the employee.
            lastName (str): The last name of the employee.
            address (str): The address of the employee.
            sin (float): The social insurance number of the employee.
            salary (float): The salary of the employee.
        """
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.sin = sin
        self.salary = salary

    def toString(self) -> str:
        """
        Returns a string representation of the Employee object.

        Returns:
            str: A string containing the employee's details.
        """
        return (f"Employee Details:\n"
                f"First Name: {self.firstName}\n"
                f"Last Name: {self.lastName}\n"
                f"Address: {self.address}\n"
                f"SIN: {self.sin}\n"
                f"Salary: ${self.salary:,.2f}")
    
    def calculate_bonus(self, bonus_percentage: float) -> float:
        """
        Calculates the bonus based on the salary and bonus percentage.

        Args:
            bonus_percentage (float): The bonus percentage to be applied.

        Returns:
            float: The calculated bonus amount.
        """
        return self.salary * bonus_percentage / 100
    
if __name__ == "__main__":
    firtName = input("Enter employee's first name: ")
    lastName = input("Enter employee's last name: ")
    address = input("Enter employee's address: ")
    sin = float(input("Enter employee's SIN: "))
    salary = float(input("Enter employee's salary: "))
    print("--------------------------------")
    employee = Employee(firtName, lastName, address, sin, salary)
    print(employee.toString())
    bonus = input("Enter bonus percentage: ")
    bonus = employee.calculate_bonus(float(bonus))
    print(f"Bonus: ${bonus:,.2f}")