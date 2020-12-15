# Tuples

# Creating a tuple
tup = (1, 2, 3, 6, 7, 8)

# Tuple object doesn't support mutability
# chaning the tuple will give error
# tup[1] = 199
# print (tup)

# Empty tuple
emp_tup = ()
print (emp_tup)

# tuple with only single item in it
singleton_tup = (1,)
print (singleton_tup)

# Wrong way of creating a tuple
single_tup = (1) # is not a tuple, is a int
print (type(single_tup)) # gives <class int>

# printing tuple
print (tup)

