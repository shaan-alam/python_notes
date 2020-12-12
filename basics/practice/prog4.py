string = input("Enter a string: ")

reverse = ""

for x in string:
    reverse = x + reverse

print ("Original string : ", string)
print ("Reversed string : ", reverse)
