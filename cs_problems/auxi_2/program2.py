# JAN 6 

# Question 2
# Find the reverse of the string

string = input("Enter the string: ")

reverse = ""

for x in range(len(string) - 1, -1, -1):
  reverse += string[x]

print ("Original string: ", string)
print ("Reversed string: ", reverse)
