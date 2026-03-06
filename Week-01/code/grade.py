# I wanted to see if i could make a simple programm to calculate the cgpa of a student
# The formula is: CGPA = Total Grade Points Earned ÷ Total Credit Hours
name = input("What is your name? ")
subject1_grade = float(input(name + " what is the grade point of subject1? "))
subject2_grade = float(input(name + " what is the grade point of subject2? "))
subject3_grade = float(input(name + " what is the grade point of subject3? "))
subject1_credit = int(input(name + " What is the credit point if subject1? "))
subject2_credit = int(input(name + " What is the credit point if subject2? "))
subject3_credit = int(input(name + " What is the credit point if subject3? "))
subject1_point = subject1_grade * subject1_credit
subject2_point = subject2_grade * subject2_credit
subject3_point = subject3_grade * subject3_credit
total_point = subject1_point + subject2_point + subject3_point
total_credit = subject1_credit + subject2_credit + subject3_credit
if total_point == 0:
    print("Something is wrong please input your values again ")
if total_credit == 0:
    print("Something is wrong please input your values again ")
CGPA = total_point / total_credit
print(f"{name}, Your CGPA is {CGPA:.2f}")