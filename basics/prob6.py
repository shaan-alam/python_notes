# Pyramid
space = 8 

for i in range(1, 8):
    for x in range (space):
        print (' ', end = '')

    for j in range(i, 0, -1):
        print (format(str(j), "<s"), end = ' ')

    for k in range(2, i + 1):
        print (format(str(k), "<s"), end = ' ')
    
    print ('\n')
    space -= 1
