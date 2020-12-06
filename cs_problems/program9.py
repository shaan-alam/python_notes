number = int(input("Enter number: "))

factors = 0

for x in range(1, number + 1):
    if number % x == 0:
        factors += 1

if factors == 2:
    print (number, "is a prime number.")
else:
    print (number, "is not a prime number")


