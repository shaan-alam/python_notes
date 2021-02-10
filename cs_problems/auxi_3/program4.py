# FEB 10
# Write a menu driven program to display the elements of the list in 
# ascending order or descending order as per choice entered by the user

def sortAscending(list):
  for x in range(len(list) - 1):
    for y in range(x + 1, len(list)):
      if list[y] < list[x]:
        list[x], list[y] = list[y], list[x]

  return list


def sortDescending(list):
  for x in range(len(list) - 1):
    for y in range(x + 1, len(list)):
      if list[y] > list[x]:
        list[x], list[y] = list[y], list[x]

  return list

size = int(input("Enter the size of the list: "))
list1 = []

for x in range(size):
  value = eval(input("Enter the value: "))
  list1.append(value)


print ("Original List: ",list1)

print ("1 - Sort in ascending order")
print ("2 - Sort in descening order")

choice = int(input("Enter your choice: "))

if choice == 1:
  print ("List sorted in ascending order: ", sortAscending(list1))
elif choice == 2:
  print ("List sorted in descending order: ", sortDescending(list1))