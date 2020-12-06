def reverse (number):
    reverse = 0

    while number != 0:
        reverse = reverse * 10 + (number % 10)
        number //= 10

    return reverse

def isPalindrome(number):
    reverseNumber = reverse(number)

    if number == reverseNumber:
        return True
    else:
        return False

def main():
    n = int(input("Enter the number : "))

    if isPalindrome(n):
        print (n, "is a palindrome number.")
    else:
        print (n, "is not a palindrome number.")


main()

