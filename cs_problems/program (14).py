
# Question 14
# WAP to enter time, rate, and principle from the user & calculate the 
# simple interest. (using functions) 

def simpleInterest(time, rate, principle):
  SI = (principle * rate * time) / 100
  return SI


time = eval(input("Enter time: "))
rate = eval(input("Enter rate: "))
principle = eval(input("Enter principle amount: "))

SI = simpleInterest(time, rate, principle)

print ("SI : ", SI)