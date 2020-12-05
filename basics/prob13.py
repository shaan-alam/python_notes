# reverse a number 

def reverse(number):
    reverse = 0
    temp = number
    
    while number != 0:
        reverse = reverse * 10 + (number % 10)
        number = int(number / 10)

    return reverse


def main():
    number = int(input("Enter a number: "))

    print ("Original Number : ", number)
    print ("Reversed Number : ", reverse(number))

main()

