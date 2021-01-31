# JAN 29
# Write a menu driven program in python for the following matrix operations
# 1. Addition of two matrices
# 2. Multiplication of two matrices
# 3. Transpose of a matrix

def readMatrix():
  matrix = []
  row = int(input("Enter no of rows: "))
  col = int(input("Enter no of columns: "))

  for x in range(row):
    row = []
    for y in range(col):
      value = eval(input("Enter a value: "))      
      row.append(value)

    matrix.append(row)

  
  return matrix

def getTranspose(matrix):
  transpose = []

  for x in range(len(matrix[0])):
    list1 = []
    for y in range(len(matrix)):
      list1.append(matrix[y][x])

    transpose.append(list1)

  return transpose

def getSum(matrix, matrix2):

  assert len(matrix) == len(matrix2) and len(matrix[0]) == len(matrix2[0]), "Matrices can't be added."

  result = []

  for x in range(len(matrix)):
    list1 = []
    for y in range(len(matrix[0])):
      sum = matrix[x][y] + matrix2[x][y]
      list1.append(sum)
    
    result.append(list1)

  return result


def multiplyMatrix(matrix1, matrix2, result):

  assert len(matrix1[0]) == len(matrix2), "Matrix cannot be multipled"

  for x in range(len(matrix1)):
    for y in range(len(matrix2[0])):
      for z in range(len(matrix2)):
        result[x][y] += matrix1[x][z] * matrix2[z][y]
        
  
  return result

def printMatrix(matrix):
  for x in matrix:
    for y in x:
      print (y, end = "\t")
    print()


print ("1. Addition of two matrices")
print ("2. Multiplication of two matrices")
print ("3. Transpose of a matrix")

choice = int(input("Enter your choice: "))

if choice == 1:
  matrix1 = readMatrix()
  matrix2 = readMatrix()

  result = getSum(matrix1, matrix2)
  print ("Sum of two matrices: ")
  printMatrix(result)
elif choice == 2:
  matrix1 = readMatrix()
  matrix2 = readMatrix()
  result = []

  for x in range(len(matrix1)):
    list1 = []
    for y in range(len(matrix2[0])):
      list1.append(0)
    result.append(list1)

  result = multiplyMatrix(matrix1, matrix2, result)
  print ("Product of two matrices: ")
  printMatrix(result)
elif choice == 3:
  matrix = readMatrix()

  result = getTranspose(matrix)
  printMatrix(result)




