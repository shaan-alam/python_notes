
# Question 6
# WAP to find the area of the rectangle

length = eval(input("Enter the length: "))
breadth = eval(input("Enter the breadth: "))

area = 0

if length <= 0 or breadth <= 0:
    print ("Please enter non-zero positive dimensions.")
else:
    area = length * breadth
    print ("Area = ", area)


