# JAN 13

# Question 8 - WAP to display sum of digits of a number

num = eval(input("Enter a number: "))

sum = 0
temp = num

while temp != 0:
  sum = sum + (temp % 10)
  temp //= 10

print ("Number entered : ", num)
print ("Sum of digits : ", sum)