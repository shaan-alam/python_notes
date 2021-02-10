# FEB 10
# Write a program to create a dictionary where keys must be strings 
# and values must be count of characters in its respective key

def countCharacters(string):
  count = 0

  for x in string:
    count += 1

  return count

dictionary = {}
size = int(input("Enter the size of the dictionary: "))

for x in range(size):
  key = input("Enter the key: ")
  value = countCharacters(key)

  dictionary[key] = value

print ("Dictionary with keys and values as character count in keys: ")
print (dictionary)