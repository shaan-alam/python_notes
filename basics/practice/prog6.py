string = input("Enter the string : ")

vowels = 0
consonants = 0

for x in string:
    if x != ' ':        
        if x == 'a' or x == 'A' or x == 'e' or x == 'E' or x == 'I' or x == 'i' or x == 'o' or x == 'O' or x == 'u' or x == 'U':
            vowels += 1
        else:
            consonants += 1

print ("String : ", string)
print ("No of vowels : ", vowels)
print ('No of consonants : ', consonants)
