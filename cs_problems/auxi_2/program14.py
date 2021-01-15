# JAN 15

# Question 14
# WAP to check if a number is armstrong

def isArmstrong(number):
  power = len(str(number))
  sum = 0
  temp = number

  while temp != 0:
    sum = sum + ((temp % 10) ** power)
    temp //= 10


  return sum == number

number = int(input("Enter the number: "))

if isArmstrong(number):
  print (number,"is an armstrong number")
else:
  print (number,"is not an armstrong number")
