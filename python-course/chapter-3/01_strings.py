firstName = "Shaan"
lastName = "Alam"

# string concatenation
name = firstName + lastName

# String slicing
print (name[0:3]) # => print name from 0 to 3
print (name[0:]) # => print name from 0 to end
print (name[:]) # => print whole string
print (name[:4]) # => print name from 0 to 3 (4 - 1)

# negative indexes
# We can access string character's from behind using negative indexing

print ("Last character : ", name[-1])

# Slicing with negative indexing
print (name[-5:-4])

# Slicing with skip value
# name[start:end:skip_value]
print (name[2:5:2]) # printing name from 2 to 4 by skipping 2 values
