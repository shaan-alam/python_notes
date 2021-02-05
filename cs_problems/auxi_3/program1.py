# FEB 3

# Write a function called “check_duplicates” that takes a list and returns true if there is any element that appears 
# more than once. Also find the frequency of that element. The original list should not be modified.

def check_duplicates(list, x):
  return list.count(x) > 1

size = int(input("Enter the size of the list: "))
list1 = []

for x in range(size):
  value = eval(input("Enter a value: "))
  list1.append(value)

checked = []
duplicates = 0

for x in list1:
  if check_duplicates(list1, x) and checked.count(x) == 0:
    print (x,"appears",list1.count(x),"times.")
    checked.append(x)
    duplicates += 1


if duplicates == 0:
  print ("No duplicates found")