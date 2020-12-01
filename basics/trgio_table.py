import math 

print ("Degree\tSin\tCos")


for i in range(0, 361, 10):
    print (i, "\t", format(math.sin(i), "1.4f"), "\t", format(math.cos(i), "1.4f"))


