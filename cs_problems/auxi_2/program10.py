# JAN 13

# Question 10 - WAP to take values in a list from user and display them.
# Also take the number of values the user want to enter in the list

size = int(input("Enter the number of items you want: "))

list1 = []

for x in range(0, size):
  
  value = eval(input("Enter the value: "))
  list1.append(value)

print ("List ====== ", list1)
