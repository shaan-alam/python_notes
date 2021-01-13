
# DATE - JAN 8

# Question 6
# Write a function to compute gcd, lcm of two numbers.Both functions must take numbers as arguments

def gcd(number1, number2):
  gcd = 0

  i = 1

  while i <= number1 and i <= number2:
    if number1 % i == 0 and number2 % i == 0:
      gcd = i
    
    i += 1

  return gcd


def lcm(number1, number2):
  return (number1 * number2) / gcd(number1, number2)
  

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print ("GCD = ", gcd(num1, num2))
print ("LCM = ", lcm(num1, num2))