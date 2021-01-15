# JAN 13

# Question 12 - WAP to check if a string is palindrome

def rev(string):
  return string[::-1]


string = input("Enter the string: ")

if (string == rev(string)):
  print (string,"is a palindrome string")
else: 
  print (string, "is not a palindrome string")