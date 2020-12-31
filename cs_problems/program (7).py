
# Question 7
# WAP to print the multiplication table of a number (entered by user).

number = eval(input("Enter number : "))

print ("Multiplication Table of ", number)

for x in range(1, 11):
  print (number, " * ", x, " = ", number * x)

