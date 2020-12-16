# Dictionary => Collection of key value pairs
myDict = {
  "Fast": "In a quick manner",
  "Shaan Alam": "Web developer",
  "Marks": [100, 100, 98, 90],
  "name": {
    "firstName": "Shaan",
    "lastName": "Alam"
  },
  1: 10 # can also contain int as key
}

# accessing my dictionary
print (myDict['Shaan Alam'])
print (myDict['Marks'])
print (myDict['name']['firstName'])
print (myDict[1])

# Dictionary methods

# keys() => returns all the keys.
print (list(myDict.keys()))

# values() => returns the values of the dictionary
print (list(myDict.values()))

# items() => returns the (key, value) for all contents
print (list(myDict.items()))


# update() => helps adding item in the dict
newDict = {
  "newKey": "new value",
  "Shaan Alam": "Coder & Web Developer"
}
myDict.update(newDict)
myDict.update({ "newKey2": "newValue2" })

print (myDict)

# Accessing myDict values

# get() => returns the value of a key from the dictionary
print (myDict.get('Shaan Alam2')) # returns None if the key is not present in the dictionary
print (myDict['Shaan Alam']) # Throws an error if the key is not present in the dictionary

