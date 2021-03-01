# FEB 26
# Q6 Define a class Student that keeps a record of students. The class should contain the following:
# • data members for every student: rollNo, Name, Class, Section, marks1, marks2, and marks3. Assume that the maximum marks for each subject are 100.
# • an additional data member count to keep a record of the number of objects created for this class. Add appropriate statements in the code to increment the value of count by 1, when an object is created.
# • Also define function members:
#  a constructor function to initialize the members
#  a function grade, that returns the overall grade of the student according to the following criteria:
# A : if percentage ≥ 90
# B : if percentage ≥ 80 and < 90
# C : if percentage ≥ 70 and < 80
# D : if percentage < 70
#  __str__ function to display the details of a student including the overall grade of the student
# Also write statements for the following:
# • create an object s1 of this class for a student Tarun of Class XII A having roll no 15 and marks in three subjects as 83, 93, 86.
# • display the details of the student s1 using __str__ function statement.


class Student:
  count = 0

  def __init__(self, rollNo, Name, Class, Section, marks1, marks2, marks3):
    Student.count += 1

    self.Name = Name
    self.Class = Class
    self.Section = Section
    self.marks1 = marks1
    self.marks2 = marks2
    self.marks3 = marks3
  
  def grade(self):
    percentage = ((self.marks1 + self.marks2 + self.marks3) * 100) // 300

    if percentage >= 90:
      return "A"
    elif percentage >= 80 and percentage < 90:
      return "B"
    elif percentage >= 70 and percentage < 80:
      return "C"
    elif percentage < 70:
      return "D"
    
  def __str__(self):
    return "Name = " + self.Name + "\n" \
    + "Class = " + self.Class + "\n" \
    + "Section = " + self.Section + "\n" \
    + "Marks 1 = " + str(self.marks1) +"\n" \
    + "Marks 2 = " + str(self.marks2) + "\n" \
    + "Marks 3 = " + str(self.marks3) + "\n" \
    + "Grade = " + self.grade()


s1 = Student(15, "Tarun", "XII", "A", 83, 93, 86)  
print (s1.__str__())
print ("No Of objects created: ", Student.count)