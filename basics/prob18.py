def isPrime(n):
    factors = 0

    for i in range(2, n):
        if n % i == 0:
            factors += 1
    
    if factors == 0:
        return True
    else:
        return False

def main():
    count = 0

    for value in range(1, 10001):
        if isPrime(value):
            count += 1

    print ('Number of Prime numbers between 1 & 10000 = ', count)

main()


