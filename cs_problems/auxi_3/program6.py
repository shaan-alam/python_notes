# FEB 10
# Create a dictionary and retrieve its value and keys

dict = {}

size = int(input("Enter dictionary size: "))

for x in range(size):
  key = input("Enter key: ")
  value = input("Enter value: ")

  dict[key] = value

print ("Original dictionary: ", dict)

print ("Dictionary keys: ", list(dict.keys()))
print ("Dictionary values: ", list(dict.values()))

