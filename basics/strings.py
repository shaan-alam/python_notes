string = 'Welcome'

# lower() => Converts all letters to lowercase
print (string.lower())

# upper() => Converts all letters to uppercase
print (string.upper())

# strip() => remove whitespace characters from both the ends of the string
print (string.strip()) 

# Formatting numbers and strings

# Formatting with scientific notation
print (format(57.45679, "9.3e"))

# Formatting with float values
print (format(57.456, '10.3f'))

# Formatting with % => multiply number with 100 and formats the string
print (format(57.456, '10.2%'))

# Justifying formats => You can justify the strings with > for right justification and < for left justification
print (format(54.74564, "<10.2f"))

# Formatting integers
# d = decimal
# o = octal
# x = hexadecimal
# b = binary

print (format(78656, "10d"))
print (format(78656, "<10d"))
print (format(78656, "10x"))
print (format(78656, "<10x"))
print (format(78656, "10x"))

# Formatting strings
print (format("Shaan ", ">20s"))

print (format(0.457467657, "9.3%"))
