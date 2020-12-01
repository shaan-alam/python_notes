print ("CHAR", format("ASCII", ">10s"))

for i in range(ord('!'), ord('~') + 1):
    print (format(chr(i), "5s"), format(str(i), ">5s"))
