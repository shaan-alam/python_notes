# JAN 20

# Question 17 - WAP to print element of a list after removing even numbers from it

n = int(input("Enter the size of list: "))
list1 = []

for x in range(n):
  value = eval(input("Enter a value: "))

  list1.append(value)

print ("Original list : ", list1)

for x in list1:
  if x % 2 == 0:
    list1.remove(x)

print ("After removing even numbers from the list: ", list1)