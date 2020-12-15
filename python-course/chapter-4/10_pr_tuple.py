# Create a List using []
a = [1, 2, 3, 54, 23]

# List items can be changed
a[0] = 10

# Print the list items using indexes
print (a[3])

# list can be redefined
a = [100, 300, 234, 32, 12, -98, 45, 10, 0, -87]

# We can create a list with items of different types
a = [45, 64, "Shaan", False, 3.9]

# List slicing => same as string slicing
friends = ["John Doe", "Rohan", "Sam", "Shaan", "Brad", "Florin Pop"]

print (friends[:]) # prints the whole list
print (friends[:5]) # prints from 0 to 4
print (friends[4:]) # prints from 4 to end
print (friends[::2]) # prints whole string y skipping 1 value
print (friends[-1]) # Negative slicing
print (friends[-4:-1]) # prints the list from back

