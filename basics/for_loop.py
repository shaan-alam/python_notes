# for loop syntax
# for i in range (inititalValue, endValue):
#   statement(s)

# range() => range(a), range(a, b), range(a, b, k)
# k = step value

# 1st type range() function is used here
print ("1st type of for loop")
for i in range(10):
    print (i)

# This for loop will redirect the output in the output.txt file
# 2nd type range() function is used here
print ("2nd type of for loop")
for i in range(0, 10):
    print (i)

# 3rd type for loop is used here, it can also have -ve step value
print ("3rd type of for loop")
for i in range(0, -10, -2):
    print (i)


# backward for loop
print ("Backward counting :")
for i in range(5, 0, -1):
    print (i);
