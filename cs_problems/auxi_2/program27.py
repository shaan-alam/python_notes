# JAN 29

# WAP to perform multiplication of two matrices.
# Also assert the condition for multiplication of matrices

def readMatrix():
  row = int(input("Enter no of rows: "))
  col = int(input("Enter no of columns: "))

  matrix = []

  for x in range(row):
    list1 = []
    for y in range(col):
      value = eval(input("Enter matrix element: "))
      list1.append(value)

    matrix.append(list1)

  return matrix

def multiplyMatrix(matrix1, matrix2, result):

  assert len(matrix1[0]) == len(matrix2), "Matrix cannot be multipled"

  for x in range(len(matrix1)):
    for y in range(len(matrix2[0])):
      for z in range(len(matrix2)):
        result[x][y] += matrix1[x][z] * matrix2[z][y]
        
  
  return result

def printMatrix(matrix):
  for x in range(len(matrix)):
    for y in range(len(matrix[0])):
      print (matrix[x][y], end = "\t")

    print ()

matrix1 = readMatrix()
matrix2 = readMatrix()

result = []
  
for x in range(len(matrix1)):
  list1 = []
  for y in range(len(matrix2[0])):
    list1.append(0)
  result.append(list1)

result = multiplyMatrix(matrix1, matrix2, result)

print ("First Matrix: ")
printMatrix(matrix1)
print ("Second Matrix: ")
printMatrix(matrix2)
print ("Resultant Matrix: ")
printMatrix(result)