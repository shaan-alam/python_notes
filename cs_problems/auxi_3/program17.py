
# FEB 24
# Define a class Student that keeps track of academic record of stdents in a school.The
# class should contain the following data members:
#    1.rollNum - Roll number of Student
#    2.name - Name of Student
#    3.marksList - List of marks in Five subjects
#    4.stream - A : Arts ; C : Commerce ; S : Science
#    5.percentage - Percentage compound using marks
#    6.grade - grade in each subject computed using marks
#    7.division - Division computed on the basis of overall Percentage.
# The class should support the following methods:
# (a) _init_for initializing the data members.
# (b) setMarks to take marks for five subjects as an input from the user.
# (c) getStream for acccessing the stream of the student.
# (d) percentage for computing the overall percentage for the student.
# (e) gradeGen that generates grades for each student in each course on the basis of the marks
# obtained. Criteria for computing the grade is as follows:
#           Marks                Grade
#           >=90                  A
#           <90 and >=80          B
#           <80 and >=65          C
#           <65 and >=40          D
#           <40                   E
# (f) division for computing division on the basis of the following criteria based on overall percentage of marks scored:
#           Percentage            Division
#           >=60                    I
#           <60 and >=50            II
#           <50 and >=35            III

# class Student:
#   def __init__(self, rollNum, name, stream):
#     self.rollNum = rollNum
#     self.name = name
#     self.marksList = []
#     self.stream = stream
#     self.percentage = 0
#     self.grade = ""
#     self.divison = ""

#   def setMarks(self):
#     print ("Enter marks for 5 subjects: ")
#     for x in range(5):
#       value = eval(input("Enter marks : "))

#       self.marksList.append(value)

#   def getPercentage(self):
#     return (sum(self.marksList) / 500) * 100

#   def gradeGen(self):
#     if self.getPercentage() >= 90:
#       return "A"
#     elif self.getPercentage() < 90 and self.getPercentage() >= 80:
#       return "B"
#     elif self.getPercentage() < 80 and self.getPercentage() >= 65:
#       return "C"
#     elif self.getPercentage() < 65 and self.getPercentage() >= 40:
#       return "D"
#     elif self.getPercentage() < 40:
#       return "E"
  
#   def getDivision(self):
#     if self.getPercentage() >= 60:
#       return "I Division"
#     elif self.getPercentage() < 60 and self.getPercentage() >= 50:
#       return "II Division"
#     elif self.getPercentage() < 50 and self.getPercentage() >= 35:
#       return "III Division"

# # Initializing a new subject
# student = Student(27, "Shaan Alam", "BSc APS")

# # setting marks in marksList list
# student.setMarks()

# # result
# print ("Name = ", student.name)
# print ("Roll no = ", student.rollNum)
# print ("Stream = ", student.stream)
# print ("Percentage = ", student.getPercentage())
# print ("Grade = ", student.gradeGen())
# print ("Division = ", student.getDivision())
class Student:
  def __init__(self):
    self.rollNum = int(input("Enter your Roll Number :"))
    self.name = input("Enter your Name :")
    self.marksList = []
    self.stream = ""
    self.percentage = 0
    self.grade = ""
    self.divison = ""
 
  def setMarks(self):
    print ("Enter marks for 5 subjects: ")
    for x in range(5):
      value = eval(input("Enter marks: "))
      self.marksList.append(value)
  
  def getStream(self):
    print("For Stream Selection press :",'\n',"A : Arts",'\n',"C : Commerce",'\n',"S : Science")
    stream = input("Enter Your Stream:")
    return stream
 
  # getPercentage is used instead of percentage()
  def getPercentage(self):
    return (sum(self.marksList) / 500) * 100
 
  def gradeGen(self):
    if self.getPercentage() >= 90:
      return "A"
    elif self.getPercentage() < 90 and self.getPercentage() >= 80:
      return "B"
    elif self.getPercentage() < 80 and self.getPercentage() >= 65:
      return "C"
    elif self.getPercentage() < 65 and self.getPercentage() >= 40:
      return "D"
    elif self.getPercentage() < 40:
      return "E"
  
  # getDivision() is used instead of division
  def getDivision(self):
    if self.getPercentage() >= 60:
      return "I Division"
    elif self.getPercentage() < 60 and self.getPercentage() >= 50:
      return "II Division"
    elif self.getPercentage() < 50 and self.getPercentage() >= 35:
      return "III Division"
 
# Initializing a new subject
s1= Student()
 
# setting marks in marksList list
s1.setMarks()

# Result
print("Details of the Student :")
print ("Name = ", s1.name)
print ("Roll no = ", s1.rollNum)
print ("Stream = ", s1.getStream())
print ("Percentage = ", s1.getPercentage())
print ("Grade = ", s1.gradeGen())
print ("Division = ", s1.getDivision())