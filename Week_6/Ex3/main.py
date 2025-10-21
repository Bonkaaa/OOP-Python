# 20237451 - Nguyen Huu Kien

from Student import Student

print("20237451 - Nguyen Huu Kien")
print("----------------------------")

students = [
    Student("Alice", 3.5),
    Student("Bob", 3.9),
    Student("Charlie", 2.8),
    Student("Diana", 3.9),
]

# Sắp xếp tăng dần theo GPA
sorted_asc = sorted(students)
print("Sorted ascending by GPA:")
for s in sorted_asc:
    print(s)

# Sắp xếp giảm dần theo GPA
sorted_desc = sorted(students, reverse=True)
print("\nSorted descending by GPA:")
for s in sorted_desc:
    print(s)

# So sánh trực tiếp
print("\nCompare Bob vs Diana (gpa both 3.9):", students[1].compare_to(students[3]))
print("Is Alice < Bob? ->", students[0] < students[1])