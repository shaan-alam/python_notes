# Display three numbers in sorted manner

def displaySortedNumber(num1, num2, num3):
    # To keep a check if numbers have been sorted   
    sorted = False

    while sorted != True: 
        # swap the numbers if they aren't in ascending order
        if num1 > num2:
            num1, num2 = num2, num1

        # swap the numbers if they aren't in ascending order
        if num2 > num3:
            num2, num3 = num3, num2

        # swap the numbers if they aren't in ascending order
        if num1 > num3:
            num1, num3 = num3, num1
        
        # Check if all the numbers have been sorted
        if num1 < num2 and num2 < num3 and num1 < num3:
            sorted = True

    return num1, num2, num3

def main():
        
    n1 = eval(input("Enter a number: "))
    n2 = eval(input("Enter a number: "))
    n3 = eval(input("Enter a number: "))
    
    n1, n2, n3 = displaySortedNumber(n1, n2, n3)

    print ("Sorted numbers : ", n1, n2, n3)

main()

