# Question 1

divisors = []

number = int(input("Enter a number: "))

for x in range(1, number + 1):
  if number % x == 0:
    divisors.append(x)

print ("Divisor's list : ", divisors)
