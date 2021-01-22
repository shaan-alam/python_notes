# DATE - JAN 22

# Question 1 - Write a menu driven program to invoke function to calculate area of square,
# rectangle, circle and triangle. Use suitable assertions

print ("1 - Area of square")
print ("2 - Area of rectangle")
print ("3 - Area of triangle")
print ("4 - Area of circle")

choice = int(input("Enter your choice: "))

def areaSqr(length, widht):
  assert length > 0 and width > 0, "Please enter non-zero dimensions!"

  return length * width

def areaRect(length, width):
  assert length > 0 and width > 0, "Please enter non-zero dimensions!"

  return length * width

def areaTri(base, height):
  assert base > 0 and height > 0, "Please enter non-zero dimensions!"

  return 0.5 * base * height

def areaCircle(radius):
  assert radius > 0, "Please enter non-zero dimensions!"

  return 3.14 * (radius ** 2)

if choice == 1:
  length = eval(input("Enter length of square : "))
  width = eval(input("Enter width of square : "))

  print ("Area of square: ", areaSqr(length, width))

elif choice == 2:
  length = eval(input("Enter length of square : "))
  width = eval(input("Enter width of square : "))

  print ("Area of Rectangle: ", areaRect(length, width))

elif choice == 3:
  base = eval(input("Enter base of square : "))
  height = eval(input("Enter height of square : "))

  print ("Area of Triangle: ", areaTri(base, height))

elif choice == 4:
  radius = eval(input("Enter radius: "))
  print ("Area of circe:", areaCircle(radius))

else:
  print ("Wrong choice entered....Try again!!")