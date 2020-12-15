# string functions
story = "Once upon a time, there was a code named Shaan Alam who learned Python"

# string functions
print (len(story))

# endswith()
print (story.endswith("Python")) # True

# count() => count the number of characters
print (story.count(' '))
print (story.count("Shaan"))

# capitalize() => capitalizes the string
print (story.capitalize())

# find() => finds a word in the string
print (story.find('Shaan')) # gives only the first occurence

# replace() => replace a string
print (story.replace('Shaan', 'shaancodes')) # replaces every occurence
