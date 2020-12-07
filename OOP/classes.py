
import math

class Circle:
    radius = 0
    area = 0

    def __init__(self, radius):
        self.radius = radius
        self.area = 0 

    def getRadius(self):
        return self.radius

    def getArea(self):
        return math.pi * math.pow(self.radius, 2)
    
    def setRadius(self, newRadius):
        self.radius = newRadius
        self.area = self.getArea()
        

circle1 = Circle(3)


print ('Circle radius : ', circle1.getRadius())
print ("Circle area : ", circle1.getArea())

# Setting new radius

circle1.setRadius(100)

print ('Circle new area : ', circle1.getArea())

