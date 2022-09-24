# Team - GoBeans
# Owner - Shakti Kumar Singh

'''
This example demonstrate the python function

Calculating the Grade of student based on the exam marks
'''

def calculate_average(marks):
    total_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = total_marks / total_subjects
    return average_marks

def calculate_grade(average_marks):
    if average_marks >= 80:
        grade = "A"
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 40:
        grade = 'C'
    else:
        grade = 'D'
    
    return grade


marks = [90, 40, 78, 88, 65]
average_marks = calculate_average(marks)
print("Your average marks is ", average_marks)

grade = calculate_grade(average_marks)
print("Your grade in exam is ", grade)