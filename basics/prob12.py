number = int(input("Enter the number : "))

sum_of_divisors = 0

for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i

if sum_of_divisors == number:
    print ("Perfect number.")
else:
    print ("Not a perfect number.")

