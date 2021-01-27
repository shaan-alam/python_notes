
# JAN 27 

# WAP to transpose a matrix

def getTranspose(matrix):
  transpose = []

  for x in range(len(matrix[0])):
    list1 = []
    for y in range(len(matrix)):
      list1.append(matrix[y][x])

    transpose.append(list1)

  return transpose

def printMatrix(matrix):
  for x in matrix:
    for y in x:
      print (y, end = "\t")
    print()


row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))

matrix = []

for x in range(row):
  list1 = []
  for y in range(col):
    value = eval(input("Enter the matrix element: "))
    list1.append(value)
  
  matrix.append(list1)

transpose = getTranspose(matrix)

print ("Original matrix: ")
printMatrix(matrix)

print ("Transpose of matrix: ")
printMatrix(transpose)