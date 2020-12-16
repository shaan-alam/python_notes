# An empty set can be created using the below syntax
a = set()

# Printing the type of object
print (type(a))

# add() => used to add an item to the set
a.add(4)
a.add(40)
a.add(5)
a.add((1, 2, 3)) # tuple can be added to set because it is hashable and cannot be changed
# a.add([1, 2, 3]) list cannot be added to set because list can be changes
# a.add({4:5}) dict is not hashable and its content can be changed, thats why it cannot be added to set
print (a)
# len() => returns the length of set
print (len(a))

# remove() => removes an item from the set
a.remove(4)

# pop() => removes an item and retuns it
print (a.pop())
print (a)

# clear() => empties the set
a.clear()
print (a)

# union() => returns a new set with all items from both the sets
a = {1, 2, 3, 4}
b = {5, 6, 7, 8}

print(a.union(b))

# intersection() => returns the intersection of two sets
print (a.intersection(b))