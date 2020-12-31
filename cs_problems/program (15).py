
# Question 15
# WAP to enter two numbers and an operator and perform the respective operation (using functions)

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


def add (num1, num2):
  return num1 + num2

def substract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

def power(num1, num2):
  return math.pow(num1, num2)

def findRemainder(num1, num2):
  return num1 % num2

if choice == '+':
    sum = add(number1, number2)
    print ("Sum = ", sum)
elif choice == '-':
    difference = substract(number1, number2)
    print ("Difference = ", difference)
elif choice == '*':
    product = multiply(number1, number2)
    print ("Product = ", product)
elif choice == '/':
    quotient = divide(number1, number2)
    print ("Quotient = ", quotient)
elif choice == '^':
    powerValue = power(number1, number2)
    print ("Number1 ^ Number2 = ", powerValue)
elif choice == '%':
    remainder = findRemainder(number1, number2)
    print ("Remainder = ", remainder)
else:
    print ("Wrong choice entered...Please try again!!")
