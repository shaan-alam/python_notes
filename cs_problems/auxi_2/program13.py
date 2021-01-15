# JAN 15
# Question - 13
# WAP to find the max element in a list.
# Take the numbers from the user in the list and also how many
# elements user wants in his list

size = int(input("Enter the size of the list: "))
list1 = []

for i in range(0, size):
  value = eval(input("Enter value: "))
  list1.append(value)

max = list1[0]

for i in list1:
  if i > max:
    max = i
  

print ("List = ", list1)
print ("Max element = ", max)

