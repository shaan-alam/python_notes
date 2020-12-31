
# Question 21
# WAP to print the following pattern. (Take the last character from the user)

# A
# A B
# A B C
# A B C D


last_char = input("Enter the last character : ")

i = 65

while i <= ord(last_char):
  j = 65

  while j <= i:
    print (chr(j), end = " ")
    j += 1

  print ()
  i += 1

