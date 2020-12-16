def simpleInterest(time, rate, principle):
  SI = (principle * rate * time) / 100
  return SI


time = eval(input("Enter time: "))
rate = eval(input("Enter rate: "))
principle = eval(input("Enter principle amount: "))

SI = simpleInterest(time, rate, principle)

print ("SI : ", SI)