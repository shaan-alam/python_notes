# Jan 13

# Question 9 - WAP that will check all items in the list.
# If the items are number display their sum, if items are string, 
# display after concatenating them

list1 = [1, 2, "three", 4, "five", "six", 7]

string = ""
sum = 0

for x in list1:
  if type(x) == int or type(x) == float:
    sum += x
  elif type(x) == str:
    string += x
  

print ("String concatenation: ", string)
print ("Sum of numbers : ", sum)