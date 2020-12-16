
def calculateArea(side1, side2, side3):
  if side1 < (side2 + side3) and side2 < (side1 + side3) and side3 <  (side1 + side2):
      s = (side1 + side2 + side3) / 2
      
      area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
      print ("Area = ", area)

  else:
      print ("Area cannot be calculated")


side1 = eval(input("Enter side 1: "))
side2 = eval(input("Enter side 2: "))
side3 = eval(input("Enter side 3: "))

calculateArea(side1, side2, side3)