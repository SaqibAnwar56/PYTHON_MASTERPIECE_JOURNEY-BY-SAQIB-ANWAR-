# STUDENT RESULT SUMMARY GENERATOR
# CREATED BY SAQIB ANWAR

print("Welcome to the Student Result Summary Generator!\n")

name = input("Enter Student's Name: ")
roll_no = input("Enter Student's Roll No: ")

python_marks = float(input("Enter Marks in Python: "))
html_marks = float(input("Enter Marks in HTML: "))
java_marks = float(input("Enter Marks in Java: "))

total_marks = python_marks + html_marks + java_marks
average = total_marks / 3

print("\n--- Result Summary ---")
print("Name:", name)
print("Roll No:", roll_no)
print("Python:", python_marks)
print("HTML:", html_marks)
print("Java:", java_marks)
print("Total Marks:", total_marks)
print("Average:", average)

print("\nStudent", name, "has secured", total_marks,
      "marks with an average of", average)
