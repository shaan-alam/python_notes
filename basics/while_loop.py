import random

# A while loop executes statements repeatedly as long as a condition remains true

# syntax
# while loop-condition:
#   loop body
#   statements(s)

count = 0
while count < 11:
    print (count)
    count += 1

# Repeated substraction game
number1 = eval(input("Enter a number: "))
number2 = eval(input("Enter another number: "))

if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input("What is " + str(number1) + " - " + str(number2) + " = ? "))

while number1 - number2 != answer:
    answer = eval(input("Wrong answer. Try answering again = "))

print ("You got it")
