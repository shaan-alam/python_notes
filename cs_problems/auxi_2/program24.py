
# JAN 27
# Question 24 - WAP to print the sum of two matrix

def takeInput(row, col):
  matrix = []

  for x in range(row):
    row = []
    for y in range(col):
      value = eval(input("Enter a value: "))      
      row.append(value)

    matrix.append(row)

  
  return matrix

def getSum(matrix, matrix2):
  result = []

  for x in range(len(matrix)):
    list1 = []
    for y in range(len(matrix[0])):
      sum = matrix[x][y] + matrix2[x][y]
      list1.append(sum)
    
    result.append(list1)

  return result

def printMatrix(matrix):
  for x in matrix:
    for y in x:
      print (y, end = "\t")
    print()

row = int(input("Enter no of rows: "))
col = int(input("Enter no of columns: "))

print("Input first matrix: ")
matrix = takeInput(row, col)
print("Input second matrix: ")
matrix2 = takeInput(row, col)

sum = getSum(matrix, matrix2)

print ("First matrix: ")
printMatrix(matrix)

print ("Second matrix: ")
printMatrix(matrix2)

print ("Sum of matrix: ")
printMatrix(sum)


