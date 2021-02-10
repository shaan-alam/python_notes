# FEB 10
# WAP to create a dictionary where key must be integer value from 1 to 10
# and value must be cube of respective key


dictionary = {}

for x in range(1, 11):
  dictionary[x] = x ** 3

print (dictionary)