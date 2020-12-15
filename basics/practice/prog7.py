# Question 4

def sum_of_multiples(limit):
    sum = 0

    for i in range(limit + 1):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    
    return sum


limit = int(input("Enter the limit : "))
print ("Sum of multiples", sum_of_multiples(limit))
