# FEB 10
# Write a program to search an element in the list using linear search.
# The searching operation must be performed by function named Lsearch that take two parameters
# list and the number to be searched

def Lsearch(list, elem):
  pos = -1
  found = False

  for x in range(len(list)):
    if list[x] == elem:
      pos = x
      found = True
      break

  if found:
    print (elem,"found at position",pos)
  else:
    print (elem,"doesn't exists in the list")

size = int(input("Enter the list size: "))
list1 = []

for x in range(size):
  value = eval(input("Enter the value: "))
  list1.append(value)

element = eval(input("Enter the element to be searched: "))
print ("Original list: ", list1)
Lsearch(list1, element)