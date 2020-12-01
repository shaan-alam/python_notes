number_of_students = int(input("Enter the number of students : "))
marks = 0
highest_marks = -1

for i in range(number_of_students):
    marks = eval(input("Enter the marks: "))
    if marks > highest_marks:
        highest_marks = marks

print ("Highest Marks = ", highest_marks)

