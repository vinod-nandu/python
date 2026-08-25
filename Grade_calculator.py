# Student Grade Calculator
# This program takes a student's mark as input
# and displays the corresponding grade.

# Get mark from user
mark = int(input("Enter the student's mark (0-100): "))

# Determine grade using conditional statements
if mark >= 90 and mark <= 100:
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >= 70:
    grade = "C"
elif mark >= 60:
    grade = "D"
elif mark >= 0:
    grade = "E"
else:
    grade = "Invalid Mark"

# Display result
print(f"\nStudent Mark : {mark}")
print(f"Student Grade: {grade}")
