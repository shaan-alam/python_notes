sum = 0
i = 0

while i < 1001:
    sum += i
    i += 1

print (sum)

sum = 0

for i in range(sum, 10000):
    sum = sum + i
    i += 1

print (sum)


count = 0 
loopCount = 0
n = 16

while count < n:
    count += 3 
    loopCount += 1

print ('loop count = ', loopCount)

for i in range(1, 5):
    j = 0
    while j < i:
        print (j, end = ' ')
        j += 1


