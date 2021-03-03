# FEB 24
# Create a class Student having data members rollno, name, stream and marksList in which is a list of marks in 5 subjects
# use __init__() function to initialise data members.
# Make data member avg to calculate avg of marks of student

class Student:
  def __init__(self, name, roll, stream, marks):
    self.name = name
    self.rollno = roll
    self.stream = stream
    self.marksList = marks
  
  def avg(self):
    return sum(self.marksList) / 3

student = Student("Shaan Alam", 27, "BSC APS", [98, 99, 100])

print ("Name = ", student.name)
print ("Roll no = ", student.rollno)
print ("Stream = ", student.rollno)
print ("Marks = ", student.marksList)
print ("Average marks of",student.name," = ",student.avg())

