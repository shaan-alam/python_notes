# Calendar

year = int(input("Enter year :" ))
day = int(input("Enter day : "))


filler = 1

for i in range(6):
    for space in range(day):
        print ("\t", end = '')
    
    for x in range(day, 8):
        if filler < 31:
            print (filler, end = '\t')
            filler += 1

    print ('\n')
    day = 1

