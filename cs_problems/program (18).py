
# Question 18
# Write a function test to check if a number lies within a range.
# Enter staring and ending range values from the user

def test(start, end, number):
  if number >= start and number <= end:
    print (number,"is in range.")
  else:
    print (number,"is out of range.")


start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))
number = int(input("Enter the number: "))

test(start, end, number)
