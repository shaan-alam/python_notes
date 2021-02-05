# FEB 3
# Q write a program that accepts two strings and perform the following using sets 
# (a) convert each string into seperate set
# b) identify and display the common characters between the two sets 
# (c) identify and display distinct character between the two sets

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

set1 = set(str1)
set2 = set(str2)

print ("First string set: ", set1)
print ("Second string set: ", set2)

print ("Common characters: ", set1.intersection(set2))

print ("Distinct Characters: ", set1.union(set2) - set1.intersection(set2) )