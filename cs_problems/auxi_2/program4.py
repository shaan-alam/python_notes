
# DATE - JAN 8

# Question 4
# WAP that will take the name and phone number from the end user.
# Print name & phone no only if name is in lowercase and length of the phone no is 10, else display "No proper input provided"


name = input("Enter your name :")
phone = int(input("Enter your phone number :"))

if name.islower() and len(str(phone)) == 10:
  print ("Your name = ", name)
  print ("Your phone number = ", phone)
else:
  print ("No proper input provided")