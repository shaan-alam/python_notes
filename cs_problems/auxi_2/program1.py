# Question 1
# Find the common characters in the string

string1 = input("Enter the string 1 : ")
string2 = input("Enter the string 2 : ")

print ("String 1 :", string1)
print ("String 2 :", string2)

count = 0

print ("Common characters are : ")

dup = "" # to store the duplicate characters

for x in string1:
  if x in string2 and dup.find(x) == -1:
    print (x)
    dup += x
    count += 1


if count == 0:
  print ("There are no common characters in both strings.. ")
else:
  print ("There are ",count,"common characters in the string.")