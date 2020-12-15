# List methods
list = [15, 21, 34, 54, 12, 43]

# sort() => sorts the list
list.sort() # sorts the original list and return None
print (list)

# reverse() => reverses the list
list.reverse()
print (list)

# append() => insert the element at the last of the list
list.append(10)
list.append(20)
print (list)

# insert(x, y) => insert x at y position
list.insert(1, 42)
print (list)

# pop(x) => removes the element at index 2 and return its value
# pop() => removes the last element from the list
list.pop(2)
print (list)

# remove(x) => removes x from the list
list.remove(21)
print (list)


