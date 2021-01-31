# JAN 29

# Question 27
# WAP to create a list of 10 integers. Accept the values from user in that list.
# Input another number from the user and find out how many numbers are equal to the number passed.
# How many numbers are greater and how many numbers are less than the number passed.

list1 = []

equal = []
greater = []
smaller = []

def printList(list):
  for x in list:
    print (x, end = "\t")

for x in range(10):
  value = eval(input("Enter a value: "))
  list1.append(value)

number = eval(input("Enter a number you want to check: "))

for x in list1:
  if x == number:
    equal.append(x)
  elif x < number:
    smaller.append(x)
  elif x > number:
    greater.append(x)

print ("No of numbers smaller than",number,"=",len(smaller))
printList(smaller)
print()

print ("No of numbers equal to",number,"=",len(equal))
printList(equal)
print()

print ("No of numbers greater than",number,"=",len(greater))
printList(greater)
print()