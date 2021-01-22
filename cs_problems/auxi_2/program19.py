# JAN 20

# Write a function that takes n as an input and creates a list of n lists such
# that ith list contains first five multiples of i

n = int(input("Enter the size of the list: "))

def createList():
  list1 = []

  for x in range(1, n + 1):
    list = []

    for i in range(1, 6):
      list.append(x * i)

    list1.append(list)

  return list1


print ("Required list = ", createList())
