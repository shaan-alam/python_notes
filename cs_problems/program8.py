number = eval(input("Enter the number: "))

print ("Factors of ", number, " are : ")

for x in range (1, number + 1):
    if number % x == 0:
        print (x)
