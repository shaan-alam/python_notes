
def sumDigits(n):
    sum = 0

    while n != 0:
        sum += (n % 10)
        n //= 10

    return sum

def main():
    n = int(input("Enter a number: "))

    print ("Sum of digit = ", sumDigits(n))

main()
