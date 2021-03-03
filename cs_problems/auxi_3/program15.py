# FEB 24
# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * (self.radius ** 2)
  
  def perimeter(self):
    return 2 * 3.14 * self.radius
  

circle = Circle(20)

print ("Radius of the circle = ", circle.radius)
print ("Area of the circle = ", circle.area())
print ("Perimeter of the circle = ", circle.perimeter())
