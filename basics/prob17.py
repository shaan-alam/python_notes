def displayPattern(n):
    space = n

    for i in range(1, n + 1):
        for x in range(space):
            print ('\t', end = "")

        for j in range(i, 0, -1):
            print (j, end = '\t')

        print ('\n')
        space -= 1 
        


def main():
    n = int(input("Enter n: "))

    displayPattern(n)

main()
