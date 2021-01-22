# DATE - JAN 22

# Write a menu driven program using built in string functions to do the following task.
# Menu should be displayed and user must br prompted to enter the choice. Repeat this sequence till 
# the user enters exit options

# Look for a substring in the given string and return its position
# Replace substring "good" with "best" in given string.
# Convert lowercase to uppercase and uppercase to lowercase in the given string
# Exit



while True:
  print ()
  
  string = input("Enter the string: ")
  
  print ("1 - Look for a substring in the given string and return its position.")
  print ("2 - Replace substring \"good\" with \"best\" in given string.")
  print ("3 - Convert lowercase to uppercase and uppercase to lowercase in the given string")
  print ("4 - Exit")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    substring = input("Enter the substring you want to look for : ")

    if string.find(substring) >= 0:
      print ("Substring position = ", string.find(substring))
    else:
      print ("The substring",substring,"doesn't exists in the original string")

  elif choice == 2:
    if string.find("good") >= 0:
      print ("New string: ", string.replace("good", "best"))
    else:
      print ("The string doesn't contains substring \"good\".")

  elif choice == 3:
    print ("New string: ", string.swapcase())

  elif choice == 4:
    print ("You exited.....")
    break

  else: 
    print ("Invalid option...Try again!")