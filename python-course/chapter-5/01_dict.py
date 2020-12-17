# Dictionary => Collection of key value pairs
myDict = {
  "Fast": "In a quick manner",
  "Shaan Alam": "Web developer",
  "Marks": [100, 100, 98, 90],
  "name": {
    "firstName": "Shaan",
    "lastName": "Alam"
  }
}

# adding items into dict
myDict['city'] = 'New Delhi'

# accessing my dictionary
print (myDict['Shaan Alam'])
print (myDict['Marks'])
print (myDict['name']['firstName'])
print (myDict['city'])
