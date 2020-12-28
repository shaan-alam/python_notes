# Question 6  

def areAllDigitsEven(number): 
  result = True

  while number > 0:
    digit = number % 10

    if digit % 2 != 0:
      result = False
      break

    number = number // 10

  return result


for x in range(1000,3001):
  if areAllDigitsEven(x):
    print (x, end = ", ")