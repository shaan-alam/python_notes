# FEB 12
# Binary search implementation

def binary_search(list, x):
  start = 0
  end = len(list) - 1
  mid = (start + end) // 2

  position = -1

  while start <= end:
    mid = (start + end) // 2

    if x == list[mid]:
      position = mid
      return position
    elif x > list[mid]:
      start = mid + 1
    elif x < list[mid]:
      end = mid - 1


list1 = []
size = int(input("Enter the size of the list: "))

for x in range(size):
  value = eval(input("Enter the value: "))
  list1.append(value)

print ("List = ", list1)

number = eval(input("Enter the number you want to search: "))

if binary_search(list1, number) >= 0:
  print (number,"found at index ",binary_search(list1, number))
else:
  print (number,"doesnt exists in the list")