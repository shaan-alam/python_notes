import math

number1 = eval(input("Enter the first number : "))
number2 = eval(input("Enter the second number : "))

print ("1 - Addition.")
print ("2 - Substraction.")
print ("3 - Multiplication.")
print ("4 - Division.")
print ("5 - Find Power.")
print ("6 - Find remainder.")

choice = int(input("Enter your choice : "))

print ("First number = ", number1)
print ("Second number = ", number2)

if choice == 1:
    sum = number1 + number2
    print ("Sum = ", sum)
elif choice == 2:
    difference = number1 - number2
    print ("Difference = ", difference)
elif choice == 3:
    product = number1 * number2
    print ("Product = ", product)
elif choice == 4:
    quotient = number1 / number2
    print ("Quotient = ", quotient)
elif choice == 5:
    powerValue = math.pow(number1, number2)
    print ("Number1 ^ Number2 = ", powerValue)
elif choice == 6:
    remainder = number1 % Number2
    print ("Remainder = ", remainder)
else:
    print ("Wrong choice entered...Please try again!!")
