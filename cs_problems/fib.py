
n = int(input("Enter no of terms : "))

if n <= 0:
    print ("Please enter a non-zero positive integer...")
else:
    a = 0
    b = 1
    c = a + b

    print ("Fibonnaci series upto",n,"terms : ")

    for x in range(n):
        print (a)

        a = b
        b = c
        c = a + b
