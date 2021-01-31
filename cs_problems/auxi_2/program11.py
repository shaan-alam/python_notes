
# JAN 13

# Question 11 - WAP to take values in a list from user and display them.
# Also take the number of values the user want to enter in the list
# Also display the sum of values

size = int(input("Enter the number of items you want: "))

list1 = []
sum = 0

for x in range(0, size):
  
  value = eval(input("Enter the value: "))
  list1.append(value)
  sum += value

print ("List ====== ", list1)
print ("Sum of elements in the list = ", sum)
