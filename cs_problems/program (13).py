
# Question 13
# WAP to enter the row from user and print the following pattern

# *
# * *
# * * *
# * * * *
# * * * * *


row = int(input("Enter row : "))

for i in range(1, 6):
    for j in range(1, i + 1):
        print ("*", end = " ")

    print ("\n")
