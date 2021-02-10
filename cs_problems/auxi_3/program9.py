# FEB 10
# WAP to create a dictionary where key must be integer value from 1 to n
# (entered by the user) and value must be factorial of respective key

def getFactorial(x):
  fact = 1

  for x in range(1, x + 1):
    fact *= x
  
  return fact

dictionary = {}
n = int(input("Enter the size of the dictionary: "))

for x in range(1, n + 1):
  factorial = getFactorial(x)
  dictionary[x] = factorial


print ("Dictionary with key and factorial of keys: ")
print (dictionary)