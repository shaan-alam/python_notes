
# DATE - JAN 8

# Question 3
# WAP to reverse a string. It must use function rev() to reverse the string,
# taking string as an argument and must return the reversed string

def rev(string):
  return string[::-1]

string = input("Enter the string: ")

print ("Original string: ", string)
print ("Reversed string: ", rev(string))
