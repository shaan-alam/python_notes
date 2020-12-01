gcd = 1
k = 2

n1 = eval(input("Enter the first number : "))
n2 = eval(input("Enter the second number : "))

while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1

print ("GCD = ", k)

