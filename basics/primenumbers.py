def isPrime(number):
    count = 0
    
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

def main():
    count = 0
    number = 1

    while count != 50:
        if isPrime(number):
            print (number, end = ' ')
            count += 1
        number += 1

main()
