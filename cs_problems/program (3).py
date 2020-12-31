
# Question 3
# WAP to calculate the area of the triangle (if possible, else print an appropriate message)


side1 = eval(input("Enter first side: "))
side2 = eval(input("Enter second side: "))
side3 = eval(input("Entrer third side: "))

s = 0
area = 0

if side1 < (side2 + side3) or side2 < (side1 + side3) or side3 <  (side1 + side2):
    s = (side1 + side2 + side3) / 2
    
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    print ("Area = ", area)

else:
    print ("Area cannot be calculated")
