string = input("Enter the string: ")

count = 0

for char in string:
    if char == 'a':
        count += 1

print ("String = ", string)
print ("Frequency of 'a' in the string : ", count)
