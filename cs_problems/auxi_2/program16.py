
# JAN 15
# Question 16
# WAP to display armstrong number within a list. Take input in list 
# from user


def isArmstrong(number):
  power = len(str(number))
  sum = 0
  temp = number

  while temp != 0:
    sum = sum + ((temp % 10) ** power)
    temp //= 10


  return sum == number

size = int(input("Enter the size of the list: "))
list1 = []

for i in range(0, size):
  value = int(input("Enter value: "))
  list1.append(value)

print ("List ==> ", list1)
print ("Armstrong numbers in the list are: ")

for i in list1:
  if isArmstrong(i):
    print (i)