import random

# Generate random number between 0 and 9 using randint()
print (random.randint(0, 9))

# Generate random number between 0 and 9 using randrange()
print (random.randrange(0, 10))

# Generate a random float between 0 and 1
print (format(random.random(), ".2f"))

# if statements => already practiced

x = 5
y = x > 10 and True or  False

y= True if x > 10 else False
print (y)
