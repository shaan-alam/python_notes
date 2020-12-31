
# Question 16
# WAP to print the fibonacci series. (using functions)

def fib(n):
  a =  0
  b = 1
  c = a + b

  for x in range(n):
    print (a)

    a = b
    b = c
    c = a + b


terms = int(input("Enter the limit: "))

if terms < 0:
  print ("Please enter positive number.")
else:
  fib(terms)
