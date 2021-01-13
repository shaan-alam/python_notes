
# DATE - JAN 8

# Question 5
# WAP to display the occurence of particular character/word in the given string

string = input("Enter the string: ")
char = input("Enter the character you want to find occurence : ")

count = 0

for x in string:
  if x == char:
    count += 1

print ("Occurence of ",char,"in string",string,"is = ", count)
