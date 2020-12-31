
# Question 5
# WAP to find the square root of a number

number = eval(input("Enter a number: "))

if number < 0:
    print ("Please enter a positive number..")
else:
    sqrt_number = number ** 0.5
    print ("Square root of ", number, " is = ", sqrt_number)


