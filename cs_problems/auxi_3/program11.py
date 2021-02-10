# FEB 10 
# Write a program that takes a sentence as input from the user
# and compute the frequencey of each vowel. Use a variable dictionary 
# type to maintain the count


def count(string, char):
  count = 0

  for x in string:
    if x.lower() == char:
      count += 1

  return count

vowels = 'aeiou'
string = input("Enter the string: ")

dictionary = {}

for x in vowels:
  dictionary[x] = count(string, x)

print ("Result = ")
print (dictionary)