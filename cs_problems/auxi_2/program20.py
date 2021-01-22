# Jan 20 

# Write a function to determin whether a given number is a perfect number.
# [The perfect number is said to be perfect if it is the sum of its divisors]

def isPerfect(number):
  sum = 0

  for x in range(1, number):
    if number % x == 0:
      sum += x

  return sum == number


number = int(input("Enter a number: "))

if isPerfect(number):
  print (number,"is a perfect number.")
else:
  print (number,"is not a perfect number.")