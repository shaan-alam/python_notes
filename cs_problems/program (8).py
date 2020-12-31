
# Question 8
# WAP to find the factors of a number entered by the user

number = eval(input("Enter the number: "))

print ("Factors of ", number, " are : ")

for x in range (1, number + 1):
    if number % x == 0:
        print (x)
