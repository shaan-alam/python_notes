# JAN 20

# Question 18 - WAP to append a list to the second list

def readList():
  result = []
  size = int(input("Enter the list size: "))

  for x in range(size):
    value = eval(input("Enter the value: "))
    result.append(value)

  return result

list1 = readList()
list2 = readList()
list1.append(list2)

print ("List 1 : ", list1)
print ("List 2 : ", list2)
print ("Result : ", list1)