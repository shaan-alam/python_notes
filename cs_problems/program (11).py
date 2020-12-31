
# Question 11
# WAP to swap the values of two numbers.

number1 = eval(input("Enter the first number : "))
number2 = eval(input("Enter the second number : "))

print ("Before Swapping : ")
print ("First Number :", number1)
print ("Second Number :", number2)

temp = number1
number1 = number2
number2 = temp 

print ("After Swapping : ")
print ("First Number :", number1)
print ("Second Number :", number2)
