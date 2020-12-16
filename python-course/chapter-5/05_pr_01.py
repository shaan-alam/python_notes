
# Create a hindi to english dictionary

myDict = {
  "Pankha": "fan",
  "Dabba": "box",
  "Vastu": "Item"
}

print ("Options are : ", list(myDict.keys()))
a = input("Enter the hindi word : ")
print ("THe meaning of your word is: ", myDict.get(a))