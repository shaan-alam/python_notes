# FEB 24

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

