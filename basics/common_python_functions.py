# Common python functions
import math
x = -10

# absolute function to calculate the absolute value
print ('Absolute value ' , abs(x))

# max function to calculate the maximum of numbers
print ('Max value ', max(1, 2, 3, 4, 5))

# min function to calculate the minimum of numbers
print ('Min value ', min(1, 3, 4, 5))

# pow function to calculate the power of a number
print ('value after rasised to something (pow) ', pow(3, 4))

# round function to calculate the rounded value of a number
print ('Rounded value ', round(3.4))
print ('Rounded value after some decimal points ', round(3.44, 1))


# ceil rounds x up to its nearest integer
print ('Rounded up value (ceil)', math.ceil(3.4))

# floor rounds x down to its nearest integer
print ('Rounded down value (floor) ', math.floor(3.4))

# fabs returns the absolute value for x as float 
print ('Absolute value as float (fabs)', math.fabs(-4))

# exp returns the exponential value
print ('Exponential value ', math.exp(1)) 

# log returns the log value
print ('Log value (without specifying base)', math.log(10))
print ('Log value ', math.log(10, 10))

# sqrt returns the square root of the number passed
print ('Square root value of 625 ', math.sqrt(625))



