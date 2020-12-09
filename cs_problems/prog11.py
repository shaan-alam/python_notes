import math

number1 = eval(input("Enter the first number : "))
number2 = eval(input("Enter the second number : "))

print ("+ - Addition.")
print ("- - Substraction.")
print ("* - Multiplication.")
print ("/ - Division.")
print ("^ - Find Power.")
print ("% - Find remainder.")
choice = input("Enter your choice : ")

print ("First number = ", number1)
print ("Second number = ", number2)

if choice == '+':
    sum = number1 + number2
    print ("Sum = ", sum)
elif choice == '-':
    difference = number1 - number2
    print ("Difference = ", difference)
elif choice == '*':
    product = number1 * number2
    print ("Product = ", product)
elif choice == '/':
    quotient = number1 / number2
    print ("Quotient = ", quotient)
elif choice == '^':
    powerValue = math.pow(number1, number2)
    print ("Number1 ^ Number2 = ", powerValue)
elif choice == '%':
    remainder = number1 % Number2
    print ("Remainder = ", remainder)
else:
    print ("Wrong choice entered...Please try again!!")
