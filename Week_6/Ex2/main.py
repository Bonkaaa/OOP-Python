# 20237451 - Nguyen Huu Kien

from Student import Student
from Faculty import Faculty
from Staff import Staff


class Professor(Faculty):
	"""Concrete Faculty implementation for testing."""
	def __init__(self, name, number, email, department, salary, date_hired, office_hours, rank):
		super().__init__(name, number, email, department, salary, date_hired, office_hours, rank)

	def calculateBonus(self):
		# Use Faculty's base plus an extra percentage for professors
		return 1000 + (0.05 * self._salary) + (0.02 * self._salary)

	def calculateVacation(self):
		# Use Faculty's logic but convert weeks to days for demonstration
		weeks = super().calculateVacation()
		return weeks * 7


def main():
	print("20237451 - Nguyen Huu Kien")
	print("----------------------------")
	# Create a Student
	student = Student("Alice Morgan", "555-0101", "alice@example.com", "Computer Science")

	# Create a Staff member (hired 01/01/2020)
	staff = Staff("Bob Smith", "555-0202", "bob@example.com", "Administration", 45000, "01/01/2020", "Office Manager")

	# Create a Professor (hired 15/09/2018)
	prof = Professor("Dr. Carol Lee", "555-0303", "carol@example.com", "Mathematics", 80000, "15/09/2018", 10.0, "Senior Lecturer")

	print("--- Student ---")
	student.toString()
	print(f"Program: {student.program}")

	print("\n--- Staff ---")
	staff.toString()
	print(f"Title: {staff.title}")
	try:
		print(f"Staff bonus: {staff.calculateBonus():.2f}")
		print(f"Staff vacation (weeks): {staff.calculateVacation()}")
	except Exception as e:
		print("Error calculating staff details:", e)

	print("\n--- Professor ---")
	prof.toString()
	print(f"Office hours: {prof.office_hours}")
	print(f"Rank: {prof.rank}")
	try:
		print(f"Professor bonus: {prof.calculateBonus():.2f}")
		print(f"Professor vacation (days): {prof.calculateVacation()}")
	except Exception as e:
		print("Error calculating professor details:", e)


if __name__ == "__main__":
	main()


