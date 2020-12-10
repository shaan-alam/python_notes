# Lists 
# Ordered Sequence
# Flexible
# Can store many type of data
# Mutable

mix = [2, 3.7, 'hi']

# Printing the type
print (type(mix))

# Printing the whole list
print ("List = ", mix)

# Printing the individual list items
print ("First item = ", mix[0])
print ("Second item = ", mix[1])
print ("Third item = ", mix[2])

# Extracting data from list
# Syntax = list[<start_index>:<end_index>] => <end_index> is not included
print (mix[0:3])

# Changing list items
mix[0] = 'First element'
print ("After changing the first element : ", mix)

# Changing the whole list
mix = [0, 1, 2, 3, 4]
print ("After changing the whole list : ", mix)

# List methods

fruits = ['apple', 'banana', 'guava', 'mango']

# len(list) => to get the length of the list
print ("Length of fruits list : ", len(fruits))

# Creating list from list constructor
list = list((1, 2, 3, 4))
print (list)

# Negative indexing
print ("Last Item = ", fruits[-1])

# Extracting whole list
print (fruits[0:])

# in keyword
print ('banana' in fruits)

# appending to list
fruits2 = ["orange", "pineapple", "strawberries"]
fruits.extend(fruits2)

print ("After extending the list : ", fruits)

