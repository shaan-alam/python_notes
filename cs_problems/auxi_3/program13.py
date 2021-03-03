# FEB 24
# Question 14 - Define a class Rectangle. The class should contain sides: length and breadth of the rectangle as data members. It should report the following methods

# (a) - __init__ for initializing data members length and breadth
# (b) - setLength() for updating the length of the rectangle
# (c) - setBreadth() for updating the breadth of the rectangle
# (d) - getLength() for retrieving the length of the rectangle
# (e) - getBreadth() for retrieving the breadth of the rectangle
# (f) - area() to find the area of the rectangle
# (g) - perimeter() to find the perimeter of the rectangle


class Rectangle:
  length = 0
  breadth = 0

  def __init__(self, len, bre):
    self.length = len
    self.breadth = bre
  
  def setLength(self, newLength):
    self.length = newLength
  
  def setBreadth(self, newBreadth):
    self.breadth = newBreadth
  
  def getLength(self):
    return self.length
  
  def getBreadth(self):
    return self.breadth
  
  def area(self):
    return self.length * self.breadth

  def perimeter(self):
    return 2 * (self.length + self.breadth)


rect = Rectangle(10, 20)

print ("Rectangle dimensions: ")
print (rect.length, rect.breadth)

print ("Updating rectangle dimensions: ")
rect.setLength(20)
rect.setBreadth(40)

print ("New dimensions: ")
print (rect.getLength(), rect.getBreadth())

print ("Area of rectangle: ")
print (rect.area())

print ("Perimeter of rectangle: ")
print (rect.perimeter())

