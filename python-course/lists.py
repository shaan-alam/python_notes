# Python lists

list = [1, 2, 3, 4, 5, 6]

# index => returns the index of the specified element in the list
# index => list.index(element, start, end)
# start => start searching from this index
# end => search upto this index

print (list.index(4))

# append => add an item to the end of the list
list.append(7)
list.append(8)
list.append(9)

print (list)

# extend => adds all the elements of an iterable to the end of the list
list2 = [10, 11]
list.extend(list2)
print (list)

# insert => insert an element in to the list at a specific index
list.insert(0, 0)
print (list)

# remove => removes an element from the list
list.remove(8)
list.remove(9)
print (list)

# count => returns the count of an element in the list
print (list.count(0))
