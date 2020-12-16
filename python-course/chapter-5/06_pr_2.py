# WAP a program to read numbers from the user and display all the unique numbers

myset = set()

for x in range(8):
  number = int(input("Enter number : "))
  myset.add(number)

print ("Unique values are : ", myset)