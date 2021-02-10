# FEB 10
# Write a program that takes a sentence as input from the user
# and compute the frequency of each letter. Use variable dictionary type to maintain the count.

def count(string, char):
  count = 0

  for x in string:
    if x == char:
      count += 1

  return count

string = input("Enter the string: ")
dictionary = {}

for x in string:
  if x != ' ':
    dictionary[x] = count(string, x)

print ("Result = ")
print (dictionary)