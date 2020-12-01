number = 12000
start = 1
result = -1

while True:
    if start ** 2 > number:
        result = start
        break
    
    start += 1

print ('Result = ', result)
