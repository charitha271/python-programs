print("===== STUDENT INFORMATION =====")

name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
course = input("Enter course: ")
semester = input("Enter semester: ")
marks = float(input("Enter marks: "))

print("\n===== STUDENT DETAILS =====")
print("Name:", name)
print("Roll Number:", roll_number)
print("Course:", course)
print("Semester:", semester)
print("Marks:", marks)

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
print("============================")