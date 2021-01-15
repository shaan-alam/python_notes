# JAN 15
# Question 15 - WAP to print armstrong numbers in the range
# provided by the user


def isArmstrong(number):
  power = len(str(number))
  sum = 0
  temp = number

  while temp != 0:
    sum = sum + ((temp % 10) ** power)
    temp //= 10


  return sum == number


start = int(input("Enter the starting range: "))
end = int(input("Enter the starting range: "))

for i in range(start, end + 1):
  if isArmstrong(i):
    print (i)
  
