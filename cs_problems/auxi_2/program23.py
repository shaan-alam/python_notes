# JAN 27
# Question 23 - WAP python program to create a matrix that will take values from the user
# Also display the matrix


matrix = []
row = int(input("Enter the row size of matrix: "))
col = int(input("Enter the column size of matrix: "))

for x in range(row):
  list1 = []
  for y in range(col):
    value = eval(input("Enter the matrix element: "))
    list1.append(value)
  
  matrix.append(list1)

print ("MATRIX = ")

for x in range(row):
  for y in range(col):
    print (matrix[x][y], end = "\t")
  print()