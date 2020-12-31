# Question 23
# WAP to print the following pattern.

# A
# B C
# D E F
# G H I J
# K L M N O

char = input("Enter the last character: ")
row = 1

for x in range(65, ord(char) + 1):
  for j in range(row):
    print (ord(x), end= " ")  
    x += 1
  print ()
