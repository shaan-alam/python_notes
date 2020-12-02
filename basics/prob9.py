
space = 7

for i in range(1, 7):
    for x in range(space):
        print (' ', end = '')

    for j in range(i, 0, -1):
        print (j, end = '')

    space -= 1
    print ('\n')
