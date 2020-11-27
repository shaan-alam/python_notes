# Strings and characters

char = 'a'
string = 'A is an english alphabet'
message = 'Good Evening!'

# ord(char) => returns the ASCII code for the character passed
print ('ASCII value of "A" = ', ord('A'))

# chr(code) => returns the character value for the ASCII code passed

print ('Character corresponding to ASCII value "65" is = ', chr(65))

# Calculating the uppercase letter given lowercase letter
print (chr(ord('h') - 32))

# Calculating the lowercase letter given uppercase letter
print (chr(ord('H') + 32))

# Escape sequence
print ("He\'s good at programming!")

# Printing without new line
print ('AAAA', end = '\n')


# str function => can be used to convert a number into string
print (str(4.5))

# string concatenation operator
message = "Welcome " + "to " + "Python"  
print (message)


# reading strings from the console

name = input ("Enter your name : ")
print (name)
