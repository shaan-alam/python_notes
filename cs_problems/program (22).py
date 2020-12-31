
# Question 22
# WAP to print the following pattern

# H
# H E
# H E L L
# H E L L O

word = input("Enter the word: ")

for x in range(0, len(word) + 1):
  for j in range(0, x):
    print (word[j], end = " ")
  
  print()