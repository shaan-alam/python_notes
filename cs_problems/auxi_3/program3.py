# FEB 5
# Linear search example

A = [1, 3, 5, 67, 34, 22, 90]

pos = -1
found = False


for x in range(len(A)):
  if A[x] == 22:
    found = True
    pos = x
    break


if found:
  print ("Position of 22 = ", pos)
else:
  print ("22 not found!!")